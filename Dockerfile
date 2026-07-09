FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TASKS_PATH=/input/tasks.json \
    OUTPUT_DIR=/output

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py router.py ./
COPY templates ./templates

CMD ["python", "main.py"]
