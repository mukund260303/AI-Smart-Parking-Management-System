# 🚗 AI Smart Parking Management System

An AI-powered Smart Parking Management System built using **Flask, MongoDB, YOLOv8, OpenCV, and Arduino Integration**. The system enables users to reserve parking slots online while allowing administrators to monitor parking occupancy using computer vision and IoT sensors.

---

## ✨ Features

- 🔐 User Registration & Login
- 🚗 Online Parking Slot Reservation
- 🤖 AI-Based Vehicle Detection using YOLOv8
- 🎥 Real-Time Video Processing with OpenCV
- 📊 Live Parking Availability Dashboard
- 👨‍💼 Admin Dashboard
- 💰 Parking Price Calculator
- 🗄️ MongoDB Database Integration
- 📡 Arduino Sensor Integration
- 📱 Responsive Web Interface

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | HTML5, CSS3, JavaScript, Jinja2 |
| Backend | Python, Flask |
| Database | MongoDB, PyMongo |
| Authentication | Flask-Login, bcrypt |
| AI & Computer Vision | YOLOv8, OpenCV |
| Hardware | Arduino, PySerial |
| Deployment | Gunicorn, Render |

---

## 🏗️ System Workflow

```text
User
   │
   ▼
Flask Web Application
   │
   ▼
MongoDB Database
   ▲
   │
OpenCV + YOLOv8
   │
Arduino Sensors
   │
   ▼
Real-Time Parking Status
```

---

## 📂 Project Structure

```text
AI-Smart-Parking-Management-System/
│── app.py
│── db.py
│── users.py
│── training.py
│── requirements.txt
│── models/
│── templates/
│── static/
│── screenshots/
│── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/mukund260303/AI-Smart-Parking-Management-System.git
cd AI-Smart-Parking-Management-System
```

Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Initialize MongoDB

```bash
python init_parking.py
```

Run the project

```bash
python app.py
```

Open

```text
http://localhost:5000
```

---

## 📸 Screenshots

### Landing Page

![Landing](screenshots/loginpage.png)

### Login

![Login](screenshots/loginpage_2.png)

### User Dashboard

![Dashboard](screenshots/userdashboard.png)

### Booking Page

![Booking](screenshots/booking_page.png)

### Payment Page

![Payment](screenshots/Payment_page.png)

### Admin Dashboard

![Admin](screenshots/admin_page_1.png)

---

## 🚀 Future Enhancements

- Automatic Number Plate Recognition (ANPR)
- QR Code Based Entry
- Email Notifications
- UPI Payment Gateway
- Parking Analytics Dashboard
- Mobile Application

---

## 📖 What I Learned

- Flask Web Development
- MongoDB Integration
- User Authentication
- OpenCV Image Processing
- YOLOv8 Object Detection
- Arduino Serial Communication
- Git & GitHub
- Full-Stack Project Deployment

---

## 👨‍💻 About This Repository

This repository is maintained for learning, experimentation, and demonstrating the integration of **Flask, MongoDB, OpenCV, YOLOv8, and Arduino** in a smart parking management application. I have configured, deployed, studied, and documented the project while continuing to enhance it with additional features and improvements.

---

## 👤 Developer

**Balmukund Patidar**

🎓 MCA Student | NIT Raipur

🔗 GitHub: https://github.com/mukund260303

---

⭐ If you found this project useful, consider giving it a star.