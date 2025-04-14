[![Linting](https://github.com/akshar-raaj/rabbitmq/actions/workflows/lint.yml/badge.svg)](https://github.com/akshar-raaj/rabbitmq/actions/workflows/lint.yml)
[![Tests](https://github.com/akshar-raaj/rabbitmq/actions/workflows/tests.yml/badge.svg)](https://github.com/akshar-raaj/rabbitmq/actions/workflows/tests.yml)
[![Deployment](https://github.com/akshar-raaj/rabbitmq/actions/workflows/delivery.yml/badge.svg)](https://github.com/akshar-raaj/rabbitmq/actions/workflows/delivery.yml)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview

Explored RabbitMQ using Python pika library.

## Examples and Patterns
1. Direct exchange with few consumers.
2. Work queue
3. Publish Subscribe
4. Routing different messages to different queues.

## Exploration

Concepts
- Connection
- Exchange
- Queue
- Bindings and Routing
- Acknowledgement: Automatic and Manual
- Queue Durability and Message Persistence

Learnings
1. Publishers publish to an exchange.
2. Consumers consume from a queue.
3. Multiple queues can be bound to an exchange.
4. Messages must be acknowledged by the consumer.

Data
1. A single publisher was able to publish 5K messages/second.
2. Attempted publishing with 3 concurrent publishers. Was able to achieve throughput of ~ 15K messages/second.
   This translates to ~ **1 million message per minute**.
3. Assuming each message size is 100 bytes. Thus a throughput of 1.5 MB/second (15K/s * 100bytes).
4. A single consumer was able to consume 5K messages/second with automatic acknowledgement.
5. With manual acknowledgements, consumer througput slightly decreases, say 3.5 K/s.
6. Several concurrent consumers can allows RabbitMQ to reach a delivery rate of 10K messages/second.

## Give it a spin

Building the Docker image

    $ docker build -t rabbitmq-producer-consumer .

Running the Docker container, to start the consumer.

    $ docker run --name rabbit-consumer -v .:/app rabbitmq-producer-consumer

Spin a one-off producer to enqueue/publish a message.

    $ docker run --rm --name rabbit-producer -v .:/app rabbitmq-producer-consumer python producer.py

Switch to the consumer terminal, you would notice:

    Received: Hello World


### Modifying the queue

If you want the producer to publish to a different queue, say `hola` queue.

    $ docker run --rm --name rabbit-producer -v .:/app -e QUEUE=hola rabbitmq-producer-consumer python producer.py hola "Hola Mundo"

Then, configure the consumer to consume from this queue as well. Use `-e` switch with `docker run` to override the `QUEUE` environment variable.

    ß$ docker run --name rabbit-consumer -v .:/app -e QUEUE=hola rabbitmq-producer-consumer


## Docker Hub Repository

This setup can be pulled from Docker Hub registry. See https://hub.docker.com/r/raajakshar/rabbitmq

The following sequence of commands will push the build image to the repository raajakshar/rabbitmq

    $ docker build -t raajakshar/rabbitmq-producer-consumer .
    $ docker tag raajakshar/rabbitmq-producer-consumer raajakshar/rabbitmq:2.0
    $ docker push raajakshar/rabbitmq:2.0