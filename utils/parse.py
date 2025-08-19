import argparse
from .constant import COLOR_PRESETS

# --- Module: Argument parser ---
def parse_args():
    ap = argparse.ArgumentParser(description="Invisibility Cloak in Real-Time (OpenCV).")
    ap.add_argument("--source", type=int, default=0, help="Video source index (default: 0).")
    ap.add_argument("--color", type=str, default="red", choices=list(COLOR_PRESETS.keys()),
                    help="Target cloak color preset.")
    ap.add_argument("--save", type=str, default="", help="Optional output video path (e.g., output.mp4).")
    ap.add_argument("--width", type=int, default=0, help="Resize width (0 = keep native).")
    ap.add_argument("--height", type=int, default=0, help="Resize height (0 = keep native).")
    return ap.parse_args()