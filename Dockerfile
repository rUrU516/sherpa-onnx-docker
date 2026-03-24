FROM registry.cn-hangzhou.aliyuncs.com/serverless_devs/cuda:11.8.0-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=9000

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libc-bin \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY app.py /app/app.py

CMD ["python3", "/app/app.py"]
