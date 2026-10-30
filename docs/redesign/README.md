# P 재설계 문서 지도

> 상태: **작업 지침** (2026-10-30). P(새 출간본) 설계 문서의 권한과 적용 범위를 정한다.
> 공통 규칙은 [AGENTS.md](../../AGENTS.md)에 있다. 이 폴더의 어떤 문서도 AGENTS.md나 작가의 명시적 지시보다 높은 권한을 갖지 않는다.

## 1. W와 P

| 버전 | 뜻 | 정본 위치 | 상태 |
|---|---|---|---|
| W | 작업 원고 W1~W6(`manuscript/book1`~`book6`) | [docs/canon.md](../canon.md), [docs/decisions.md](../decisions.md)(D-001~), characters·world·creatures 문서 | 보존. 더 쓰지 않음 |
| P | 새 출간본 | [p-canon/](p-canon/README.md)(작가가 승인한 P 설정만), [p-canon/decisions.md](p-canon/decisions.md)(P결정-001~) | 설계 중. 원고 없음 |

- **적용 범위:** W의 D 결정은 W에 적용된다. P결정은 P에 적용된다. 두 결정이 다르면 각자 자기 버전에만 적용되고, 서로를 고치지 않는다.
- **번호:** P 결정은 `P결정-001`처럼 쓴다. 기존 D 번호의 뜻을 바꾸거나 다시 쓰지 않는다.
- **입력 자료:** P를 설계할 때 W의 정본은 ‘기존 버전 자료’다. 근거로 인용할 수 있지만 P를 구속하지 않는다.

## 2. 문서의 권한과 적용 범위

| 문서·폴더 | 권한 | 적용 범위 |
|---|---|---|
| [p-canon/](p-canon/README.md) | **P 정본.** 작가가 승인한 P 설정만 담는다 | P |
| [p-canon/decisions.md](p-canon/decisions.md) | P 결정의 근거와 변경 이력 | P |
| [plan.md](plan.md) | 단계별 작업 계획(절차·문서 체계·관문) | P 설계 작업 |
| [checklist.md](checklist.md) | 설계 누락 점검 목록 | P 설계 작업 |
| [conflicts.md](conflicts.md) | 기존 결정·제안서와의 충돌 기록 | W·P 사이 |
| [character-and-naming.md](character-and-naming.md) | 인물 재창조·작명 기준 | P 인물 설계 |
| [candidates/](candidates/history.md) | **P 설계 후보.** 승인 전. 정본 아님 | P |
| `docs/proposals/` | 기존 미승인 제안서. W 시기에 쓴 것 | 후보 자료 |

## 3. 승격 절차

1. 후보는 `candidates/`에 `[P 후보]`로 쓴다.
2. 작가가 승인한 범위만 `p-canon/`의 해당 문서로 옮기고, `p-canon/decisions.md`에 P결정 번호와 근거를 적는다.
3. 승인되지 않은 후보는 다음 설계의 전제로 쓰지 않는다. 쓸 수밖에 없으면 ‘작업 가정’이라고 적는다.
4. 바뀐 P결정은 지우지 않고 [대체됨]으로 표시한다.

## 4. 영역별 위치 (2026-10-30 4단계 개정, P결정-006)

