"""
shiftPerspective.py
This script will take an image and transform it to a bird's eye view.
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2



def shift_perspective(frame, mode):
    IMG_SIZE = frame.shape[::-1][1:]
    OFFSET = 300

    # Select lane area (assuming 1280x720 image)
    PRES_SRC_PNTS = np.float32([
      (590, 411), # Top-left corner
      (400, 605), # Bottom-left corner
      (960, 605), # Bottom-right corner
      (687, 411) # Top-right corner
    ])

    # Select destination area (size of image doesn't change)
    PRES_DST_PNTS = np.float32([
      [OFFSET, 0],
      [OFFSET, IMG_SIZE[1]],
      [IMG_SIZE[0]-OFFSET, IMG_SIZE[1]],
      [IMG_SIZE[0]-OFFSET, 0]
    ])


    frame_cp = frame.copy()
    M = cv2.getPerspectiveTransform(PRES_SRC_PNTS, PRES_DST_PNTS)
    M_INV = cv2.getPerspectiveTransform(PRES_DST_PNTS, PRES_SRC_PNTS)
    if (mode == 0) :
        warped = cv2.warpPerspective(frame, M, IMG_SIZE, flags=cv2.INTER_LINEAR)
    if (mode == 1) :
        warped = cv2.warpPerspective(frame, M_INV, IMG_SIZE, flags=cv2.INTER_LINEAR)

    return warped


if __name__ == '__main__':
  frame = cv2.imread('./frames/589.png')
