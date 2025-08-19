import cv2
import numpy as np
from .constant import COLOR_PRESETS

# --- Module: Mask builder ---
def build_mask(hsv, color_key: str) -> np.ndarray:
    ranges = COLOR_PRESETS[color_key]
    mask_total = np.zeros(hsv.shape[:2], dtype=np.uint8)
    for r in ranges:
        lower = np.array(r["lower"], dtype=np.uint8)
        upper = np.array(r["upper"], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        mask_total = cv2.bitwise_or(mask_total, mask)

    # cleanup
    kernel_open = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    kernel_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask_clean = cv2.morphologyEx(mask_total, cv2.MORPH_OPEN, kernel_open, iterations=2)
    mask_clean = cv2.dilate(mask_clean, kernel_dilate, iterations=1)
    return mask_clean
