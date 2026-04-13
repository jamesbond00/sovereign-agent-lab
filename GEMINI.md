# GEMINI.md

## Project Overview
**Sovereign Agent Lab** is a 5-week course project for AI Performance Engineering at Nebius Academy. The goal is to build and evolve two types of AI agents:
1.  **The Headless Automator (`sovereign_agent/`)**: A LangGraph-based agent that performs autonomous research and acts without human guidance.
2.  **The Digital Employee (`exercise3_rasa/`)**: A Rasa Pro CALM agent that handles structured human interactions with deterministic business rules.

The project uses a shared tool layer via the **Model Context Protocol (MCP)** to allow both agents to share capabilities.

### Technologies
- **Main Stack**: Python 3.14 (managed by `uv`)
- **Rasa Stack**: Python 3.10 (managed by `uv`)
- **Frameworks**: LangGraph, Rasa Pro CALM, LangChain
- **Tooling**: `uv` (package manager), `make` (command runner), `ruff` (linting), `pytest` (testing)
- **APIs**: Nebius (OpenAI-compatible), Rasa Pro License (for Exercise 3)

---

## Building and Running

### Prerequisites
- Install `uv`: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Install `make`: (Pre-installed on Mac/Linux; use `winget install GnuWin32.Make` on Windows)

### Setup
1.  **Environment**: `cp .env.example .env` and add your `NEBIUS_KEY`.
2.  **Main Environment**: `make install` (Installs Python 3.14 and dependencies).
3.  **Rasa Environment**: `make install-rasa` (Requires `RASA_PRO_LICENSE` in `.env`).
4.  **Verify**: `make smoke` to check API connectivity.

### Key Commands
- `make test`: Run unit tests for tools (run this before exercises).
- `make ex1`: Run Exercise 1 (Context Engineering).
- `make ex2`: Run Exercise 2 (LangGraph Research Agent).
- `make ex3-train`: Train the Rasa model.
- `make ex3-actions`: Start Rasa action server (Terminal 1).
- `make ex3-chat`: Chat with Rasa agent (Terminal 2).
- `make ex4`: Run Exercise 4 (MCP Client/Server).
- `make grade`: Run mechanical checks before submission.
- `make lint`: Check code style with `ruff`.
- `make help`: Show all available commands.

---

## Development Conventions

### Project Structure
- `sovereign_agent/`: Core autonomous agent code.
    - `tools/`: Tool implementations (e.g., `venue_tools.py`).
    - `agents/`: Agent logic (e.g., `research_agent.py`).
- `exercise3_rasa/`: Rasa-specific project directory.
    - `data/flows.yml`: CALM conversation flows.
    - `actions/actions.py`: Custom Python actions for Rasa.
- `week1/`: Weekly exercises, benchmarks, and answer templates.
    - `answers/`: **User-editable** answer files (e.g., `ex1_answers.py`).
    - `outputs/`: Auto-generated JSON results from exercises.

### Coding Standards
- **Tooling**: Always use `uv` for package management (`uv add`, `uv sync`). Do not use `pip` directly.
- **Linting**: Follow `ruff` rules. Run `make lint` or `make lint-fix`.
- **Testing**: Add or update tests in `sovereign_agent/tests/`. Run tests via `make test`.
- **Workflows**: 
    - Implement TODOs in `sovereign_agent/tools/venue_tools.py` for Exercise 2.
    - Uncomment cutoff guards in `exercise3_rasa/actions/actions.py` for Exercise 3.
    - Always run `make grade` to ensure all mechanical checks pass before concluding a task.

### Extension Policy
Code written in `sovereign_agent/` and `exercise3_rasa/` is intended to be persistent and will be imported/extended in future weeks. Avoid breaking changes to existing tool interfaces.
