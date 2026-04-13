# Changelog

## [Week 1 Fixes & Improvements] - 2026-04-13

### Agent & Tooling
- **Fixed Tool-Calling Format**: Added a system prompt to `sovereign_agent/agents/research_agent.py` to enforce standard tool-calling schema. This prevents the Llama model from returning non-standard JSON lists in the message content, which was causing execution failures in LangGraph.
- **Improved Tool Call Parsing**: Updated `run_research_agent` to robustly handle both standard `tool_calls` attributes and custom JSON-in-content formats. This ensures tool execution and results are correctly captured in the trace even when models vary their output style.
- **Bug Fix in Grader**: Patched `week1/grade.py` to fix a `TypeError`. The grader was calling `generate_event_flyer` with an incorrect keyword argument (`pub_name`); it now correctly uses `venue_name`.

### Documentation & Context
- **Created GEMINI.md**: Generated a comprehensive project guide including architecture overview, setup instructions, key commands, and development conventions.
- **Updated Progress & Strategy**: Verified all Exercise 2 tasks (A, B, C) are now successfully populating `ex2_results.json` with complete traces and final answers.

### Verification
- **Passed Mechanical Checks**: Verified that all 65 checks in `make grade` pass successfully.
- **Unit Tests**: Confirmed all 15 tool unit tests in `pytest` are passing.
