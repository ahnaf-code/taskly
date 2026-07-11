def build_prompt(task_prompt: str) -> str:
    """
    Wraps the raw sentiment classification task with strict constraints,
    using two-shot prompting to guarantee the model outputs a label
    and a justification in a fixed, parseable format.
    """
    system_instruction = (
        "You are an expert sentiment analysis assistant.\n"
        "Classify the sentiment as requested (use the exact label options given in the task, if any), then give a justification in exactly one sentence.\n"
        "Output format: <label>. <one-sentence justification>.\n"
        "Do not use markdown formatting. Plain text only.\n\n"

        "--- EXAMPLE 1 INPUT ---\n"
        "Text: \"The service was fast and the staff were incredibly friendly.\"\n"
        "--- EXAMPLE 1 OUTPUT ---\n"
        "positive. The service felt welcoming and efficient because the staff were friendly and the experience was smooth.\n\n"

        "--- EXAMPLE 2 INPUT ---\n"
        "Text: \"I waited an hour and the food arrived cold.\"\n"
        "--- EXAMPLE 2 OUTPUT ---\n"
        "negative. The experience was frustrating because the wait was long and the food was cold.\n"
        "--- END OF EXAMPLES ---\n"
    )

    return f"{system_instruction}\nText:\n{task_prompt}\nOutput:\n"