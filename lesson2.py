# ==========================================================
# עיבוד תמונה – תרגיל 02
# ==========================================================

import numpy as np
import matplotlib.pyplot as plt


# ==========================================================
# שאלה 1 – פונקציות טריגונומטריות
# ==========================================================

# פונקציה שממירה מעלות לרדיאנים
def degrees_to_radians(degrees):
    return degrees * np.pi / 180


# ==========================================================
# שאלה 2 – מטריצות בסיסיות
# ==========================================================

# א. מטריצת סיבוב
def rotation_matrix(theta):
    theta_rad = np.deg2rad(theta)
    return np.array([
        [np.cos(theta_rad), -np.sin(theta_rad)],
        [np.sin(theta_rad),  np.cos(theta_rad)]
    ])


# ב. Scaling אחיד פי 2
def scale_uniform_2():
    return np.array([
        [2, 0],
        [0, 2]
    ])


# ג. Scaling בציר X בלבד
def scale_x_2():
    return np.array([
        [2, 0],
        [0, 1]
    ])


# ==========================================================
# שאלה 3 – טרנספורמציות ושרשור מטריצות
# ==========================================================

if __name__ == "__main__":

    # ========================
    # שאלה 1
    # ========================
    print("======================================")
    print("שאלה 1 – חישוב radians, sin, cos")
    print("======================================")

    degrees_list = [0, 90, 180, 45, 30, 10, 5, 1]

    print("degrees,radians,sin,cos")

    for deg in degrees_list:
        rad = degrees_to_radians(deg)
        sin_val = np.sin(rad)
        cos_val = np.cos(rad)

        print(f"{deg},{rad:.6f},{sin_val:.6f},{cos_val:.6f}")


    # ========================
    # שאלה 2
    # ========================
    print("\n======================================")
    print("שאלה 2 – מטריצות בסיסיות")
    print("======================================")

    r_30 = rotation_matrix(30)
    print("\nRotation matrix (30°):\n", r_30)

    scale_uniform = scale_uniform_2()
    print("\nScaling x2 (uniform):\n", scale_uniform)

    sx_2 = scale_x_2()
    print("\nScaling x2 in X direction:\n", sx_2)


    # ========================
    # שאלה 3
    # ========================
    print("\n======================================")
    print("שאלה 3 – מטריצות וטרנספורמציות")
    print("======================================")

    print("\nr_30 =\n", r_30)
    print("\nsx_2 =\n", sx_2)

    # חישוב שרשור מטריצות
    rs = r_30 @ sx_2
    sr = sx_2 @ r_30

    print("\nrs (R then S) =\n", rs)
    print("\nsr (S then R) =\n", sr)


    # ========================
    # יצירת מלבן
    # ========================
    rectangle = np.array([
        [-1, -0.5],
        [ 1, -0.5],
        [ 1,  0.5],
        [-1,  0.5],
        [-1, -0.5]
    ])


    # פונקציה להפעלת טרנספורמציה
    def transform(shape, matrix):
        return (matrix @ shape.T).T


    # ========================
    # הפעלת טרנספורמציות
    # ========================
    rect_rot = transform(rectangle, r_30)
    rect_scale = transform(rectangle, sx_2)
    rect_rs = transform(rectangle, rs)
    rect_sr = transform(rectangle, sr)


    # ========================
    # ציור
    # ========================
    plt.figure(figsize=(8, 8))

    plt.plot(rectangle[:, 0], rectangle[:, 1], label="Original")
    plt.plot(rect_rot[:, 0], rect_rot[:, 1], label="Rotate 30°")
    plt.plot(rect_scale[:, 0], rect_scale[:, 1], label="Scale x2")
    plt.plot(rect_rs[:, 0], rect_rs[:, 1], label="R then S")
    plt.plot(rect_sr[:, 0], rect_sr[:, 1], label="S then R")

    plt.axhline(0)
    plt.axvline(0)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title("Rectangle Transformations")
    plt.grid()

    plt.show()