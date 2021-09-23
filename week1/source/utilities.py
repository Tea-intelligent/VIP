import cv2
import numpy as np
import os


def gray_convert(img):
    h, w, c = img.shape
    gray_img = np.zeros((h, w, 1), dtype=np.uint8)
    i = 0
    while i < w:
        j = 1
        while j < h:
            gray_img[j, i] = 0.2989*img[j, i, 2]+0.5870*img[j, i, 1]+0.1140*img[j, i, 0]
            j = j+1
        i = i+1
    return gray_img


def video_convert(path, start, step, destination):
    vidcap = cv2.VideoCapture(path)
    vidcap.set(cv2.CAP_PROP_POS_FRAMES, start)
    success, image = vidcap.read()
    count = start
    while success:
        filename = os.path.join(destination, "frame%d.jpg" % count)
        cv2.imwrite(filename, image)     # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += step
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, count)
