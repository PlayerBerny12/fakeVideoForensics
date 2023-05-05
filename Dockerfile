FROM python:3.6

WORKDIR /app
COPY . .

RUN apt update && apt install -y cmake && \
    python3 -m pip install torch==1.0.1.post2 torchvision==0.2.1 --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    rm -rf /var/lib/apt/lists/*

CMD [ "uvicorn", "entrypoint:app", "--host", "0.0.0.0", "--port", "50500", "--reload"]