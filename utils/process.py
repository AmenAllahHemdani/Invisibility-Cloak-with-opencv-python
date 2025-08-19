import cv2
from .build_mask import build_mask

# --- Module: Frame processing ---
def process_frame(frame, background, color_key, got_background):
    frame_blur = cv2.GaussianBlur(frame, (7, 7), 0)
    hsv = cv2.cvtColor(frame_blur, cv2.COLOR_BGR2HSV)
    mask = build_mask(hsv, color_key)

    if got_background:
        mask_inv = cv2.bitwise_not(mask)
        cloak_area = cv2.bitwise_and(background, background, mask=mask)
        non_cloak_area = cv2.bitwise_and(frame, frame, mask=mask_inv)
        output = cv2.addWeighted(cloak_area, 1.0, non_cloak_area, 1.0, 0.0)
    else:
        output = frame.copy()

    return mask, output