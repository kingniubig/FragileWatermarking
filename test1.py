import cv2
import numpy as np
from tkinter import Tk, filedialog
import io
from flask import Flask, request, render_template_string
from PIL import Image

img = cv2.imread("test.jpg")
# print(img.shape, img.dtype)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(type(gray_img), type(rgb_img))

r, g, b = cv2.split(rgb_img)

merged = cv2.merge([b, g, r])

# 归一化到[0, 1]区间
img_f = img.astype(np.float32) / 255.0

# 仅有红色通道
r_only = img.copy()
r_only[:, :, 0] = 0
r_only[:, :, 1] = 0

cv2.namedWindow("R Channel", cv2.WINDOW_NORMAL)
cv2.imshow("R Channel", r_only)
cv2.waitKey(0)
cv2.destroyAllWindows()

ycrcb = cv2.cvtColor(cv2.imread("test.jpg"), cv2.COLOR_BGR2YCrCb)
y, cr, cb = cv2.split(ycrcb)

cv2.namedWindow("Y image", cv2.WINDOW_NORMAL)
cv2.imshow("Y image", y)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 偏红
y_new = np.full_like(y, 128)
cb_new = np.full_like(cb, 128)

cr_only = cv2.cvtColor(cv2.merge([y_new, cr, cb_new]), cv2.COLOR_YCrCb2RGB)

cv2.namedWindow("Cr image", cv2.WINDOW_NORMAL)
cv2.imshow("Cr image", cr_only)
cv2.waitKey(0)
cv2.destroyAllWindows()

def dct2(block):
    return cv2.dct(block)

def idct2(coef):
    return cv2.idct(coef)

block = gray_img[0:8, 0:8].astype(np.float32)
coef = dct2(block)
back = idct2(coef)

def jpeg_attack(img, qf):
    cv2.imwrite("tmp.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, qf])
    return cv2.imread("tmp.jpg")

root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="选择图片",
    filetypes=[
        ("图片", "*.jpg *.jpeg *.png *.bmp *.gif *.webp"),
        ("所有文件", "*.*")
    ]
)

if file_path:
    img_t = cv2.imread(file_path)
    cv2.namedWindow("Chosen image", cv2.WINDOW_NORMAL)
    cv2.imshow("Chosen image", img_t)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("已取消")