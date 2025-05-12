FROM python:3.12.7-slim-bookworm

RUN apt-get update
RUN apt-get -y install gcc python3-dev
RUN mkdir -p /app/cache

RUN useradd -m -u 6969 apiuser
RUN chown -R apiuser:apiuser /app/cache
USER apiuser
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
COPY factories/ /app/factories/
COPY seeders/ /app/seeders/
COPY modules/ /app/modules/
COPY *.py /app/
WORKDIR /app

ENV PYTHONPATH=/app
CMD ["/home/apiuser/.local/bin/fastapi", "run", "main.py", "--port", "8080"]