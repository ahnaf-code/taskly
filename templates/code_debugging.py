def build_prompt(task_prompt: str) -> str:
    """
    Wraps the raw code debugging task prompt with a robust two-shot system-style instruction
    to prevent formatting hallucinations, minimize output tokens, and enforce strict structure.
    """
    system_instruction = (
        "You are an expert code debugging assistant.\n"
        "Analyze the buggy code, explain the bug in exactly one line, and provide the corrected executable code.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- Explain the bug in EXACTLY one line. Do not write more than one line of explanation.\n"
        "- Output ONLY the one-line explanation and the raw, corrected Python code.\n"
        "- Do NOT wrap code in markdown blocks or code fences (e.g., do not use ```python).\n"
        "- Do NOT provide any introductory, concluding, or conversational text.\n\n"
        "--- EXAMPLE 1 INPUT ---\n"
        "Task: This function should return the sum of a and b but has a bug: def sum(a, b): return a - b. Find and fix it.\n"
        "--- EXAMPLE 1 OUTPUT ---\n"
        "Bug: The function uses the subtraction operator (-) instead of the addition operator (+).\n"
        "def sum(a, b):\n"
        "    return a + b\n\n"
        "--- EXAMPLE 2 INPUT ---\n"
        "Task: Fix this bug where appending to a list accumulates across calls: def append_to(element, target=[]): target.append(element); return target\n"
        "--- EXAMPLE 2 OUTPUT ---\n"
        "Bug: The function uses a mutable default argument which persists across multiple function calls.\n"
        "def append_to(element, target=None):\n"
        "    if target is None:\n"
        "        target = []\n"
        "    target.append(element)\n"
        "    return target\n"
        "--- END OF EXAMPLES ---\n"
    )
    
    return f"{system_instruction}\nTask:\n{task_prompt}\nOutput:\n"