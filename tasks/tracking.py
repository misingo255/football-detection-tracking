from ultralytics import YOLO
import supervision as sv
import numpy as np


ellipse_annotator = sv.EllipseAnnotator()
tracker = sv.ByteTrack()
model = YOLO("yolov9c.pt")
model.set_classes = (["player","referee", "ball"])

class TrackAndAnnotate:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def callback(self, frame: np.ndarray, _: int) -> np.ndarray:
        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        detections = tracker.update_with_detections(detections)
        return ellipse_annotator.annotate(frame.copy(), detections=detections)

    def track_and_anotate(self):
        sv.process_video(
        source_path=self.input_file_path,
        target_path=self.output_file_path,
        callback=self.callback
        )




    