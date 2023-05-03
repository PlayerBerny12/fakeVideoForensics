"""
DeepfakeDetectionFramework
--------------------------

if any required method is written in python
then import specific module and run the method
directlly otherwise import subprocess module
and run it as subprocess and parse the output

e.g.:
    from my_module import my_func1, my_func2
    my_func1(x, y)
    
    -------------------------
    
    import subprocess
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True) 
    
    print(result.stdout)
"""

from fastapi import FastAPI
from typing import Any

import subprocess
import os
import pathlib

app = FastAPI()

ID = 7

def check_request(file_path: str):
    """
    Check file type if it is processable
    """
    file_extension = pathlib.Path(file_path).suffix
    
    if file_extension == ".mp4" or file_extension == ".avi":
        return True
    else: 
        return False

def data_preparation(file_path: str):
    """
    Prepare data from request
    
    E.g.: convert to specific format (wav, mp3, ...) 
    or split data to frames, etc.
    """
    
    return file_path

def detection_method(file_path: str):
    """
    Run detection method on prepared data    
    """
    process = subprocess.run(
        ["python3", "-u", "main.py", "--output_path", "/tmp", "--fast",
         "--video_path", "/app/obama.mp4"],
        stdout=subprocess.PIPE,
        encoding="utf-8"
    )    
    
    # Remove generated output file
    [ os.remove(f"/tmp/{f}") for f in os.listdir("/tmp") if f.endswith(".avi") ]
    
    try:
        return float((process.stdout.splitlines()[-2]).split()[-1])            
    except:
        return None    
    
def results_normalization(results: Any):
    """
    Normalize data by converting to interval <0-1>
    """
    
    return results / 100

@app.get("/detect")
def detect(id: int, checksum: str, filename: str, status: int, type: int):
    """
    Entry point for receiving requests
    """
    file_path = f"/mnt/processingdata/{filename}"

    if check_request(file_path):        
        # Prepare data from request (optional)
        file_path = data_preparation(file_path)

        # Run detection method
        results = detection_method(file_path)

        # Convert results to interval <0-1> (optional)
        if results:
            results = results_normalization(results)

            return {"RequestID": id, "Value": results, "MethodID": ID}            
        else:
            return None
    else:
        return None