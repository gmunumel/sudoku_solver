
import cv2
import numpy as np


def grid_detection():
  sudoku = cv2.imread('Images/Test/sudoku-original.jpg', 0)

  ##outerBox = cv.CreateMat(sudoku.size(), cv.CV_8UC1)

  outerBox = np.zeros((256, 256, 1), dtype = 'uint8')

  cv2.GaussianBlur(sudoku, (11,11), 0)

  #cv2.adaptiveThreshold(sudoku, outerBox, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)

  outerBox = cv2.adaptiveThreshold(sudoku, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)

  cv2.bitwise_not(outerBox, outerBox)

  #kernel = (Mat_<uchar>(3,3) << 0,1,0,1,1,1,0,1,0)

  kernel = np.ones((3,3), np.uint8)

  cv2.dilate(outerBox, kernel, iterations = 1)

  image_path = 'Images/Results/sudoku-test1.jpg'

  cv2.imwrite(image_path, outerBox)

  cv2.imshow(image_path, outerBox)


def main():
  grid_detection()

  cv2.waitKey(0)

  cv2.destroyAllWindows() 

  #cv2.waitKey(1)

if __name__ == '__main__':
    main()

    