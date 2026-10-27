# 작업 단계별 가이드

> 상태: **작업 지침 (2026-10-25, 사용자 지시 "제5권 설계 전 에이전트 지침 개편", 결정 번호 없음).** 공통 규칙은 [AGENTS.md](../../AGENTS.md)에 있고, 이 문서는 단계마다 무엇을 읽고 어디까지 바꾸고 무엇으로 끝내는지만 정한다.
> 창작 원칙의 내용은 원래 문서에 있다. 여기에는 옮기지 않고 링크만 둔다: [style-guide.md](style-guide.md), [creative-principles.md](creative-principles.md), [adventure-engagement-design.md](adventure-engagement-design.md).
> 작업 지시서가 읽을 문서나 범위를 따로 정하면 그것이 우선한다(AGENTS.md §2).

## 0. 모든 단계에 공통

- 작업 지시서와 해당 권의 현행 지시 요약을 먼저 읽는다.
- `docs/canon.md`, `docs/decisions.md`, `docs/open-questions.md`는 전체를 읽지 않는다. 인물명, 용어, D·Q 번호로 관련 항목을 찾아 확인한다.
- 단계를 섞지 않는다. 집필 중에 전면 검수를 하지 않고, 검수 중에 원고를 다시 쓰지 않는다.
- 점검표와 지표는 진단 도구다. 목표 수치로 쓰지 않는다(AGENTS.md §6).

## 1. 시리즈·권별 기획

| 항목 | 내용 |
|---|---|
| 작업 목표 | 시리즈의 결말 방향과 권별 모험을 인물의 욕망과 선택에서 짠다. 권마다 한 문장 목표, 압박, 실제 변화, 대가, 경이와 보상을 정한다 |
| 우선 읽을 문서 | [creative-principles.md](creative-principles.md) §1~§5, [adventure-engagement-design.md](adventure-engagement-design.md) §4·§5·§7, [series-arc.md](series-arc.md), [foreshadowing.md](foreshadowing.md) §1, 직전 권의 기획 요약과 마지막 회차 |
| 필요할 때만 | [../proposals/series-ending-candidates.md](../proposals/series-ending-candidates.md), [../proposals/long-clue-ledger.md](../proposals/long-clue-ledger.md), [../proposals/lia-long-term-goal.md](../proposals/lia-long-term-goal.md), [../proposals/character-design.md](../proposals/character-design.md), 인물 문서([../characters/](../characters/)), 세계·생물 문서([../world/](../world/), [../creatures/](../creatures/)), [series-revision-backlog.md](series-revision-backlog.md) |
| 허용되는 변경 | 제안 문서 작성과 수정(`docs/proposals/` 또는 권별 기획 문서, `[제안]`·`[초안]` 표기). 정본(canon, decisions, characters, world, creatures)은 사용자 승인 뒤에만 반영한다 |
| 검증 범위 | 앞 권의 확정 사실, 공개 순서([foreshadowing.md](foreshadowing.md)), 열린 미스터리 목록과의 충돌만 본다. 문서를 바꿨으면 `python3 tools/verify.py` |
| 완료 기준 | 권 기획 점검 일곱 가지(adventure §4-1)에 답이 있다. 새 장기 설정과 결말에 닿는 항목은 '사용자 결정 필요'로 따로 묶여 있다 |

- 경이 장면(독자가 처음 보는 것)과 인물의 결정적 선택을 먼저 정하고, 사건과 증거의 인과가 그것을 받치게 짠다.
- 작가가 미확정으로 둘 것과 인물이 알고 믿는 것을 기획 단계에서 따로 적어 둔다.

## 2. 회차 초고 집필

| 항목 | 내용 |
|---|---|
| 작업 목표 | 승인된 회차 플롯과 장면 설계로 읽히는 초고를 쓴다. 인물의 욕망, 선택, 발견의 경험이 장면의 중심이다 |
| 우선 읽을 문서 | 해당 회차의 장면 설계와 회차 플롯, 권별 현행 지시 요약, 앞 회차 원고의 끝부분, [style-guide.md](style-guide.md) §2·§4·§5·§10, 등장인물 문서의 '프로필·말투' 소절(style-guide §8-2) |
| 필요할 때만 | 같은 권 앞 회차 전체(연결되는 사물·약속이 있을 때), canon·decisions의 관련 항목, [../proposals/memorable-lines.md](../proposals/memorable-lines.md), [../research/fantasy-craft-notes.md](../research/fantasy-craft-notes.md) §11-3(참고, 의무 아님) |
| 허용되는 변경 | 새 원고 파일 작성(`manuscript/book{권}/ep{두 자리}-{제목}.md`). 정본과 충돌하지 않는 작은 사물·습관·배경 세부는 자유롭게 만든다. 원고에서 생긴 새 설정은 집필 뒤 decisions나 open-questions에 기록 후보로 보고한다 |
| 검증 범위 | 앞뒤 회차의 사실(날짜, 사물의 위치, 누가 무엇을 아는가), `python3 tools/verify.py`. 회차 평가 일곱 기준(style-guide §7)은 짧은 자기 점검으로만 쓴다 |
| 완료 기준 | 승인된 플롯의 사건과 인과가 원고에 있다. 발견과 감정이 설명보다 먼저 독자에게 닿는다. 새로 만든 설정과 미확정으로 남긴 것이 보고에 적혀 있다 |

