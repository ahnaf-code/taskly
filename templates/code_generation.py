def build_prompt(task_prompt: str) -> str:
    """
    Wraps the raw code generation task prompt with strict constraints,
    using two-shot prompting to guarantee the model only outputs
    raw, executable Python code without backticks or explanations.
    """
    system_instruction = (
        "You are an expert code generation assistant.\n"
        "Write a complete, runnable Python function based on the specification.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- Output ONLY raw, executable Python code.\n"
        "- Do NOT wrap code in markdown blocks or fences (e.g., do no use ```python ... ```).\n"
        "- Do NOT provide explanations, docstrings, or conversational text.\n\n"
        
        "--- EXAMPLE 1 INPUT ---\n"
        "Specification: Write a function that multiplies two numbers.\n"
        "--- EXAMPLE 1 OUTPUT ---\n"
        "def multiply(a, b):\n"
        "    return a * b\n\n"
        
        "--- EXAMPLE 2 INPUT ---\n"
        "Specification: Write a function that generates a random integer between 1 and 10.\n"
        "--- EXAMPLE 2 OUTPUT ---\n"
        "import random\n\n"
        "def get_random_num():\n"
        "    return random.randint(1, 10)\n"
        "--- END OF EXAMPLES ---\n"
    )
    
    return f"{system_instruction}\nSpecification:\n{task_prompt}\nOutput:\n"