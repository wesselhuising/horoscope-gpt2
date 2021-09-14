# syntax=docker/dockerfile:1

FROM python:3.7

RUN python3 -m pip install fastapi uvicorn
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir \
    torch \
    transformers 

EXPOSE 5001

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001", "--log-level", "debug"]