- 인물은 자기 지식과 성격대로 확신하거나 틀린다. 작가의 유보를 대사로 대신 말하게 하지 않는다(AGENTS.md §6).
- 같은 깨달음을 서술과 대사로 두 번 설명하지 않는다. 다만 '발견 → 감정 → 반론'을 고정 공식으로 쓰지 않는다.
- 인물 기록 (2026-10-27 사용자 지시): 회차를 쓴 뒤 인물의 목표·선택·관계·소지품·약속·부상처럼 이후에 영향을 주는 상태가 달라졌으면, [../characters/](../characters/)의 해당 인물 문서 '변화 이력'에 권·화 근거로 한두 줄 더한다. 달라진 것이 없으면 적지 않는다. 관계의 변화는 양쪽 문서에 짧게 서로 가리키게 쓰고, 긴 설명은 한쪽에만 둔다. 우정·동경·갈등·첫 호감·연애는 원고에 드러난 만큼만 구분해 적는다. 기록은 원고에 쓰인 사실이지 정본 결정이 아니며, 기록에 맞추려고 원고를 바꾸지 않는다.

## 3. 설정·연속성 검수

| 항목 | 내용 |
|---|---|
| 작업 목표 | 지정된 범위에서 사실·인과·연속성의 모순과 이해를 막는 결함을 찾는다 |
| 우선 읽을 문서 | 검수 대상 원고, 그 원고의 회차 플롯·장면 설계, 권별 현행 지시 요약 |
| 필요할 때만 | 대상과 이어지는 앞뒤 회차, 앞 권의 관련 원고, canon·decisions·open-questions의 관련 항목 |
| 허용되는 변경 | 기본은 읽기 전용(Codex 기본 역할). 정정은 사용자가 지시한 항목만, 가장 작은 범위로 |
| 검증 범위 | 지시된 범위만. 바뀌지 않은 범위를 다시 전수 검수하지 않는다 |
| 완료 기준 | 지적마다 등급, 근거(권·화:행), 최소 수정안이 있다. 등급 3·4에는 원고 수정안을 강요하지 않는다 |

- 지적 등급(AGENTS.md §6)
  1. 확실한 사실·인과 모순
  2. 독자의 이해를 실질적으로 방해하는 결함
  3. 의도적 생략과 미확정 — 원고에 설명을 보태라고 권하지 않는다. 필요하면 문서 기록을 권한다
  4. 문체·연출의 취향 — 제안으로만
- '독자가 추론할 수 있는데 적혀 있지 않은 것'은 모순이 아니다. 유보 문장을 더하는 수정안은 등급 1·2의 근거가 있을 때만 낸다.

## 4. 문체·가독성 퇴고

| 항목 | 내용 |
|---|---|
| 작업 목표 | 읽는 흐름, 대사의 자연스러움, 장면의 리듬을 다듬는다. 사실과 인과는 바꾸지 않는다 |
| 우선 읽을 문서 | 대상 원고, [style-guide.md](style-guide.md) §7·§8, 사용자의 통독 의견 |
| 필요할 때만 | [book1-style-review.md](book1-style-review.md) §11, [style-diagnosis.md](style-diagnosis.md), [../research/fantasy-craft-notes.md](../research/fantasy-craft-notes.md) §11-3, 해당 권의 퇴고 기록 |
| 허용되는 변경 | 시리즈 완결 전에는 사용자가 지정한 장면·회차의 국소 퇴고만. 대규모 문체·가독성 퇴고와 구조 재설계는 [series-revision-backlog.md](series-revision-backlog.md)에 이월하고 종합 편집에서 한다 |
| 검증 범위 | 바꾼 장면의 사실·증거·인과가 그대로인지 원문과 대조, 앞뒤 회차 연결, `python3 tools/verify.py` |
| 완료 기준 | 바꾸기 전후 비교와 유지한 사실 목록이 보고에 있다. 승인 전 시범안은 별도 파일로 두고 원고에 반영하지 않는다 |

- 지표(문장 길이, 대사 비율, 용어 밀도)는 막히는 곳을 찾는 데만 쓴다.
- 절제가 효과적인 곳(핵심 장면, 말수 적은 인물, 회차의 첫 문장과 끝 문장)은 그대로 둔다(style-guide §7).
- 퇴고로 사건이나 인물의 선택이 바뀌면 [../characters/](../characters/)의 해당 '변화 이력' 줄도 함께 고친다.

## 5. 정본·이력 관리

| 항목 | 내용 |
|---|---|
| 작업 목표 | 승인된 결정과 원고 상태를 정본 문서에 정확히 남긴다 |
| 우선 읽을 문서 | 사용자 결정 내용, [../canon.md](../canon.md) §1(상태 표기)과 고칠 행, 해당 권의 퇴고 기록 문서 |
| 필요할 때만 | [../decisions.md](../decisions.md)의 관련 결정과 마지막 번호, [../open-questions.md](../open-questions.md)의 관련 질문과 '작업 가정', [series-integration.md](series-integration.md)(브랜치·태그 이력), [../../tools/README.md](../../tools/README.md) |
| 허용되는 변경 | 승인된 내용의 반영, 상태 표기 갱신, 원고 머리 주석의 상태 줄, 퇴고 기록. 새 결정 번호는 사용자가 정할 때만, 마지막 번호 다음 번호로 |
| 검증 범위 | `python3 tools/verify.py`(링크, D·Q 번호, 원고 형식), `git diff --check`, 인용한 커밋 해시 |
| 완료 기준 | 사용자 결정의 근거와 이력이 지워지지 않고 남아 있다. 옛 문구는 지우기보다 [대체됨]·이력 표시로 구분한다 |

- 작업 가정(집필을 위한 임시값)은 canon §1의 규칙대로 정본과 구분해 적는다.
- 원고 머리 주석에는 상태와 근거를 짧게 쓰고, 긴 퇴고 내역은 권별 퇴고 기록 문서에 둔다.
