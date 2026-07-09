def build_prompt(task_prompt: str) -> str:
    instruction = (
        "Reason through the puzzle carefully, then output ONLY the final answer (True/False, a name, a number, etc.), with no explanation."
    )
    return f"{instruction}\n\nPuzzle: {task_prompt}\nAnswer:"
