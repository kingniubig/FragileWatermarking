import cv2
from skimage.metrics import structural_similarity as ssim_fn
from scipy.signal import convolve2d
import numpy as np

# 衡量水印嵌入后的不可感知性
def psnr(a, b):
    a, b = a.astype(np.float64), b.astype(np.float64)
    mse = np.mean((a - b) ** 2)
    return 100.00 if mse == 0 else 10 * np.log10(255**2 / mse)

# 水印不可见性评价（比 PSNR 更符合人眼）
def ssim(a, b):
    if a.ndim == 3: a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    if b.ndim == 3: b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    return ssim_fn(a, b, data_range=255)

# 水印鲁棒性评估：原始水印 vs 攻击后提取的水印 常用于灰度水印、连续值水印
def nc(w1, w2):
    w1 = w1.flatten().astype(np.float64)
    w2 = w2.flatten().astype(np.float64)
    return np.sum(w1 * w2) / np.sqrt(np.sum(w1**2) * np.sum(w2**2))

# 衡量二值水印的比特错误比例，范围 0 ~ 1，越小越好。
def ber(w1, w2):
    w1 = (w1.flatten() > 127).astype(np.int32)
    w2 = (w2.flatten() > 127).astype(np.int32)
    return np.mean(w1 != w2)

# 衡量预测的篡改区域和真实篡改区域的一致程度，范围 0 ~ 1，越大越好。
def tamper_acc(pred_mask, gt_mask):
    return np.mean(pred_mask == gt_mask)