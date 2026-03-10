FROM python:3.11-slim
WORKDIR /app
COPY requiment.txt .
RUN pip install -r requiment.txt
COPY . .
CMD ["python", "app.py"]