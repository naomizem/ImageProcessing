# ==========================================================
# עיבוד תמונה – תרגיל 03
# ==========================================================

import numpy as np
import cv2
import matplotlib.pyplot as plt


# ==========================================================
# שאלה 1 – Backward Mapping
# ==========================================================

def backward_mapping(img, T, output_shape):
    h, w = output_shape
    result = np.zeros((h, w, 3), dtype=img.dtype)

    # מטריצה הפוכה
    T_inv = np.linalg.inv(T)

    for i in range(h):
        for j in range(w):

            # מרכז הפיקסל
            x = j + 0.5
            y = i + 0.5

            # מעבר למקור
            src = T_inv @ np.array([x, y, 1])
            xs, ys = src[0], src[1]

            xs -= 0.5
            ys -= 0.5

            # nearest neighbor
            xi = int(round(xs))
            yi = int(round(ys))

            if 0 <= xi < img.shape[1] and 0 <= yi < img.shape[0]:
                result[i, j] = img[yi, xi]

    return result


# ==========================================================
# שאלה 2 – מטריצות טרנספורמציה (הומוגניות)
# ==========================================================

# מטריצת סיבוב
def rotation_matrix(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])


# מטריצת Scaling
def scale_matrix(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])


# ==========================================================
# שאלה 3 – הפעלת טרנספורמציה על תמונה
# ==========================================================

if __name__ == "__main__":

    print("======================================")
    print("שאלה 3 – טרנספורמציה על תמונה")
    print("======================================")

    # טעינת תמונה
    img = cv2.imread("image.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w = img.shape[:2]

    # ========================
    # יצירת מטריצות
    # ========================
    theta = np.deg2rad(30)

    R = rotation_matrix(theta)
    S = scale_matrix(1.5, 1.5)

    print("\nRotation matrix:\n", R)
    print("\nScaling matrix:\n", S)

    # ========================
    # שילוב טרנספורמציות
    # ========================
    T = R @ S   # קודם Scale ואז Rotate

    print("\nTransformation matrix (R @ S):\n", T)

    # ========================
    # הפעלת Backward Mapping
    # ========================
    result = backward_mapping(img, T, (h, w))

    # ========================
    # הצגה
    # ========================
    plt.figure(figsize=(8, 8))
    plt.imshow(result)
    plt.title("Transformed Image")
    plt.axis("off")
    plt.show()