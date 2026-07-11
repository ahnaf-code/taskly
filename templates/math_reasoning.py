def build_prompt(task_prompt: str) -> str:
    instruction = (
        "Solve the problem step-by-step internally, but output ONLY the final numeric or symbolic answer, with no work shown. Do not use markdown formatting (no bold, no headers, no bullet points). Plain text only."
    )
    return f"{instruction}\n\nProblem: {task_prompt}\nAnswer:"
