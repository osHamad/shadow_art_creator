import cv2 as cv
import numpy as np
import shutil
import os


def to_video():
    img_array = []
    for num in range(910):
        img = cv.imread(f'frames/frame_{num}.png')

        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    out = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc(*'DIVX'), 30, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()



def main():
    # removing frame dir is exist
    try:
        shutil.rmtree('frames')

    except:
        pass

    # making the new frame dir
    os.mkdir('frames')

    # capturing video frame
    video_capture = cv.VideoCapture('video6.mp4')

    # returns false if no more frames in video
    more_frames, curr_frame = video_capture.read()

    # for the purpose of naming frames
    frame_num = 0

    while more_frames:

        # converting image to grayscale for edge detection
        img = cv.cvtColor(curr_frame, cv.COLOR_BGR2GRAY)
        for i in img[0]:
            i = 255

        # detecting edges
        # min and max threshold values set to 100 and 200
        cv.Canny(img, 100, 200)

        # thresholding frame image to get an inverted binary image
        # we only need the threshed image returned by the threshold
        # original threshold: 127, 255
        thresh_used, threshed_img = cv.threshold(img, 200, 225, cv.THRESH_BINARY_INV)

        # flood filling inside the border area with light gray, value 128
        cv.floodFill(threshed_img, None, (0, 0), 128)

        # Extracting only the filled area
        filled_img = ((threshed_img == 128) * 255).astype(np.uint8)

        # writing frame to frames dir
        cv.imwrite(f'frames/frame_{frame_num}.png', filled_img)

        # read next frame and update the more frames bool
        more_frames, curr_frame = video_capture.read()

        # update the current frame number
        frame_num += 1

    to_video()



if __name__ == '__main__':
    main()
