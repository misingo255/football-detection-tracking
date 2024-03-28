import os
from tasks.detection import DetectAndAnnotate
from tasks.tracking import TrackAndAnnotate

system_directory = os.getcwd()
input_file_path = f"{system_directory}/media/input_01.mp4"
output_file_path = f"{system_directory}/media/output_01.mp4"


def run():
    process = TrackAndAnnotate(input_file_path=input_file_path, output_file_path=output_file_path)
    process.track_and_anotate()




run()
