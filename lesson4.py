import numpy as np
import cv2
import time

# ===============================
# פונקציה מתרגיל 3
# ===============================
def backward_mapping(img, T, output_shape):
    h, w = output_shape
    result = np.zeros((h, w, 3), dtype=img.dtype)

    T_inv = np.linalg.inv(T)

    for i in range(h):
        for j in range(w):
            x = j + 0.5
            y = i + 0.5

            src = T_inv @ np.array([x, y, 1])
            xs, ys = src[0] - 0.5, src[1] - 0.5

            xi = int(round(xs))
            yi = int(round(ys))

            if 0 <= xi < img.shape[1] and 0 <= yi < img.shape[0]:
                result[i, j] = img[yi, xi]

    return result


# ===============================
# מטריצות
# ===============================
def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

def scale_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])


# ===============================
# Vectorized
# ===============================
def warp_vectorized(img, T):
    h, w = img.shape[:2]

    ys, xs = np.meshgrid(np.arange(h), np.arange(w), indexing='ij')

    xs = xs + 0.5
    ys = ys + 0.5

    ones = np.ones_like(xs)
    coords = np.stack([xs, ys, ones], axis=0).reshape(3, -1)

    T_inv = np.linalg.inv(T)
    src_coords = T_inv @ coords

    xs_src = src_coords[0, :] - 0.5
    ys_src = src_coords[1, :] - 0.5

    xi = np.round(xs_src).astype(int)
    yi = np.round(ys_src).astype(int)

    valid = (
        (xi >= 0) & (xi < img.shape[1]) &
        (yi >= 0) & (yi < img.shape[0])
    )

    result = np.zeros_like(img).reshape(-1, 3)
    result[valid] = img[yi[valid], xi[valid]]

    return result.reshape(h, w, 3)


# ===============================
# MAIN
# ===============================
if __name__ == "__main__":

    print("======================================")
    print("שאלה 4 – השוואת ביצועים")
    print("======================================")

    # 🔥 טוענים תמונה
    img = cv2.imread("image.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 🔥 יוצרים מטריצה
    theta = np.deg2rad(30)
    R = rotation_matrix(theta)
    S = scale_matrix(1.5, 1.5)
    T = R @ S

    # ========================
    # לולאות
    # ========================
    start = time.time()
    res1 = backward_mapping(img, T, img.shape[:2])
    t1 = time.time() - start

    # ========================
    # וקטורי
    # ========================
    start = time.time()
    res2 = warp_vectorized(img, T)
    t2 = time.time() - start

    print("\nLoop time:", t1)
    print("Vectorized time:", t2)