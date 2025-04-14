FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

ENV QUEUE=hello
ENV RABBITMQ_HOST=host.docker.internal

CMD ["python", "-u", "hello-world/consumer.py"]