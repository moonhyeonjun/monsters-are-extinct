# Claude Code Instructions

이 프로젝트는 《괴물은 멸종했습니다》 소설 프로젝트다.

모든 작업 전에 [AGENTS.md](AGENTS.md)를 읽고 공통 규칙을 적용한다. 작업 단계별 절차와 읽을 문서는 [docs/plot/workflow-guide.md](docs/plot/workflow-guide.md)를 따른다.

Claude Code의 기본 역할은 장기 문서 처리, 스토리 기획, 원고 집필, 승인된 파일 수정, Git 작업(커밋·push)이다(AGENTS.md §5). Codex는 기본적으로 읽기 전용 검수자다. 사용자가 작업마다 다르게 지시하면 그 지시를 따른다.

기존 설정과 Git 상태를 확인한 뒤 사용자가 요청한 범위에서 작업한다. 작업 기준 브랜치는 `main`이다.

읽기 전용·커밋 금지 지시가 있으면 자동 커밋·push보다 그 지시가 우선한다(AGENTS.md §2·§8).
