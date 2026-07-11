import json
import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

from router import classify_task
from templates import TEMPLATE_MAP

CATEGORIES = ["factual_qa", "math_reasoning", "sentiment", "summarization", "ner", "code_debugging", "logic_puzzles", "code_generation"]
CATEGORY_MODEL_MAP = {
    "code_debugging": "kimi-k2p7-code",
    "code_generation": "kimi-k2p7-code",
}

def main():
    input_path = os.environ.get("TASKS_PATH", "/input/tasks.json")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")

    client = OpenAI(
        api_key=os.environ["FIREWORKS_API_KEY"],
        base_url=os.environ["FIREWORKS_BASE_URL"]
    )

    allowed_models = os.environ["ALLOWED_MODELS"].split(",")
    allowed_models = [f"accounts/fireworks/models/{m}" for m in allowed_models]
    model = allowed_models[0]

    with open(input_path, "r") as f:
        tasks = json.load(f)

    results = []
    for task in tasks:
        category = classify_task(task["prompt"])
        build_prompt_fn = TEMPLATE_MAP.get(category, lambda p: p)
        prompt = build_prompt_fn(task["prompt"])
        preferred_model_name = CATEGORY_MODEL_MAP.get(category)
        if preferred_model_name and f"accounts/fireworks/models/{preferred_model_name}" in allowed_models:
            model = f"accounts/fireworks/models/{preferred_model_name}"
        else:
            model = allowed_models[0]

        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            answer = response.choices[0].message.content
            results.append({"task_id": task["task_id"], "answer": answer})
        except Exception as e:
            print(e)
            results.append({"task_id": task["task_id"], "answer": ""})

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "results.json"), "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()