import cv2
import numpy as np
import imutils

input_file_address = "sample_sudoku.jpg"

sudoku = cv2.imread(input_file_address)
cv2.imshow("input picture",sudoku)
cv2.waitKey()


# finding board
gray = cv2.cvtColor(sudoku,cv2.COLOR_BGR2GRAY)
noise_canceled = cv2.bilateralFilter(gray,13,20,20)
cv2.imshow("noise canceled",noise_canceled)
cv2.waitKey()
edge= cv2.Canny(noise_canceled,30,180)
cv2.imshow("edge",edge)
cv2.waitKey()
key_points = cv2.findContours(edge.copy(),cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)


contours = imutils.grab_contours(key_points)

newimg = cv2.drawContours(sudoku.copy(), contours, -1, (0, 255, 0), 3)
cv2.imshow("contours",newimg)
cv2.waitKey()


contours = sorted(contours,key=cv2.contourArea,reverse=True)[:15]

for contour in contours:
    approx = cv2.approxPolyDP(contour,15,True)
    if len(approx)==4:
        location = approx
        break


corners = cv2.drawContours(sudoku.copy(), location, -1, (0, 0, 255), 10)
cv2.imshow("for corners of sudoku",corners)
cv2.waitKey()

height,width = gray.shape
height,width = height-height%9,width-width%9
src = np.float32(location)
dst = np.float32([[height,0],[0,0],[0,width],[height,width]  ])

transform_matrix = cv2.getPerspectiveTransform(src,dst)
result = cv2.warpPerspective(sudoku,transform_matrix,(height,width))

cv2.imshow("result",result) 
cv2.waitKey()


boxes=[]
rows = np.hsplit(result,9)
for row_index,row in enumerate(rows):
    boxes.append([])
    cols = np.vsplit(row,9)
    for col_index,col in enumerate(cols):
        cv2.imshow("box",col)
        cv2.waitKey()
        boxes[row_index].append(col)




