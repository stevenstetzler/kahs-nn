import cv2
import numpy as np
import urllib.request


# Captures video from the webcam
def capture_video(apply_func=None, *args, **kwargs):
    cap = cv2.VideoCapture(0)
    while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if apply_func is not None:
                display_frame = apply_func(frame, *args, **kwargs)
            else:
                display_frame = frame
                
            # Display the resulting frame
            cv2.imshow('frame', display_frame)
            # When everything done, release the capture
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    cap.release()
    cv2.destroyAllWindows()


host="192.168.0.100:8080"
# Captures video from a webcam at the IP address specified by host
def capture_video_phone(apply_func=None, *args, **kwargs):
    hoststr = 'http://' + host + '/video?x.mjpeg'

    img_bytes = bytes()
    i = 0
    stream = urllib.request.urlopen(hoststr)

    while True:
        img_bytes += stream.read(1024)
        a = img_bytes.find(b'\xff\xd8')
        b = img_bytes.find(b'\xff\xd9')
 
        if a != -1 and b != -1:
            jpg = img_bytes[a:b + 2]
            img_bytes = img_bytes[b + 2:]
            
            frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

            if apply_func is not None:
                display_frame = apply_func(frame, *args, **kwargs)
            else:
                display_frame = frame
                
            # Display the resulting frame
            cv2.imshow('frame', display_frame)
            prev_frame = display_frame
            # When everything done, release the capture
            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    cv2.destroyAllWindows()


def gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def sobel_vertical(img):
    return cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)


def sobel_horizontal(img):
    return cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)


def sobel_both(img):
    return cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=5)


def edges(img):
    return cv2.Canny(img, 100, 150)


face_detector_harr = cv2.CascadeClassifier("detectors/haarcascade_frontalface_default.xml")
def faces_harr(img, detector, scale_factor=1.05, min_neighbors=5):
    faces = detector.detectMultiScale(img, scale_factor, min_neighbors)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img


face_detector_lbp = cv2.CascadeClassifier("detectors/lbpcascade_frontalface.xml")
def faces_lbp(img, detector, scale_factor=1.05, min_neighbors=5):
    faces = detector.detectMultiScale(img, scale_factor, min_neighbors)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img


def main():
    # Video demonstrations
    capture_video()
    capture_video(gray)
    capture_video(sobel_vertical)
    capture_video(sobel_horizontal)
    capture_video(sobel_both)
    capture_video(edges)
    capture_video(faces_harr, face_detector_harr, scale_factor=1.50)
    capture_video(faces_lbp, face_detector_lbp)

    # Phone demonstrations
    capture_video_phone(edges)
    capture_video_phone(faces_lbp, face_detector_lbp, scale_factor=1.50)


if __name__ == "__main__":
    main()
