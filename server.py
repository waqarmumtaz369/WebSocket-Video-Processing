import asyncio
import websockets
import cv2
import base64

async def process_video(websocket, path):
    try:
        print("Client connected.")
        
        # Receive the video file link from the client
        video_link = await websocket.recv()
        if not video_link:
            raise ValueError("Empty video link received")
        print("Received video link:", video_link)

        # Attempt to open the video file for processing
        cap = cv2.VideoCapture(video_link)
        if not cap.isOpened():
            raise IOError("Failed to open video file: " + video_link)
        
        frame_count = 0
        isProcessing = False
        processing_delay = 0.0  # Simulated delay between sending responses (adjust as needed)

        while True:
            # Check if the server is still processing the previous frame
            if isProcessing:
                await asyncio.sleep(processing_delay)
                continue

            # Read a frame from the video
            ret, frame = cap.read()
            if not ret:
                break

            # Set the processing flag to indicate that the server is busy
            isProcessing = True

            frame_count += 1
            print(f"Processing frame {frame_count}...")

            # Convert the frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Encode the frame as base64
            _, frame_data = cv2.imencode('.jpg', gray_frame)
            base64_frame = base64.b64encode(frame_data).decode("utf-8")

            

            # Send the base64-encoded frame to the client
            await websocket.send(base64_frame)

            # Simulate processing delay
            await asyncio.sleep(processing_delay)

            # Reset the processing flag once frame processing is complete
            isProcessing = False

        # Close the video file and connection when finished
        cap.release()
        print("Video processing complete. Closing connection.")
        await websocket.close()

    except websockets.exceptions.ConnectionClosedError:
        print("Client disconnected. Waiting for a new connection...")
    except Exception as e:
        print(f"Error on the server: {str(e)}")

start_server = websockets.serve(process_video, "localhost", 8765)  # Adjust the host and port
print("WebSocket server started.")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
