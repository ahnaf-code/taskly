def build_prompt(task_prompt: str) -> str:
    """
    Wraps the raw sentiment classification task with strict constraints,
    using two-shot prompting to guarantee the model outputs a label
    and a justification in a fixed, parseable format.
    """
    system_instruction = (
        "You are an expert sentiment analysis assistant.\n"
        "Classify the sentiment of the given text and justify your classification.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- Output ONLY a single sentiment label, nothing else.\n"
        "- Label must be exactly one of: positive, negative, neutral.\n"
        "- Do NOT include justification or any other text.\n"
        "- Do NOT add any extra commentary outside the specified format.\n\n"

        "--- EXAMPLE 1 INPUT ---\n"
        "Text: \"The service was fast and the staff were incredibly friendly.\"\n"
        "--- EXAMPLE 1 OUTPUT ---\n"
        "positive\n\n"

        "--- EXAMPLE 2 INPUT ---\n"
        "Text: \"I waited an hour and the food arrived cold.\"\n"
        "--- EXAMPLE 2 OUTPUT ---\n"
        "negative\n"
        "--- END OF EXAMPLES ---\n"
    )

    return f"{system_instruction}\nText:\n{task_prompt}\nOutput:\n"