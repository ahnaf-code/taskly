import json
import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI

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
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": task["prompt"]}]
        )
        answer = response.choices[0].message.content
        results.append({"task_id": task["task_id"], "answer": answer})

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "results.json"), "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()