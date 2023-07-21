import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Mercury",(100,250),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Venus",(180,170),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Earth",(290,170),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Mars",(390,170),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Jupiter",(530,50),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Saturn",(780,100),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Uranus",(950,130),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"Neptune",(1100,130),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_system(With Name).jpg", img)