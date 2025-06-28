FROM mcr.microsoft.com/devcontainers/python:3.11

WORKDIR /workspace

COPY backend/requirements.txt /tmp/
COPY backend/requirements-test.txt /tmp/
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    pip install -r /tmp/requirements-test.txt

RUN apt-get update && apt-get install -y git-flow postgresql-client

ENV PYTHONPATH="/workspace/backend:/workspace/backend/app:/workspace/scripts"

USER vscode