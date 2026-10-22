#!/usr/bin/env python3
"""《괴물은 멸종했습니다》 저장소 검증 도구.

파일을 고치지 않고 읽기만 한다. 사용법과 검사 항목은 tools/README.md에 있다.

    python3 tools/verify.py            # 저장소 어디서 실행해도 된다
    python3 tools/verify.py --root DIR # 다른 사본을 검사할 때

종료 코드: 0 = 오류 없음, 1 = 오류 있음.
"""

import argparse
import collections
import glob
import os
import re
import sys

BANNED_BODY_WORDS = ['환수', '거생종']
PLANNING_TAGS = ['[제안]', '[작가 비밀]', '[초안]', '[보류]']

LINK_RE = re.compile(r'\]\(([^)#\s]+)(#[^)]*)?\)')
DECISION_HEADING_RE = re.compile(r'^## (D-\d+)\.', re.M)
QUESTION_ROW_RE = re.compile(r'^\| (Q-[가-힣]+-\d+) \|', re.M)
DECISION_REF_RE = re.compile(r'D-(\d{3,})')
QUESTION_REF_RE = re.compile(r'Q-[가-힣]+-\d+')
EPISODE_FILE_RE = re.compile(r'^ep(\d+)-.+\.md$')
EPISODE_HEADING_RE = re.compile(r'^## 제(\d+)화', re.M)
META_EPISODE_RE = re.compile(r'제\s?\d+\s?화')
META_VOLUME_RE = re.compile(r'제\s?\d+\s?권')


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def rel(root, path):
    return os.path.relpath(path, root)


def files(root, *patterns):
    out = []
    for pat in patterns:
        out += glob.glob(os.path.join(root, pat), recursive=True)
    return sorted(set(out))


def check_links(root):
    """상대 링크가 가리키는 파일이 있는지 본다. http·mailto와 앞부분 없는 #앵커는 건너뛴다."""
    broken = []
    for f in files(root, 'docs/**/*.md', 'manuscript/**/*.md', '*.md'):
        for m in LINK_RE.finditer(read(f)):
            target = m.group(1)
            if target.startswith(('http:', 'https:', 'mailto:')):
                continue
            path = os.path.normpath(os.path.join(os.path.dirname(f), target))
            if not os.path.exists(path):
                broken.append((rel(root, f), target))
    return broken


def check_decisions(root):
    ids = DECISION_HEADING_RE.findall(read(os.path.join(root, 'docs/decisions.md')))
    dups = [k for k, v in collections.Counter(ids).items() if v > 1]
    return ids, dups


def check_refs(root, decision_ids):
    """문서와 원고에 나온 D·Q 번호가 decisions.md 제목과 open-questions.md 표에 정의되어 있는지 본다."""
    questions = set(QUESTION_ROW_RE.findall(read(os.path.join(root, 'docs/open-questions.md'))))
    defined = set(decision_ids)
    undefined = set()
    for f in files(root, 'docs/**/*.md', 'manuscript/book*/*.md'):
        s = read(f)
        undefined |= {(rel(root, f), 'D-' + n) for n in DECISION_REF_RE.findall(s) if 'D-' + n not in defined}
        undefined |= {(rel(root, f), q) for q in QUESTION_REF_RE.findall(s) if q not in questions}
    return sorted(undefined)


def visible_body(text):
    """머리 주석(<!-- -->)과 제목 줄(#로 시작)을 뺀 원고 본문."""
    body = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    return re.sub(r'^#.*$', '', body, flags=re.M)


def check_manuscripts(root):
    """권마다 회차 파일을 검사한다. 회차 번호는 권 안에서만 겹치면 안 된다."""
    errors, books = [], {}
    for book_dir in sorted(glob.glob(os.path.join(root, 'manuscript', 'book*'))):
        if not os.path.isdir(book_dir):
            continue
        book = os.path.basename(book_dir)
        numbers = collections.defaultdict(list)
        for p in sorted(glob.glob(os.path.join(book_dir, 'ep*.md'))):
            name = os.path.basename(p)
            where = rel(root, p)
            m = EPISODE_FILE_RE.match(name)
            if not m:
                errors.append((where, '파일명이 epNN-제목.md 규칙과 다름'))
                continue
            n = int(m.group(1))
            numbers[n].append(where)
            text = read(p)
            if text.count('<!--') != text.count('-->'):
                errors.append((where, '닫히지 않은 머리 주석'))
            h = EPISODE_HEADING_RE.search(text)
            if not h:
                errors.append((where, '“## 제N화” 제목 없음'))
            elif int(h.group(1)) != n:
                errors.append((where, f'제목 번호({h.group(1)})와 파일 번호({n})가 서로 다름'))
            body = visible_body(text)
            for w in BANNED_BODY_WORDS:
                if w in body:
                    errors.append((where, f'본문 금지어 “{w}”'))
            for w in PLANNING_TAGS:
                if w in body:
                    errors.append((where, f'본문에 기획 표기 {w}'))
            if META_EPISODE_RE.search(body):
                errors.append((where, '본문에 회차 표기(제N화)'))
            if META_VOLUME_RE.search(body):
                errors.append((where, '본문에 권 표기(제N권)'))
            if '"' in body:
                errors.append((where, '본문에 곧은 큰따옴표(")'))
        for n, paths in sorted(numbers.items()):
            if len(paths) > 1:
                errors.append((book, f'회차 번호 {n} 중복: ' + ', '.join(paths)))
        nums = sorted(numbers)
        gaps = sorted(set(range(1, nums[-1] + 1)) - set(nums)) if nums else []
        books[book] = (len(nums), nums, gaps)
    return errors, books


def main():
    ap = argparse.ArgumentParser(description='저장소 링크, 결정·질문 번호, 원고 본문을 검증한다.')
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help='저장소 최상위 폴더 (기본: 이 파일의 상위 폴더)')
    args = ap.parse_args()
    root = os.path.abspath(args.root)
    failed = False

    broken = check_links(root)
    print(f'링크: 깨진 링크 {len(broken)}')
    for f, t in broken:
        print(f'  - {f} → {t}')
    failed |= bool(broken)

    ids, dups = check_decisions(root)
    print(f'결정 번호: 마지막 {ids[-1] if ids else "없음"}, 중복 {", ".join(dups) if dups else "없음"}')
    failed |= bool(dups)

    undefined = check_refs(root, ids)
    print(f'미정의 D·Q 참조: {len(undefined)}')
    for f, ref in undefined:
        print(f'  - {f}: {ref}')
    failed |= bool(undefined)

    errors, books = check_manuscripts(root)
    for book, (count, nums, gaps) in books.items():
        span = f'{nums[0]}~{nums[-1]}화' if nums else '없음'
        note = f', 빠진 번호 {gaps} (오류 아님)' if gaps else ''
        print(f'원고 {book}: {count}편 ({span}){note}')
    print(f'원고 본문 오류: {len(errors)}')
    for where, msg in errors:
        print(f'  - {where}: {msg}')
    failed |= bool(errors)

    print('결과:', '오류 있음' if failed else '통과')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
