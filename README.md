[![Linting](https://github.com/akshar-raaj/rabbitmq/actions/workflows/lint.yml/badge.svg)](https://github.com/akshar-raaj/rabbitmq/actions/workflows/lint.yml)
[![Tests](https://github.com/akshar-raaj/rabbitmq/actions/workflows/tests.yml/badge.svg)](https://github.com/akshar-raaj/rabbitmq/actions/workflows/tests.yml)

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
- Acknowledgement
- Durability and Persistence

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
