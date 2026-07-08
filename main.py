import json
import os

def main():
    input_path = os.environ.get("TASKS_PATH", "/input/tasks.json")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")

    with open(input_path, "r") as f:
        tasks = json.load(f)

    results = []
    for task in tasks:
        results.append({
            "task_id": task["task_id"],
            "answer": "PLACEHOLDER"
        })

    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "results.json"), "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()