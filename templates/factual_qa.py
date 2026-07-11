def build_prompt(task_prompt: str) -> str:
    instruction = (
        "Answer the factual question directly, concisely, with no extra commentary or hedging. Do not use markdown formatting (no bold, no headers, no bullet points). Plain text only."
    )
    return f"{instruction}\n\nQuestion: {task_prompt}\nAnswer:"
