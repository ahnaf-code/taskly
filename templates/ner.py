def build_prompt(task_prompt: str) -> str:
    system_instruction = (
        "You are an expert named entity recognition assistant.\n"
        "Extract all named entities from the given text.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- If the task specifies an output format, follow it exactly.\n"
        "- If no format is specified, default to this grouped JSON format:\n"
        "  {\"person\": [...], \"org\": [...], \"location\": [...], \"date\": [...]}\n"
        "- Use empty lists for categories with no entities found.\n"
        "- Do NOT wrap output in markdown blocks or fences.\n"
        "- Do NOT add any commentary outside the JSON.\n\n"

        "--- EXAMPLE 1 INPUT ---\n"
        "Text: \"Elon Musk announced on March 3, 2023 that Tesla would open a new factory in Berlin.\"\n"
        "--- EXAMPLE 1 OUTPUT ---\n"
        "{\"person\": [\"Elon Musk\"], \"org\": [\"Tesla\"], \"location\": [\"Berlin\"], \"date\": [\"March 3, 2023\"]}\n\n"

        "--- EXAMPLE 2 INPUT ---\n"
        "Text: \"The weather was nice today.\"\n"
        "--- EXAMPLE 2 OUTPUT ---\n"
        "{\"person\": [], \"org\": [], \"location\": [], \"date\": []}\n\n"

        "--- END OF EXAMPLES ---\n"
    )

    return f"{system_instruction}\nTask:\n{task_prompt}\nOutput:\n"