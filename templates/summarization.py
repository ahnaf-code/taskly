def build_prompt(task_prompt: str) -> str:
    """
    Wraps the raw summarization task with strict constraints,
    using two-shot prompting to guarantee the model outputs
    a summary within a fixed length constraint.
    """
    system_instruction = (
        "You are an expert text summarization assistant.\n"
        "Summarize the given passage.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- Output ONLY the summary text, nothing else.\n"
        "- Summary must be a maximum of 2 sentences.\n"
        "- Do NOT wrap output in markdown blocks or fences.\n"
        "- Do NOT add any extra commentary outside the summary.\n\n"

        "--- EXAMPLE 1 INPUT ---\n"
        "Text: \"The company reported record revenue this quarter, driven by strong demand for its cloud services. Analysts had expected growth of 8%, but the company posted 15% growth instead. Executives attributed the surge to new enterprise contracts signed in Asia and Europe.\"\n"
        "--- EXAMPLE 1 OUTPUT ---\n"
        "The company posted 15% revenue growth this quarter, beating analyst expectations of 8%. Executives credited new enterprise contracts in Asia and Europe.\n\n"

        "--- EXAMPLE 2 INPUT ---\n"
        "Text: \"A local nonprofit organized a beach cleanup event last weekend. Over 200 volunteers participated, collecting more than 500 pounds of trash. Organizers plan to hold similar events monthly.\"\n"
        "--- EXAMPLE 2 OUTPUT ---\n"
        "Over 200 volunteers collected 500+ pounds of trash at a local nonprofit's beach cleanup. Monthly events are planned going forward.\n"
        "--- END OF EXAMPLES ---\n"
    )

    return f"{system_instruction}\nText:\n{task_prompt}\nOutput:\n"