# Klipper SDK Project Context

## Overview
This project is dedicated to developing the **Klipper SDK**, a software development kit for the Klipper clipboard manager. It is currently in the **orchestration phase**, driven by **Kicklang** specifications defined in the `docs/` directory.

## Project Structure
The root directory contains placeholder markers for the intended modular architecture:

- **`KLIPPER_SDK_CORE`**: Intended for the core logic, domain models, and base functionality.
- **`KLIPPER_SDK_DEMO`**: Intended for demonstration applications and usage examples.
- **`KLIPPER_SDK_DOCS`**: Intended for documentation sources.
- **`docs/spec/klipper_sdk_orchestration.kl`**: The **Source of Truth**. This Kicklang file defines the project's structural planes, requirements, agentic roles (Lyra, Aurora, Kodax), and temporal phases.

## Technical Standards & Conventions
Future implementation must strictly adhere to the following modern Python standards:

### Technology Stack
- **Language**: Python (Modern, fully typed).
- **Web/API**: **FastAPI** (Async).
- **Data Validation**: **Pydantic v2**.
- **Networking**: **httpx** (Async).
- **CLI/Output**: **rich**.

### Coding Guidelines
- **Modern Idioms**: Use `async/await` and modern Python features. **DO NOT** use legacy libraries like `requests`, `flask`, or `argparse`.
- **Strict Typing**: All code must feature complete type annotations.
- **Architecture**: Follow a modern monorepo-style structure (e.g., `src/api`, `src/cli`, `src/shared`) emphasizing clear separation of concerns, DTOs, and Dependency Injection.

## Development Workflow
The development process is orchestrated via the plans in `docs/spec/klipper_sdk_orchestration.kl`:

1.  **Orchestration**: Agentic roles (defined in `.kl`) such as **Lyra** (Planning), **Aurora** (Design), and **Kodax** (Implementation) guide the workflow.
2.  **Knowledge Management**: `.kl` files are used for blueprints, specifications, and knowledge items.
3.  **Phases**:
    *   *Initial*: Requirements gathering (Current Focus).
    *   *Design*: Architecture & API definition.
    *   *Implementation*: Coding core modules.
    *   *Testing & Documentation*: QA and user guides.
