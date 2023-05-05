FROM python:3.6

WORKDIR /app
ADD dataset/ dataset/
ADD network/ network/
COPY models/face_detection/xception/full_c23.p models/face_detection/xception/full_c23.p
COPY detect_fake_videos.py entrypoint.py main.py requirements.txt xception-b5690688.pth ./

RUN apt update && apt install -y cmake && \
    python3 -m pip install torch==1.0.1.post2 torchvision==0.2.1 --extra-index-url https://download.pytorch.org/whl/cpu --no-cache-dir && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    rm -rf /var/lib/apt/lists/*

CMD [ "uvicorn", "entrypoint:app", "--host", "0.0.0.0", "--port", "50500", "--reload"]