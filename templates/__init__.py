from . import factual_qa, math_reasoning, logic_puzzles, code_debugging, code_generation, sentiment, summarization, ner

TEMPLATE_MAP = {
    "factual_qa": factual_qa.build_prompt,
    "math_reasoning": math_reasoning.build_prompt,
    "logic_puzzles": logic_puzzles.build_prompt,
    "code_debugging": code_debugging.build_prompt,
    "code_generation": code_generation.build_prompt,
    "sentiment": sentiment.build_prompt,
    "summarization": summarization.build_prompt,
    "ner": ner.build_prompt,
}
