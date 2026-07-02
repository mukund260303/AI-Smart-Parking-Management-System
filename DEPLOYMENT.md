# ParkEase Deployment Guide

## Quick Deploy to Render (Free)

### Prerequisites
1. Create a [Render](https://render.com) account
2. Create a [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) account for free cloud database

### Step 1: Set up MongoDB Atlas
1. Go to https://www.mongodb.com/cloud/atlas
2. Create a free cluster
3. Create a database user with username and password
4. Whitelist all IPs (0.0.0.0/0) under Network Access
5. Get your connection string (format: `mongodb+srv://username:password@cluster.mongodb.net/parkingdb`)

### Step 2: Initialize Your Database
Run the initialization script with your MongoDB Atlas connection string:
```bash
python init_parking.py
```

### Step 3: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/parkease.git
git push -u origin main
```

### Step 4: Deploy to Render
1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: parkease
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add Environment Variables:
   - `MONGODB_URI`: Your MongoDB Atlas connection string
   - `SECRET_KEY`: Generate a random secret key
   - `PYTHON_VERSION`: 3.12.8
6. Click "Create Web Service"

Your app will be live at: `https://parkease.onrender.com`

---

## Alternative: Deploy to Railway

1. Go to https://railway.app
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo"
4. Add environment variables:
   - `MONGODB_URI`
   - `SECRET_KEY`
5. Railway will auto-detect and deploy your Flask app

---

## Local Production Server (Windows)

Install waitress (Windows-friendly WSGI server):
```bash
pip install waitress
```

Run production server:
```bash
waitress-serve --host=0.0.0.0 --port=8080 app:app
```

Access at: http://localhost:8080

---

## Important Notes

- Make sure to initialize parking data after first deployment
- Update YOLO model path if needed for production
- Keep SECRET_KEY and MONGODB_URI secure
- For production, consider using a reverse proxy like Nginx
