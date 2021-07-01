import cv2 as cv
import numpy as np


class Shadow:
    def __init__(self, video_input):
        self.video_input = video_input
        self.image_array = []

    def make_shadow_frames(self, canny_thresh1=100, canny_thresh2=200, binary_thresh1=170, binary_thresh2=225):

        # capturing video frame
        video_capture = cv.VideoCapture(self.video_input)

        # returns false if no more frames in video
        more_frames, curr_frame = video_capture.read()

        # for the purpose of naming frames
        frame_num = 0

        while more_frames:

            # converting image to grayscale for edge detection
            img = cv.cvtColor(curr_frame, cv.COLOR_BGR2GRAY)

            # detecting edges
            # min and max threshold values set to 100 and 200
            cv.Canny(img, canny_thresh1, canny_thresh2)

            # thresholding frame image to get an inverted binary image
            # we only need the threshed image returned by the threshold
            # original threshold: 127, 255
            thresh_used, threshed_img = cv.threshold(img, binary_thresh1, binary_thresh2, cv.THRESH_BINARY_INV)

            # flood filling inside the border area with light gray, value 128
            cv.floodFill(threshed_img, None, (0, 0), 128)

            # Extracting only the filled area
            filled_img = ((threshed_img == 128) * 255).astype(np.uint8)

            # writing frame to frames dir
            self.image_array.append(filled_img)

            # read next frame and update the more frames bool
            more_frames, curr_frame = video_capture.read()

            # update the current frame number
            frame_num += 1

    def frames_to_video(self, output, frame_rate=30, codec='mp4v'):
        height, width = self.image_array[0].shape

        size = (width, height)

        out = cv.VideoWriter(f'{output}', cv.VideoWriter_fourcc(*codec), frame_rate, size, 0)

        for i in range(len(self.image_array)):
            out.write(self.image_array[i])
        out.release()
