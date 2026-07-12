def build_prompt(task_prompt: str) -> str:
    instruction = (
        "You are a precise mathematical reasoning assistant.\n"
        "Solve the problem by showing your calculation steps clearly, then state the final answer on the last line.\n"
        "CRITICAL INSTRUCTIONS:\n"
        "- Show each calculation step on a new line.\n"
        "- Do not skip steps or approximate intermediate values.\n"
        "- State the final answer clearly on the last line.\n"
        "- Do not use markdown formatting, bold, or headers.\n"
        "- Plain text only.\n\n"

        "--- EXAMPLE ---\n"
        "Problem: A store sells a laptop for $850 after a 15% discount. What was the original price?\n"
        "Step 1: After discount means price = original x (1 - 0.15) = original x 0.85\n"
        "Step 2: original = 850 / 0.85 = 1000\n"
        "Final Answer: $1000\n"
        "--- END EXAMPLE ---\n"
    )
    return f"{instruction}\nProblem: {task_prompt}\nSolution:\n"