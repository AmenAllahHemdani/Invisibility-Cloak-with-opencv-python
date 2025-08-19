import cv2
import numpy as np

# --- Module: Background capture ---
def capture_background(cap, num_frames=30) -> np.ndarray:
    print("[INFO] Capturing background...")
    acc = None
    for _ in range(num_frames):
        ret, frm = cap.read()
        if not ret:
            continue
        frm = cv2.GaussianBlur(frm, (7, 7), 0)
        if acc is None:
            acc = frm.astype(np.float32)
        else:
            cv2.accumulate(frm.astype(np.float32), acc)
    bg = (acc / max(1, num_frames)).astype(np.uint8)
    print("[INFO] Background captured.")
    return bg