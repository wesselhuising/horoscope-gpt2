# syntax=docker/dockerfile:1

FROM python:3.7-slim

RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir \
    flask \
    requests \
    gunicorn \
    flask-talisman

WORKDIR /app

COPY ./app .

EXPOSE 5000

CMD ["python3", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--certfile", "/etc/letsencrypt/live/horoscope.wesselhuising.nl/fullchain.pem", "--keyfile", "/etc/letsencrypt/live/horoscope.wesselhuising.nl/privkey.pem", "app:app", "--timeout", "120"]