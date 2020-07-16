import time
import cv2
import google_ocr
import dynamodb

camera_port = 0



def image_capture():

    camera = cv2.VideoCapture(camera_port)
    time.sleep(5)  # After 5sec camera will open
    return_value, image = camera.read()
    cv2.imwrite("D:/Drishti-ocr/opencv.png", image)
    del(camera)
    return image

if __name__ == '__main__':
    image_capture()
    i = 1
    while(i == 1):
        google_ocr.detect_text(path = "D:/Drishti-ocr/opencv.png")
        dynamodb.main("TextImage")
        i = i-1
