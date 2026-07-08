def build_prompt(task_prompt: str) -> str:
    """
    Uses few-shot prompting to enforce a strict one-line explanation 
    followed by raw code, eliminating all markdown and filler.
    """
    system_instruction = (
        "You are an expert code debugging assistant.\n"
        "Analyze the code, identify the bug in exactly one line, and provide the corrected executable code.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- Do NOT wrap code in markdown blocks or fences (e.g., no ```python).\n"
        "- Do NOT provide any conversational text, intro, or outro.\n\n"
        "--- EXAMPLE INPUT ---\n"
        "Task: Fix this bug: def add(a, b): return a - b\n"
        "--- EXAMPLE OUTPUT ---\n"
        "Bug: The function subtracts 'b' from 'a' instead of adding them.\n"
        "def add(a, b):\n"
        "    return a + b\n"
        "--- END OF EXAMPLE ---\n"
    )
    
    return f"{system_instruction}\nTask:\n{task_prompt}\nOutput:\n"