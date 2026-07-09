def build_prompt(task_prompt: str) -> str:
    """
    Wraps the raw NER task with strict constraints,
    using two-shot prompting to guarantee the model outputs
    extracted entities in a fixed, parseable format.
    """
    system_instruction = (
        "You are an expert named entity recognition assistant.\n"
        "Extract and label all named entities in the given text.\n"
        "CRITICAL INSTRUCTIONS:\n"
       "- Output ONLY a valid JSON list, nothing else.\n"
        "- Format: [{\"entity\": <text>, \"type\": <PERSON|ORG|LOCATION|DATE>}]\n"
        "- If no entities are found, output exactly: []\n"
        "- Do NOT wrap output in markdown blocks or fences.\n"
        "- Do NOT add any extra commentary outside the specified format.\n\n"
"--- EXAMPLE 1 INPUT ---\n"
        "Text: \"Elon Musk announced on March 3, 2023 that Tesla would open a new factory in Berlin.\"\n"
        "--- EXAMPLE 1 OUTPUT ---\n"
        "[{\"entity\": \"Elon Musk\", \"type\": \"PERSON\"}, {\"entity\": \"March 3, 2023\", \"type\": \"DATE\"}, {\"entity\": \"Tesla\", \"type\": \"ORG\"}, {\"entity\": \"Berlin\", \"type\": \"LOCATION\"}]\n\n"

        "--- EXAMPLE 2 INPUT ---\n"
        "Text: \"The weather was nice today.\"\n"
        "--- EXAMPLE 2 OUTPUT ---\n"
        "[]\n"
        "--- END OF EXAMPLES ---\n"
    )

    return f"{system_instruction}\nText:\n{task_prompt}\nOutput:\n"