# 1. Base image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements
COPY requirements.txt .

# 5. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy application code
COPY app/ app/
COPY models/ models/

# 7. Expose port
EXPOSE 8200

ENV OTEL_SERVICE_NAME=fraud-api
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector.default.svc.cluster.local:4318
ENV OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf


# 8. Start FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8200"]
