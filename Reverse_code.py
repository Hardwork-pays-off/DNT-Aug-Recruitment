import cv2

def reverse_slow_motion(input_video_path, output_video_path):
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change the codec to 'mp4v'
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    for frame in reversed(frames):
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = r"C:\Users\devir\Desktop\VIT\Sem 3\Extras Sem 3\SampleVideo.mp4"
    output_video_path = r"C:\Users\devir\Desktop\VIT\Sem 3\Extras Sem 3\OutputVideo.mp4"

    reverse_slow_motion(input_video_path, output_video_path)
