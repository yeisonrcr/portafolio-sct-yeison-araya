FROM python:3.11-slim

# No generar .pyc, logs sin buffer
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar proyecto
COPY . .

# Colectar static (para producción; en dev se sirven directamente)
RUN python manage.py collectstatic --noinput --settings=config.settings.local || true

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001", "--settings=config.settings.local"]