| 영역 | 현재 후보 | 이전 후보(상태) | 정본(승인 뒤) |
|---|---|---|---|
| 가문의 역사(차별·대토벌·연구·독점) | [candidates/house-history.md](candidates/house-history.md)(방향 채택, 세부 후속) | concealment-origins.md(대체), history.md(대체) | p-canon/world.md |
| 감응자 식별과 신호 | [candidates/sensing-identification-v3.md](candidates/sensing-identification-v3.md) | sensing-identification-v2.md(방향 채택, 세부 대체), sensing-identification.md(거절) | p-canon/sensing.md |
| 감응과 사회·가문 계층 | [candidates/sensing-identification-v3.md](candidates/sensing-identification-v3.md) §4·§6 | sensing-identification-v2.md §4~§5(참고), sensing-society.md(보류) | p-canon/sensing.md |
| 감응 기술 | [candidates/sensing-tech.md](candidates/sensing-tech.md)(탐지·해석까지 채택, 4~6단계 보류) | — | p-canon/sensing.md |
| 다중 집결지·집결 모델 | [candidates/gathering-ecology.md](candidates/gathering-ecology.md)(모델·범위 채택, 원리 후보) | anomaly-and-gathering.md(일부 채택·대체) | p-canon/world.md, creatures.md |
| 첫 번째 침묵과 대토벌 | [candidates/silence-and-hunt-v2.md](candidates/silence-and-hunt-v2.md)(일부 보류), [candidates/world-causality.md](candidates/world-causality.md) | first-silence-review.md(구조만 채택) | p-canon/world.md |
| 아르바넬 생존 | [candidates/arbanel-survival.md](candidates/arbanel-survival.md)(일부 채택) | house-world.md(거절) | p-canon/world.md |
| 마지막 집결지 생태·정상 집결과 분산 | [candidates/arbanel-ecology.md](candidates/arbanel-ecology.md)(일부 채택), [candidates/gathering-wonders-review.md](candidates/gathering-wonders-review.md)(현상 선별) | arbanel-survival.md §2(대체) | p-canon/world.md, creatures.md |
| 억류 구조·탈출 | [candidates/containment-v2.md](candidates/containment-v2.md) | containment.md(거절) | p-canon/world.md |
| 첫 탈출 개체와 첫 만남 | [candidates/first-encounter-v2.md](candidates/first-encounter-v2.md) | first-encounter.md(거절) | p-canon/outline.md |
| 마지막 집결지의 이름 | [candidates/site-naming.md](candidates/site-naming.md) | ‘아르바넬’(확정 안 함) | p-canon/world.md |
| 봉인 구역·멸종 선언 | [candidates/seal-declaration-v4.md](candidates/seal-declaration-v4.md)(구조 채택) | declaration-v3.md(구조 채택), refuge-secrecy.md(기본 구조 채택), extinction-declaration.md(거절) | p-canon/world.md |
| 연표 | [candidates/timeline-v3.md](candidates/timeline-v3.md)(‘약 200년’ 가설) | timeline-options.md(보류) | p-canon/world.md |
| 역사·생태의 상호 요구 | [candidates/cross-requirements.md](candidates/cross-requirements.md) | — | — |
| 비밀 원장 | [candidates/secrets-ledger-v6.md](candidates/secrets-ledger-v6.md) | v5·v4·v3·v2·v1(대체) | p-canon/secrets.md |
| 결정 대기·검증·전달 | [candidates/decisions-pending-v6.md](candidates/decisions-pending-v6.md) | v5·v4·v3·v2(대체), recommendations.md(일부 대체) | p-canon/decisions.md |
| 정치 질서·국가·가문·기관 | [candidates/polity.md](candidates/polity.md) | world-powers.md(거절), factions-v2.md(보류), factions.md(대체) | p-canon/factions.md |
| 종교와 신앙 | [candidates/faith.md](candidates/faith.md) | — | p-canon/faith.md |
| 환류종 생태 | candidates/creatures.md(다음 단계) | — | p-canon/creatures.md |
| 인물·관계 | candidates/cast.md, relationships.md | — | p-canon/cast.md, relationships.md |
| 전체 줄거리 | candidates/outline.md | — | p-canon/outline.md |
| 권별·장별 구성 | candidates/volumes/ | — | p-canon/volumes/ |

- 이전 후보 문서는 맨 위에 상태(대체·거절·보류·채택 범위)가 표시되어 있다. 현재 후보와 함께 유효한 것으로 읽지 않는다.
- 이름 표기: P결정-006부터 ‘아르바넬’은 확정 지명이 아니다. 새 이름이 정해질 때까지 P 문서는 ‘마지막 집결지’라고 부른다. 이전 후보 문서의 ‘아르바넬’은 작업명으로 읽는다.

## 5. 작가용 설계 현황판

- 승인·후보·결정 대기·역사·세력·비밀·인물을 한눈에 보는 요약 페이지: https://claude.ai/artifact/TaTynvorHi7Pbb95G6qpVR (비공개, 작가 계정)
- 원본 파일: [status-board.html](status-board.html). 설계 문서가 바뀔 때마다 이 파일을 고치고 같은 주소로 다시 게시한다.
- 현황판은 요약이다. 내용이 다르면 저장소의 문서가 맞다.
