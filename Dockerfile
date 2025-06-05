# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY pyproject.toml ./

# Install the package (editable mode for dev, change as needed)
RUN pip install -e ./

# Final image
FROM base AS final
CMD ["python", "-m", "starter_template"] 