import cv2
from pathlib import Path

# --- Module: Video writer init ---
def init_writer(path, output_shape, fps):
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(out_path), fourcc, fps or 25.0, output_shape)
    if not writer.isOpened():
        print("[WARN] Could not open video writer.")
        return None
    return writer