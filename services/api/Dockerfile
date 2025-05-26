FROM python:3.12-slim

WORKDIR /app

# Install poetry-core so pip can process pyproject files
RUN pip install --no-cache-dir poetry-core

# Copy Python package and install it
COPY wealth/pyproject.toml wealth/poetry.toml /app/wealth/
COPY wealth/wealth /app/wealth/wealth
RUN pip install --no-cache-dir ./wealth

# Copy API service code
COPY services/api /app/services/api

EXPOSE 8000
CMD ["uvicorn", "services.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
