# 🌿 Plant Poison Detection using Deep Learning

A Machine Learning / Deep Learning project that classifies whether a plant is **poisonous or non-poisonous** using an uploaded image.

---

## 📌 Overview

This project uses a **Convolutional Neural Network (CNN)** with transfer learning to analyze plant images and predict toxicity.

It is designed as a **real-world application** that can help identify potentially harmful plants.

---

## 🚀 Features

* 📷 Upload plant images
* 🧠 Deep learning-based classification
* ⚡ Fast predictions using MobileNetV2
* 📊 Confidence score output
* 🌐 Simple web interface using Streamlit

---

## 🛠️ Tech Stack

* Python
* TensorFlow / Keras
* NumPy
* Streamlit
* PIL (Python Imaging Library)

---

## 📂 Project Structure

```
plant_poison_project/
│
├── dataset/
│   ├── poisonous/
│   └── non_poisonous/
│
├── model/
│   └── plant_model.h5
│
├── train.py
├── predict.py
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/plant-poison-detector.git
cd plant-poison-detector
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate:

```
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## 🧠 Train the Model

```
python train.py
```

This will generate:

```
model/plant_model.h5
```

---

## 🔍 Run Prediction (CLI)

```
python predict.py
```

---

## 🌐 Run Web App

```
streamlit run app.py
```

---

## 📊 Dataset

* Custom dataset of plant images
* Two classes:

  * Poisonous plants (e.g., Datura, Oleander)
  * Non-poisonous plants (e.g., Neem, Mint)

---

## ⚠️ Limitations

* Accuracy depends on dataset quality
* Some plants look visually similar
* Not suitable for medical or safety-critical decisions

---

## 🔮 Future Improvements

* 🌿 Multi-class plant species detection
* 📱 Mobile app integration
* 🔍 Explainable AI (Grad-CAM)
* ☁️ Cloud deployment

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit pull requests.

---

## 📜 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Meet Dutta**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
