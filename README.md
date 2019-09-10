# FakeVideoForensics!!!

FakeVideoForensics is an ambicious open-source tool that allows to detect fake videos using the best algorithms and released tools. 
Our tool is useful for OSINT researchers, threat intelligent's analysts and for design best procedures about authentication and identification of people/users, specially in the security behaviour area.

Currently, our tool can detect fake faces from urls (videos from youtube) and video files that use FaceSwap, Face2Face or DeepFakes as algorithm to create fake content. We use the advanced researches in this topic to get this target. For example, we use an evolution of the research FaceForensics++

[Sources]
- https://github.com/MarekKowalski/FaceSwap
- https://github.com/datitran/face2face-demo
- https://github.com/deepfakes/faceswap
- FaceForensics++: Learning to Detect Manipulated Facial Images - Andreas Rössler, Davide Cozzolino, Luisa Verdoliva, Christian Riess, Justus Thies, Matthias Nießner. https://arxiv.org/abs/1901.08971

[Authors]
Dr. Alfonso Muñoz (@mindcrypt), Miguel Hernández (@miguelhzbz), Jose Ignacio Escribano Pablos (github-@jyep)



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
