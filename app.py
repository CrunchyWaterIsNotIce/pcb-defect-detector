from flask import Flask, render_template, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# model path
MODEL_PATH = 'weights/runs/yolo11n_pcb_defectsv2/weights/best.pt'

# loading the YOLO model
try:
    model = YOLO(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

def generate_frames():
    """
    Generates video frames with object detection.
    Connects to the default camera (index 0).
    """
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Cannot open camera")
        return

    while True:
        # capture frame-by-frame
        success, frame = camera.read()
        if not success:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        else:
            # --- DETECTION ---
            # run inference on the frame
            results = model(frame, verbose=False) # verbose=False to reduce console output

            # show results on the frame
            annotated_frame = results[0].plot()

            # --- STREAMING ---
            # encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame_bytes = buffer.tobytes()

            # yield the frame in the multipart format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    camera.release()

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Use threaded=True to handle multiple clients, debug=False for production
    app.run(debug=True, threaded=True)