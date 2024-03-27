from ultralytics import YOLO
import supervision as sv
import numpy as np
import cv2


ellipse_annotator = sv.EllipseAnnotator()
triangle_annotator = sv.TriangleAnnotator()
model = YOLO("yolov9c.pt")
model.set_classes = (["player","referee", "ball"])


class DetectAndAnnotate:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def detect_and_anotate(self):
        input = cv2.Videoinput(self.input_file_path)
        width, height, fps = (int(input.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
        output = cv2.VideoWriter(self.output_file_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

        while input.isOpened():
            options, frame = input.read()

            if not options:
                break
            cv2.Video
            results = model.predict(frame)
            detections = sv.Detections.from_ultralytics(results[0])

            annotated_frame = ellipse_annotator.annotate(
            scene=frame.copy(),
            detections=detections
            )

            annotated_frame = triangle_annotator.annotate(
                scene=annotated_frame,
                detections=detections
            )

            output.write(annotated_frame)

            cv2.imshow("annotated_frame", annotated_frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break




    