import time
import sys
import os
import cv2
import numpy as np
import tensorflow.keras as keras
from PIL import Image, ImageOps

# window setting
CAMERA_ID = 0
WIDTH = 640
HEIGHT = 480
FPS = 10
WINDOW_NAME = 'key_hook'
EMPTY_COLOR = (0,0,255)
NOMAL_COLOR = (255,0,0)

# message
EMPTY_MESSAGE = 'Out currently.'
NOMAL_MESSAGE = 'At home.'

# comvert cv to pil
def cv2pil(image_cv):
    image_cv = cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_cv)
    image_pil = image_pil.convert('RGB')

    return image_pil

# display message
def display_message(img, color, message):

    img_height, img_width = img.shape[:2]
    cv2.rectangle(img, (0, 0), (img_width, 10), color, -1)
    cv2.rectangle(img, (0, img_height - 10), (img_width, img_height), color, -1)
    cv2.putText(img, message, (10, img_height - 15),
               cv2.FONT_HERSHEY_PLAIN, 2,
               color, 2, cv2.LINE_AA)
    return img

# main process
def main():

    np.set_printoptions(suppress=True)

    Input_Array = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    cap_video = cv2.VideoCapture(CAMERA_ID)
    cap_video.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap_video.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap_video.set(cv2.CAP_PROP_FPS, FPS)

    if not cap_video.isOpened():
        return

    model = keras.models.load_model('./model/keras_model.h5')

    while True:
        ret, frame = cap_video.read()
        if(frame is None):
            continue

        size = (224, 224)
        image = ImageOps.fit(cv2pil(frame), size, Image.ANTIALIAS)
        image_array = np.array(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        Input_Array[0] = normalized_image_array
        
        predictions = model.predict(Input_Array)
        if np.argmax(predictions[0]) == 0:
            frame = display_message(frame, EMPTY_COLOR, EMPTY_MESSAGE)
        else:
            frame = display_message(frame, NOMAL_COLOR, NOMAL_MESSAGE)

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap_video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

