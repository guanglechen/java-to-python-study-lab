# Week 1 Plan: Python Basics for a Java Engineer

## Learning scope

This week only covers Python language basics and standard library usage.

Do not add web frameworks, database code, Redis, or AI SDKs in this stage.

## Learning objectives

1. Understand Python variable binding and object references.
2. Use lists, dictionaries, and comprehensions naturally.
3. Write small functions instead of heavy class wrappers.
4. Use exceptions intentionally instead of defensive boilerplate.
5. Understand how Python packages and imports are organized.

## Local code targets

### Module 1: `basics.py`

- Write simple business-like functions.
- Practice default arguments, loops, branching, and return values.

### Module 2: `collections_demo.py`

- Practice list and dictionary transformations.
- Prefer comprehensions or small loops over verbose object scaffolding.

### Module 3: `exceptions_demo.py`

- Practice custom exceptions and controlled parsing.
- Learn when to raise and when to return a fallback value.

## Execution order

1. Read the implementation files in `src/study_lab/core/`.
2. Read the tests in `tests/unit/`.
3. Run the tests.
4. Modify one function and rerun the tests.
5. Write down what feels different from Java.

## Week 1 checklist

- [ ] Read all Week 1 source files.
- [ ] Read all Week 1 tests.
- [ ] Run the tests successfully.
- [ ] Explain why Python functions are the main building block here.
- [ ] Explain mutable vs immutable behavior with one example.
- [ ] Add at least three migration notes to `docs/java-vs-python-notes.md`.

## Exit criteria

At the end of Week 1, you should be able to explain:

1. Why Python code does not need a class for every behavior.
2. Why package imports are simpler than Java package naming conventions.
3. Why list and dictionary transformations are much more lightweight in Python.
4. Why exceptions should represent invalid states, not normal control flow.