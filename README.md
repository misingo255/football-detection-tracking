# Football Player, Referee, and Ball Detection and Tracking App

This project is a football player, referee, and ball detection and tracking application built using the YOLOv9 model. It utilizes libraries such as Ultralytics, NumPy, OpenCV-Python, and Supervisely for efficient detection and tracking. This README file provides an overview of the application, including how to set it up and use it, along with a preview video demonstrating the final output.

## Features

- **Object Detection**: The app utilizes the YOLOv9 model to detect football players, referees, and the ball in football match videos.
- **Tracking**: After detection, the application tracks the detected objects (players, referees, and ball) across frames to provide continuous monitoring.
- **Real-Time Processing**: The app is capable of processing videos in real-time, making it suitable for live broadcasts or recorded matches.


## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x: You can download and install Python from [python.org](https://www.python.org/).
- Pip: The Python package installer. It usually comes pre-installed with Python. If not, you can install it using your package manager or by downloading get-pip.py from [here](https://bootstrap.pypa.io/get-pip.py).
- Git: Install Git from [git-scm.com](https://git-scm.com/) if not already installed.

## Setup

1. **Clone the Repository**: 
    ```bash
    git clone https://github.com/your-username/football-detection-tracking.git
    ```

2. **Navigate to the Project Directory**:
    ```bash
    cd football-detection-tracking
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Application**:
    ```bash
    python main.py
    ```


2. **View Results**: The application will process the video, detect football players, referees, and the ball, and track them across frames. You can view the processed video along with bounding boxes around the detected objects.

3. **Export Results**: Optionally, you can export the processed video with the detection and tracking results for further analysis or sharing.

## Preview Video

<video width="720" height="300" controls>
  <source src="./media/output_01.mp4" type="video/mp4">
</video>

Click on the preview image above to watch a video demonstrating the final output of the application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to the developers and contributors of the YOLOv9 model, Ultralytics, NumPy, OpenCV-Python, and Supervisely for their invaluable tools and resources that made this project possible.
