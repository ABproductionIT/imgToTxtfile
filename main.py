import numpy as np
import cv2


cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

cv2.namedWindow("test")

img_counter = 0
#
# while True:
for i in range(30):
    ret, frame = cam.read()
    img_name = "opencv_frame_{}.png".format(img_counter)
    cv2.imwrite(img_name, frame)
# print("{} written!".format(img_name))
# img_counter += 1

cam.release()

cv2.destroyAllWindows()


path = r'C:\Users\AB\Desktop\intelekt'
color_image = cv2.imread(path + "\\opencv_frame_0.png")
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
n_image = np.array(np.true_divide(gray_image, 255.0))
mas = np.array(n_image, dtype=np.float16)
print(mas)
np.savetxt("test.txt", mas, fmt = '%1.5f', delimiter=",")
# f = open("test.txt", "w")
# f.write(str(mas))
# f.close()
