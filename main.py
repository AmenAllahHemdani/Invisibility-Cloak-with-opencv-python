import time
import cv2
from utils.process import process_frame
from utils.init_writer import init_writer
from utils.parse import parse_args
from utils.capture import capture_background

# --- Main loop ---
def main():
    args = parse_args()

    color_key = args.color
    saving_enabled = bool(args.save)
    writer = None

    cap = cv2.VideoCapture(args.source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source {args.source}")

    if args.width > 0:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    if args.height > 0:
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

    time.sleep(0.5)

    background = None
    got_background = False
    print("[INFO] Press 'b' to capture background when the scene is clear.")
    print("[INFO] Press 'r'/'g'/'B' to switch cloak color. Current:", color_key)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[WARN] Frame grab failed. Exiting.")
            break

        mask, output = process_frame(frame, background, color_key, got_background)

        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("Invisibility Cloak", output)

        # Init writer if needed
        if saving_enabled and writer is None:
            h, w = output.shape[:2]
            writer = init_writer(args.save, (w, h), cap.get(cv2.CAP_PROP_FPS))
            if writer is None:
                saving_enabled = False

        if saving_enabled and writer is not None:
            writer.write(output)

        key = cv2.waitKey(1) & 0xFF
        if key in (27, ord('q')):  # ESC or q
            break
        elif key == ord('b'):
            background = capture_background(cap)
            got_background = True
        elif key == ord('r'):
            color_key = "red"; print("[INFO] Switched color -> red")
        elif key == ord('g'):
            color_key = "green"; print("[INFO] Switched color -> green")
        elif key == ord('B'):
            color_key = "blue"; print("[INFO] Switched color -> blue")
        elif key == ord('s'):
            if args.save:
                saving_enabled = not saving_enabled
                state = "ON" if saving_enabled else "OFF"
                print(f"[INFO] Save-to-video toggled {state}.")
            else:
                print("[INFO] Provide --save path to enable saving.")

    cap.release()
    if writer is not None:
        writer.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
