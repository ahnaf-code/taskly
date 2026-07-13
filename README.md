# Taskly Agent

Taskly is an intelligent routing AI agent built for Track 1 of the AMD Developer Hackathon. It classifies incoming natural language tasks into 8 capability domains (math reasoning, code generation, sentiment analysis, etc.) using a zero-cost, keyword-based classifier, then routes each task to a category-tuned prompt template and the most suitable Fireworks AI model from the competition's allowed model set — optimizing for both accuracy and token efficiency.

## Environment Setup

The application requires specific environment variables to interact with the Fireworks API. Create a `.env` file in the root directory of the project and add the following keys:

```env
# Fireworks API key 
FIREWORKS_API_KEY=your_api_key_here

# Base URL for all Fireworks API calls
FIREWORKS_BASE_URL=https://api.fireworks.ai/inference/v1

# Comma-separated list of permitted models
ALLOWED_MODELS=model-id-1,model-id-2

```

*Note: For the official evaluation harness, do not bundle the `.env` file in your Docker image. The evaluation environment injects these variables dynamically at runtime.*

## Input / Output Structure

Whether running via Python or Docker, the agent expects the following file structure:

* **Input:** Tasks must be provided in a JSON array located at `input/tasks.json`.
* **Output:** The agent will generate its answers and save them to `output/results.json`.

## How to Run Locally (Python)

To run the routing logic directly on a host machine without containerization:

1. **Install dependencies:**
```bash
pip install -r requirements.txt

```


2. **Run the agent:**
```bash
python main.py

```



## How to Run via Docker (Build Local)

To test the containerized version locally and view the generated output:

1. **Build the image:**
```bash
docker build -t taskly:test .

```

Note: if building on Apple Silicon (M1/M2/M3/M4), the evaluation harness requires linux/amd64. Use: docker buildx build --platform linux/amd64 -t taskly:test .


2. **Run the container:**
```bash
docker run --rm --env-file .env -v $(pwd)/input:/input -v $(pwd)/output:/output taskly:test

```


3. **View the results:**
```bash
cat output/results.json

```



## How to Run via Docker (GitHub Container Registry)

To run the pre-built image directly from the public GitHub Container Registry:

1. **Pull the image:**
```bash
docker pull ghcr.io/ahnaf-code/taskly:latest

```


2. **Run the container:**
```bash
docker run --rm --env-file .env -v $(pwd)/input:/input -v $(pwd)/output:/output ghcr.io/ahnaf-code/taskly:latest

```
