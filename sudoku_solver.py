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

result = cv2.warpPerspective(noise_canceled,transform_matrix,(height,width))
cv2.imshow("result",result) 
cv2.waitKey()

boxes=[]
rows = np.vsplit(result,9)
for row_index,row in enumerate(rows):
    boxes.append([])
    cols = np.hsplit(row,9)
    for col_index,col in enumerate(cols):
        cv2.imshow("box",col[5:-5,5:-5])
        cv2.waitKey()
        boxes[row_index].append(col[5:-5,5:-5])



import easyocr
reader = easyocr.Reader(['ch_sim','en'])

digits = []
for i in range(len(boxes)):
    digits.append([])
    for j in range(len(boxes[0])):
        result =reader.readtext(np.asarray(boxes[i][j],dtype=np.uint8))
        digits[i].append(result)
        print(result)

# result =reader.readtext(np.asarray(result,dtype=np.uint8))
# for i in result:
#     print(i)

d = [[int(y[0][-2]) if len(y)>0 else 0 for y in x] for x in digits]

from back_track_solver import Table

t = Table(d)
print(t)
