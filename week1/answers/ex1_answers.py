"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
The model meta-llama/Llama-3.3-70B-Instruct returned correct answers in all three conditions.
This is common on strong models with clean data.
The plain answer returned 'The Haymarket Vaults' (with capacity exactly 160) which was in the middle of the context. 
The XML and sandwich answer returned 'The Albanach' with 180 capacity which satisfies all constraints but appears first. 
The XML/sandwich methods have an impact on the model such as strong primary bias. 
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is a good candidate for causing a wrong answer because it satisfies both 
capacity and vegan conditions, but it only failse on status. It was placed just before the correct middle pos
answer 'The Haymarket Vaults' as it is hard to discriminate between them
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C was run both Part A and B had correct results.
It shows the disctractions test 'Near-Miss Distractors Added' results for the smaller model meta-llama/Meta-Llama-3.1-8B-Instruct 
Surprisingly, it correctly picked the middle 'The Haymarket Vaults' result but ignored 'The Albanach' completely.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting matters most when comparing outputs across different format such as Plain/XML/Sandwich.
Strong frontier models on short, clean datasets sometimes get all three conditions correct and the 
structural help is not needed. But if we consider Part B with distractions and Part C with the smaller modelrs
then the effect appears. The format matters most when switching to the small 8B model. 
"""
