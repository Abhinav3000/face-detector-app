# 👁️ Real-Time Face Detection using MTCNN

This is a simple real-time face detection app built with Python.  
It uses your webcam to detect faces live and draws boxes around them using a deep learning model called **MTCNN** from `facenet-pytorch`.

If you're just getting into computer vision or want a clean starter project — this one's for you.  
No bells, no whistles, just straight-up detection. 🎯

---

## 🛠️ What it does

- Turns on your webcam  
- Detects faces in real time  
- Draws green boxes around detected faces  
- Quits cleanly when you press `Q`  

That's it. It's light, fast, and does the job.

---

## 🚀 How to run it

### 1. Clone the project

```bash
git clone https://github.com/Abhinav3000/face-detector-app.git
cd face-detector-app
```

### 2. Install required packages

Make sure Python 3.7+ is installed, then:

```bash
pip install -r requirements.txt
```

### 3. Start the app

```bash
python main.py
```

You’ll see a window pop up showing your webcam feed.  
Move your face around. Watch the green box follow like it’s got a crush on you 👀💚  
Hit `Q` anytime to close it cleanly.

---

## 🧠 Tech used

- **OpenCV** – to access webcam and draw boxes  
- **facenet-pytorch** – for pre-trained MTCNN face detection  
- **Pillow (PIL)** – to handle image conversion  
- **PyTorch** – the deep learning engine behind the scenes

---

## 🤓 Why I made this

Just exploring deep learning and computer vision, and wanted a clean, working setup to detect faces live.  
It’s a great intro to combining **pre-trained models**, **OpenCV**, and **PyTorch** — without getting too complex.

---

## 🙋‍♂️ Who's this for?

- Students & beginners in AI/ML  
- Anyone learning OpenCV or PyTorch  
- Anyone who wants a simple real-time face detection script to play with

---

## ⚡ Next ideas (feel free to fork & build on this):

- Count number of faces  
- Add face recognition (who’s who)  
- Save frames with detected faces  
- Make a GUI with Streamlit or Gradio  
- Deploy on Hugging Face Spaces

---

## 💬 P.S.

No fancy models, no internet dependency, no image uploads — just your face and a real-time box.  
Fast, lightweight, and fun. That’s how we roll. 
