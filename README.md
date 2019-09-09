# Fake video detector

The tool use the project faceforensics.

# Instalation
```
pip install -r requirements.txt
```

# Usage
```
usage: main.py [-h] [--model_path MODEL] [--output_path VIDEOOUT]
               [--start_frame START_FRAME] [--end_frame END_FRAME] [--cuda]
               [--fast] --video_path VIDEOIN

optional arguments:
  -h, --help            show this help message and exit
  --model_path MODEL, -mi MODEL
  --output_path VIDEOOUT, -o VIDEOOUT
  --start_frame START_FRAME
  --end_frame END_FRAME
  --cuda
  --fast

required arguments:
  --video_path VIDEOIN, -i VIDEOIN
```

# Demo

https://youtu.be/8YYRT4lzQgY

# Credits

* FaceForensics++: Learning to Detect Manipulated Facial Images (https://github.com/ondyari/FaceForensics)
