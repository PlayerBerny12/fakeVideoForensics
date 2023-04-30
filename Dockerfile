FROM python:3.6

RUN apt update && apt upgrade -y && apt install -y cmake && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .

RUN python3 -m pip install -r requirements.txt --no-cache-dir  

CMD [ "uvicorn", "entrypoint:app", "--host", "0.0.0.0", "--port", "50500", "--reload"]