# 🛰️ SatVision AI

> **AI-Powered Satellite Change Detection & Semantic Segmentation Platform**

SatVision AI is an end-to-end satellite image analysis platform that leverages Deep Learning to detect land-cover changes, perform semantic segmentation, generate AI-powered insights, and create downloadable PDF reports through an interactive Streamlit dashboard.

---

## 🚀 Features

### 🌍 Satellite Change Detection

* Compare before and after satellite images.
* Detect environmental and land-cover changes.
* Generate binary change masks using Deep Learning.

### 🧠 Semantic Segmentation

Classifies satellite imagery into:

* 🌳 Vegetation
* 🏙️ Urban Area
* ⬜ Background

### 🔥 Heatmap Visualization

* Visualize changed regions with interactive heatmaps.
* Easily identify affected areas.

### 🖼️ Overlay Generation

* Overlay predicted changes on original satellite imagery.
* Improve visual interpretation of detected changes.

### 📊 Dashboard & Analytics

* Interactive dashboard
* Analysis history
* Performance statistics
* Change trends
* Historical reports

### 🤖 AI Generated Insights

* Generates intelligent analysis using the Groq API.
* Provides:

  * Location overview
  * Historical context
  * Environmental observations
  * Future outlook

### 📄 PDF Report Generation

Automatically generates professional reports containing:

* Satellite images
* Change percentage
* Semantic analysis
* Heatmaps
* AI observations
* Statistics

### 🔐 User Authentication

* Secure Login & Signup
* SQLite Database Integration
* User-specific report history

---

# 🧠 AI Models

## Change Detection Model

* Architecture: U-Net
* Framework: PyTorch
* Input Resolution: 256 × 256
* Output: Binary Change Mask

## Semantic Segmentation Model

* Architecture: Semantic U-Net
* Framework: PyTorch

Classes:

* Vegetation
* Urban
* Background

---

# 🛠️ Technology Stack

## Frontend

* Streamlit
* HTML
* CSS

## Backend

* Python
* SQLite

## Deep Learning

* PyTorch
* OpenCV
* NumPy

## Visualization

* Matplotlib
* Folium

## AI Integration

* Groq API

## Reporting

* ReportLab

---

# 📂 Project Structure

```text
SatVision-AI
│
├── app.py
├── pages/
├── saved_models/
├── sidebar.py
├── auth.py
├── database.py
├── predict.py
├── semantic_predict.py
├── requirements.txt
├── README.md
└── .streamlit/
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Sidtyagi81/satvision-ai.git
```

### Navigate to Project

```bash
cd satvision-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Add Groq API Key

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GROQ_API_KEY = "YOUR_GROQ_API_KEY"
```

---

### Run Application

```bash
streamlit run app.py
```

---

# 🔄 Workflow

```text
Before Satellite Image
          │
          ▼
Upload Images
          │
          ▼
U-Net Change Detection
          │
          ▼
Binary Change Mask
          │
          ▼
Heatmap Generation
          │
          ▼
Semantic Segmentation
          │
          ▼
AI Generated Insights
          │
          ▼
PDF Report Generation
```

---

# 📈 Future Improvements

* Multi-class Change Detection
* Time-series Satellite Analysis
* GIS Integration
* Cloud Storage Support
* Real-time Satellite Monitoring
* Multi-user Collaboration

---

# 👨‍💻 Author

**Siddhartha Tyagi**

Computer Science Engineering Student

GitHub:
https://github.com/Sidtyagi81

LinkedIn:
https://www.linkedin.com/in/siddhartha-tyagi-22a088308/

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates further improvements.
