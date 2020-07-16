import os
import cv2
import time
import dynamodb


camera_port = 0

def image_capture():

    camera = cv2.VideoCapture(camera_port)
    time.sleep(5)  # After 5sec camera will open
    return_value, image = camera.read()
    cv2.imwrite("D:\Drishti-ocr\Drishti.png", image)
    del(camera)
    return image




if __name__ == '__main__':
    image_capture()
    i = 1
    while (i == 1):
        os.system("ms_visionapi.py")
        dynamodb.main("SceneImage")
        i = i - 1

