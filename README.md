# Fake video detector!!!

The tool use the project faceforensics.

# Requirements

```
Python >= 3.5
```

# Installation
```console
pip install -r requirements.txt
```

# Usage
```console
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

# Output
```console
user@host:/app# python3 main.py -i https://www.youtube.com/watch?v=GTh2tRAE2w4 -mi models/full/xception/full_c23.p
[youtube] GTh2tRAE2w4: Downloading webpage
[youtube] GTh2tRAE2w4: Downloading video info webpage
WARNING: Unable to extract video title
[youtube] GTh2tRAE2w4: Downloading MPD manifest
[download] video.mp4 has already been downloaded
[download] 100% of 1.75MiB
video.mp4
Starting: video.mp4
Model found in models/full/xception/full_c23.p
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 694/694 [09:57<00:00,  1.35it/s]
The Fake Score is: 90.05763688760807%
Output video in: video.avi
```

# Demo

[<img src="https://img.youtube.com/vi/8YYRT4lzQgY/maxresdefault.jpg" width="100%">](https://youtu.be/8YYRT4lzQgY)


# Credits

* FaceForensics++: Learning to Detect Manipulated Facial Images (https://github.com/ondyari/FaceForensics)
