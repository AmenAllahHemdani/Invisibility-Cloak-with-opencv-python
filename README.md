
# Invisibility Cloak (Real-Time)

### How it works:
1) Capture a static background frame (press 'b' when your scene is clear).
2) Detect a chosen cloth color (HSV thresholding with presets).
3) Replace the cloak region with the background to create the illusion.

### Controls:
  b : capture background
  r / g / b : switch target color (red / green / blue)
  s : toggle save-to-video (if --save given)
  q / ESC : quit

### Example:
  python invisible_cloak.py --color red --source 0 --save output.mp4

### Dependencies:
  pip install opencv-python numpy
