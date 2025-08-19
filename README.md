
# 🧥 Invisibility Cloak with OpenCV

A fun computer vision project that recreates the **famous “invisibility cloak” illusion** in real-time using color segmentation and background replacement.

## 🎥 Demo
Wear a solid red/green/blue cloak, capture a clean background, and watch yourself **disappear** on camera!

---

## ⚡ How It Works
1. **Capture background** : Take a snapshot of the static scene without the subject.  
2. **Color detection** : Segment cloak pixels in HSV color space.  
3. **Masking & replacement** : Replace cloak pixels with the background snapshot.  
4. **Real-time illusion** : Cloak area appears invisible on video.  

---

## 🛠 Tech Stack
- **Python 3.8+**
- [OpenCV](https://opencv.org/) (Computer Vision)
- NumPy (Matrix operations)



## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/AmenAllahHemdani/Invisibility-Cloak.git
cd Invisibility-Cloak
pip install -r requirements.txt
````

Contents of `requirements.txt`:

```txt
opencv-python
numpy
```

---

## ▶️ Usage

Run the script:

```bash
python cloak.py --source 0 --color red --save output.mp4
```

### Arguments

* `--source` : Camera index or video file path (default: `0` = webcam).
* `--color`  : Cloak color preset (`red`, `green`, `blue`).
* `--save`   : Optional output video path (e.g. `output.mp4`).
* `--width` / `--height` : Resize video (default: keep native resolution).

---

## 🎮 Controls

* **`b`** → Capture background (do this when the scene is empty).
* **`r`** → Switch cloak color → red
* **`g`** → Switch cloak color → green
* **`B`** → Switch cloak color → blue
* **`s`** → Toggle saving to video (if `--save` was given).
* **`q` / `ESC`** → Quit.

---

## 📚 Key Learnings

* HSV color masking & segmentation
* Morphological operations for noise removal
* Background subtraction techniques
* Real-time video processing

---

## 🚀 Next Steps

* Replace `build_mask` with a **deep learning segmentation model** (e.g., U-Net, DeepLab) for robust cloak detection.
* Use **video matting** for smooth cloak edges.
* Add **temporal smoothing** to reduce flickering.

---

## 📜 License

MIT License – feel free to use and remix!

---