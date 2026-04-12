"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "The Haymarket Vaults"

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Updated The Albanach venue status to full in sovereign_agent/tools/mcp_venue_server.py
search_venues returned only one venue The Haymarket Vaults instead of two initially.
So the result with matches contained only one venue.
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 283   # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 202   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
MCP provides a dynamic and modular approach to tool integration, enabling runtime discovery 
and invocation of tools. This eliminates hardcoding, enhances scalability, and simplifies 
updates without modifying the core agent logic.
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- Placeholde to be FILLed in week 5
- Placeholde to be FILLed in week 5
- Placeholde to be FILLed in week 5
- Placeholde to be FILLed in week 5
- Placeholde to be FILLed in week 5
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
The research agent (LangGraph sovereigh agent) excels in exploratory tasks, 
leveraging tools like search_venues to gather broad data. It is provided with 4 of tools such as
checking pub availability and a local weather, calculating caterings costs and generating event flyer.
The tool set can be extended and the new tool can be picked up automatically. 
The research agent is wired together: the LangGraph loop, the tools and the LLM connection. 
The main idea is that it decides its own sequence of steps, calls tools, handles failures and returns a result.
All these actions are done without human guidance at each turn. 
Basically this is a tool for open-ended problems where the path cannot be predetermined.

For example, all verues have a limit of max 200 guests. So when we tried to search a venue for 300 guests the 
research agent let us know "None of the known venues meet the capacity and dietary requirements. The Albanach, The Haymarket Vaults, and 
The Guilford Arms have a capacity of 180, 160, and 200 respectively, which is less than the required capacity of 300. 
The Bow Bar has a capacity of 80, which is also less than the required capacity, and it is currently full. 
Therefore, none of the known venues can accommodate 300 people with vegan options".

The call agent (Rasa Pro Calm agent), focused on precision, uses get_venue_details for specific queries. 
It hanfles structures interactions with real people. Its behavious is defined as explicit flows with deterministic
business rules enforced in the code. This specific behaviour is for the tool with hig-stakes convo where every decision
must be audiable and constraints/limits can be guruanteed. 

Swapping agents feels wrong because their designs align with distinct goals: exploration versus precision. 
Observations showed mismatched agents struggled with efficiency and relevance.
"""
