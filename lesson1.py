# ==========================================================
# עיבוד תמונה – תרגיל 01
# ==========================================================

import numpy as np
import matplotlib.pyplot as plt
import cv2


# ==========================================================
# שאלה 1 – פונקציות טריגונומטריות
# ==========================================================

# פונקציה שממירה מעלות לרדיאנים
def degrees_to_radians(degrees):
    return degrees * np.pi / 180


if __name__ == "__main__":

    print("======================================")
    print("שאלה 1 – חישוב radians, sin, cos")
    print("======================================")

    angles_degrees = [0, 90, 180, 45, 30, 10, 5, 1]

    print("degrees,radians,sin,cos")

    for deg in angles_degrees:
        rad = degrees_to_radians(deg)
        s = np.sin(rad)
        c = np.cos(rad)
        print(f"{deg},{rad:.6f},{s:.6f},{c:.6f}")


    # ==========================================================
    # שאלה 3 – מטריצות סיבוב ו-Scaling
    # ==========================================================

    print("\n======================================")
    print("שאלה 3 – מטריצות וטרנספורמציות")
    print("======================================")

    # א. מטריצת סיבוב 30 מעלות
    theta = degrees_to_radians(30)

    r_30 = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    print("\nr_30 =\n", r_30)

    # ב. מטריצת scaling בציר X פי 2
    sx_2 = np.array([
        [2, 0],
        [0, 1]
    ])

    print("\nsx_2 =\n", sx_2)

    # ג. R ואז S
    rs = r_30 @ sx_2
    print("\nrs (R then S) =\n", rs)

    # ד. S ואז R
    sr = sx_2 @ r_30
    print("\nsr (S then R) =\n", sr)


    # ה. יצירת מלבן (מרכז בראשית, רוחב 2, גובה 1)
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

    # ו–ח. הפעלת הטרנספורמציות
    rotated = transform(rectangle, r_30)
    scaled = transform(rectangle, sx_2)
    rect_rs = transform(rectangle, rs)
    rect_sr = transform(rectangle, sr)

    # ט. הצגה עם matplotlib
    plt.figure()

    plt.plot(rectangle[:,0], rectangle[:,1], label="Original")
    plt.plot(rotated[:,0], rotated[:,1], label="Rotated 30°")
    plt.plot(scaled[:,0], scaled[:,1], label="Scaled X2")
    plt.plot(rect_rs[:,0], rect_rs[:,1], label="R then S")
    plt.plot(rect_sr[:,0], rect_sr[:,1], label="S then R")

    plt.axhline(0)
    plt.axvline(0)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title("Transformations")
    plt.show()