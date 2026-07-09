def build_prompt(task_prompt: str) -> str:
    instruction = (
        "Answer the factual question directly, concisely, with no extra commentary or hedging."
    )
    return f"{instruction}\n\nQuestion: {task_prompt}\nAnswer:"
