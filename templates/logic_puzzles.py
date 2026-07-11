def build_prompt(task_prompt: str) -> str:
    instruction = (
        "Reason through the puzzle carefully, then output ONLY the final answer (True/False, a name, a number, etc.), with no explanation. Do not use markdown formatting (no bold, no headers, no bullet points). Plain text only."
    )
    return f"{instruction}\n\nPuzzle: {task_prompt}\nAnswer:"
