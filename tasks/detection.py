from ultralytics import YOLO
import supervision as sv
import cv2
import os

system_directory = os.getcwd()
model_path = f"{system_directory}/models/yolov9c.pt"

ellipse_annotator = sv.EllipseAnnotator()
triangle_annotator = sv.TriangleAnnotator()
model = YOLO(model_path)
model.set_classes = (["player","referee", "ball"])


class DetectAndAnnotate:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.cv_width = cv2.CAP_PROP_FRAME_WIDTH
        self.cv_height = cv2.CAP_PROP_FRAME_HEIGHT
        self.cv_fps = cv2.CAP_PROP_FPS


    def detect_and_anotate(self):
        input = cv2.VideoCapture(self.input_file_path)
        width, height, fps = (int(input.get(x)) for x in (self.cv_width, self.cv_height, self.cv_fps))
        output = cv2.VideoWriter(self.output_file_path, cv2.VideoWriter.fourcc(*"mp4v"), fps, (width, height))

        while input.isOpened():
            options, frame = input.read()

            if not options:
                break
            
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




   