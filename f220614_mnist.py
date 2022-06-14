import joblib  # model 호출용
import cv2

import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import numpy as np

model = load_model("D:/Kamie/mon_ML/model.h5")

src = cv2.imread("D:/Kamie/dataset/handwrite.png")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
key = cv2.waitKey(0)
if key == 27:
	cv2.destroyAllWindows()

th, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

bin_img = 255 - bin_img

n_blob, label_img, stats, centroids = cv2.connectedComponentsWithStats(bin_img)

show_img = src.copy()

for i in range(1, n_blob):
	x, y, w, h, area = stats[i]
	
	if area > 20:
		cropped_img = gray[y:y+h, x:x+w].copy()
		cropped_img = cv2.resize(cropped_img, (28, 28))
		# plt.imshow(cropped_img, cmap="gray")
		# plt.show()
		cropped_img = 255-cropped_img  # 배경 글자 색상 전환
		
		cropped_img = cropped_img.reshape(1, 28, 28, 1)
		# cropped_img = np.expand_dims(cropped_img, axis=0)
		# cropped_img = np.expand_dims(cropped_img, axis=-1)
		
		pred = model.predict(cropped_img)
		print(pred.argmax())