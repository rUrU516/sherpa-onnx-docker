FROM nvidia/cuda:12.8.0-cudnn-devel-ubuntu22.04

RUN apt-get update && apt-get install -y libc-bin && rm -rf /var/lib/apt/lists/*

CMD bash -lc "nvcc --version && echo '---' && ldconfig -p | grep cudnn || true"
