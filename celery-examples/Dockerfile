# Base image
FROM python:3.10-slim

# Project specific directory
RUN mkdir work

# Need both the files before performing further commands
COPY requirements.txt /work
COPY hello.py /work

# Every subsequent command will work in this directory.
# This allows us to work with relative paths rather than absolute paths
WORKDIR /work

RUN pip install -r requirements.txt

CMD ["tail", "-f"]