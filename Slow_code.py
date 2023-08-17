import cv2

def slow_down_video(input_video_path, output_video_path, factor=2):
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error opening video file")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps // factor, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        for _ in range(factor):
            out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = r"C:\Users\devir\Desktop\VIT\Sem 3\Extras Sem 3\OutputVideo.mp4"  
    output_video_path = r"C:\Users\devir\Desktop\VIT\Sem 3\Extras Sem 3\RevVideo.mp4"  
    slow_down_video(input_video_path, output_video_path, factor=2) 
