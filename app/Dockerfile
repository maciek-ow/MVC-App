FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y gcc python3-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --upgrade pip

COPY app.py requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY python_files/ /app/python_files
COPY templates/ /app/templates

ENV FLASK_APP=/app/app.py
ENV FLASK_TEMPLATES_FOLDER=/app/templates

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]