# Single-Repo Python Training Plan

## Goal

Use this repository as one continuous training project for the transition from Java engineering to Python backend and AI application engineering.

## Principles

1. Learn by coding, not by collecting notes.
2. Keep one repository and let it evolve by phase.
3. Separate language learning, engineering setup, backend development, and AI orchestration by layer.
4. End each week with code, tests, and written conclusions.

## Phase roadmap

### Phase 1: Repository skeleton and learning rules

- Create the main package, tests, docs, scripts, and examples directories.
- Keep all future work inside one repository.
- Use docs to record migration notes and weekly progress.

### Phase 2: Python language migration

- Focus on language and standard library only.
- Learn functions, collections, exceptions, modules, data classes, generators, decorators, and async basics.
- Write tests for every learning module.

### Phase 3: Engineering tooling

- Add `pyproject.toml`, dependency management, linting, testing, type checking, pre-commit, and logging conventions.
- Make the repository feel like a real project.

### Phase 4: FastAPI backend

- Add API routes, request and response models, dependency wiring, and integration tests.

### Phase 5: Database and cache

- Add SQLAlchemy, Alembic, Redis, and configuration layering.

### Phase 6: Model integration and RAG

- Add LLM client wrappers, embedding flows, chunking, retrieval, and minimal evaluation.

### Phase 7: Graph database and knowledge graph

- Add graph modeling, graph queries, and graph-enhanced retrieval experiments.

### Phase 8: Agent workflow orchestration

- Add tools, state, workflows, and end-to-end orchestration.

## Weekly sequence

1. Week 1: Python basics in `src/study_lab/core`
2. Week 2: Pythonic patterns and type hints
3. Week 3: Project tooling
4. Week 4: FastAPI basics
5. Week 5: Database and cache
6. Week 6: Model services and RAG
7. Week 7: Graph work
8. Week 8: Agent orchestration

## Repository guardrails

- Formal code belongs in `src/` and `tests/`.
- Docs explain decisions; docs do not replace code.
- AI frameworks must not define the top-level structure.
- Each new layer should depend on a smaller number of lower layers.