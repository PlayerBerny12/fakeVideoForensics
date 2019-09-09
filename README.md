# Fake video detector

The tool use the project faceforensics.

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
python3 main.py -i https://www.youtube.com/watch?v=GTh2tRAE2w4

[youtube] GTh2tRAE2w4: Downloading webpage
[youtube] GTh2tRAE2w4: Downloading video info webpage
WARNING: Unable to extract video title
[youtube] GTh2tRAE2w4: Downloading MPD manifest
WARNING: Requested formats are incompatible for merge and will be merged into mkv.
[dashsegments] Total fragments: 7
[download] Destination: video.mp4.f247
[download] 100% of 1.70MiB in 00:01
[dashsegments] Total fragments: 4
[download] Destination: video.mp4.f140
[download] 100% of 460.05KiB in 00:00
[ffmpeg] Merging formats into "video.avi"
Deleting original file video.mp4.f247 (pass -k to keep)
Deleting original file video.mp4.f140 (pass -k to keep)
Starting: video.avi
Model found in ./models/full/xception/full_c23.p
 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 695/695 [01:02<00:00,  9.62it/s]700it [01:09, 10.17it/s]                                                                                                                      
The Fake Score is: 95.71428571428572
Output video in: video.avi
```

# Demo

[<img src="https://img.youtube.com/vi/8YYRT4lzQgY/maxresdefault.jpg" width="100%">](https://youtu.be/8YYRT4lzQgY)


# Credits

* FaceForensics++: Learning to Detect Manipulated Facial Images (https://github.com/ondyari/FaceForensics)
