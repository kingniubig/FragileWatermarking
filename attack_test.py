import numpy as np, cv2

# JPEG压缩
def attack_jpeg(img, qf=50):
    cv2.imwrite("t.jpg", img, [cv2.IMWRITE_JPEG_QUALITY, qf])
    return cv2.imread("t.jpg")

# 高斯噪声
def attack_gauss(img, sigma=5):
    noise = np.random.normal(0, sigma, img.shape)
    return np.clip(img + noise, 0, 255).astype(np.uint8)

# 椒盐噪声
def attack_salt_pepper(img, p=0.01):
    out = img.copy()
    m = np.random.rand(*img.shape[:2])
    out[m < p/2] = 0
    out[m > 1-p/2] = 255
    return out

# 裁剪
def attack_crop(img, x, y, w, h):
    out = img.cpoy()
    out[y:y+h, x:x+w] = 0
    return out

# 替换
def attack_replace(img, patch, x, y):
    out = img.copy()
    h, w = patch.shape[:2]
    out[y:y+h, x:x+w] = patch
    return out

# 拼接
def attack_splice(img, patch, x, y, feather=5):
    out = img.copy()
    h, w = patch.shape[:2]
    mask = np.ones((h, w), np.float32)
    mask[:feather]  = np.linspace(0, 1, feather)[:, None]
    mask[-feather:] = np.linspace(1, 0, feather)[:, None]
    mask[:, :feather]  *= np.linspace(0, 1, feather)[None, :]
    mask[:, -feather:] *= np.linspace(1, 0, feather)[None, :]
    roi = out[y:y+h, x:x+w].astype(np.float32)
    out[y:y+h, x:x+w] = (patch * mask[..., None] +
                         roi * (1 - mask[..., None])).astype(np.uint8)
    return out