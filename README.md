# Real-Time Video Processing with WebSockets

This repository contains a Python-based solution for real-time video processing using WebSockets. It enables you to stream video from an RTSP source or a video file, process each frame on the server, and display the processed frames on the client side using OpenCV. The system is designed to automatically reconnect if the connection is lost.

## Features

- **WebSocket-based API:** The code uses WebSockets to establish communication between the server and client, allowing real-time video streaming and processing.

- **Easy Setup:** Simply run the server and client scripts to start processing video frames. You can easily replace the RTSP link with your own source.

- **Customizable Image Processing:** The server processes video frames frame by frame, allowing you to implement various image processing techniques. In the provided code, frames are converted to grayscale, but you can customize this to fit your needs.

## Getting Started

### Installation

1. Activate your Python environment (if you have one).
2. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   
### How to Run

1. Replace the RTSP link in client.py with your own RTSP link.
2. Run the server script:
`python server.py`
3. Run the client script:
`python client.py`
|Note: The sample RTSP link provided in client.py is borrowed from rtsp.stream. You can obtain a |free RTSP link with a unique key after signing up and test this code.


### Code Explanation
The code consists of two main scripts:

* `server.py`: This script runs the server that receives the video link from the client, processes each frame, and sends the processed frames back to the client.

* `client.py`: This script connects to the server, sends the video link to the server, receives the processed frames, and displays them using OpenCV.

Feel free to explore and modify the code to suit your specific video processing requirements.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
