import os
import cv2
import glob
import re

from constants import *

# Sorting function for numerical sorting
def numerical_sort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def zoom_in(files, width, height):
    # Define the codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'{OUTPUT_PATH}/{OUTPUT_ZOOM_IN_FN}', fourcc, 30.0, (width, height))

    frames = []
    for i, filename in enumerate(files):
        img = cv2.imread(filename)

        # If it's the last image, just write it to the video
        if i == len(files) - 1:
            frames.append(img)
        else:
            # Calculate zoom factor for each step
            zoom_factor = ZOOM_LEVEL ** (1 / BASE_FRAMES)

            # Create a transition where the image is gradually zoomed
            for j in range(BASE_FRAMES):
                zoom = zoom_factor ** j
                zoomed_img = cv2.resize(img, None, fx=zoom, fy=zoom, interpolation = cv2.INTER_LINEAR)

                # Crop the zoomed image to original size focused at center
                start_row, start_col = int((zoomed_img.shape[0] - height) / 2), int((zoomed_img.shape[1] - width) / 2)
                cropped_zoomed_img = zoomed_img[start_row:start_row+height, start_col:start_col+width]

                frames.append(cropped_zoomed_img)

    for frame in frames:
        out.write(frame)

    # Release the VideoWriter
    out.release()

    return frames


def reverse_video(frames, width, height):
    # Define the codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(f'{OUTPUT_PATH}/{OUTPUT_ZOOM_OUT_FN}', fourcc, 30.0, (width, height))

    for frame in reversed(frames):
        out.write(frame)

    # Release the VideoWriter
    out.release()


def create_videos(do_reverse=DO_REVERSE):
    # Get a list of all the image files in ascending order
    files = sorted(glob.glob(os.path.join(INPUT_PATH, '*.png')) + glob.glob(os.path.join(INPUT_PATH, '*.jpg')), key=numerical_sort)

    # Define the dimensions using the first image
    first_img = cv2.imread(files[0])
    height, width, _ = first_img.shape

    # Zoom in from "max" to 1 and get frames
    frames = zoom_in(files[::-1], width, height)

    # Create zoom out video by reversing frames
    if do_reverse:
        reverse_video(frames, width, height)


def create_folders(*args):
    for folder in args:
        if not os.path.exists(folder):
            os.makedirs(folder)


if __name__ == "__main__":
    create_folders(OUTPUT_PATH)
    create_videos()