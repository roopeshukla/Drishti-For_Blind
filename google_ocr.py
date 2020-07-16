

# Imports the Google Cloud client library
import os
from google.cloud import vision
from gtts import gTTS


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'json file path'
# Instantiates a client
client = vision.ImageAnnotatorClient()

path = r"D:\Drishti-ocr\opencv.png"
list = []
def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.document_text_detection(image=image)

    # Text recognition
    document = response.full_text_annotation
    text = document.text
    Myfile = open("google_ocr.txt", "w")
    list.append(text)

# Putting the recognised text in list
    for element in list:
        Myfile.write(element)
    Myfile.close()
    print("Text file successfully created.")


    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))




