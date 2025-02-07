# Sanskrit-English-Hindi Translator

## 📌 Overview
This is a simple web application that allows users to translate:
- **Sanskrit → English**
- **English → Hindi**

The app is built using **Flask** for the backend and **Hugging Face's MarianMT models** for translation. It provides an intuitive web interface using **Bootstrap** for styling.

---

## 🚀 Features
✅ Translate **Sanskrit to English** using MarianMT
✅ Translate **English to Hindi** using MarianMT
✅ Simple web interface built with **Flask & Bootstrap**
✅ Lightweight and runs locally
✅ No API key required (Offline translation using MarianMT)

---

## 📂 Project Structure
```
bhaasaantar/
│── static/
│    └── styles.css      # CSS file for styling
│── templates/
│    ├── index.html      # Webpage UI
│── app.py               # Flask Backend
│── requirements.txt     # Python Dependencies
│── Dockerfile           # Docker Setup
│── docker-compose.yml   # Docker Compose Configuration
│── README.md            # Project Documentation
```
---

## 🔧 Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have **Python 3.8+** installed, then install the required packages:
```bash
pip install flask transformers sentencepiece sacremoses torch
```

### 2️⃣ Run the Application
```bash
python app.py
```
The Flask server will start, and you will see:
```
Running on http://127.0.0.1:5000/
```

### 3️⃣ Open in Browser
Visit **`http://127.0.0.1:5000/`** to access the translator.

---

## 🐳 Docker Setup & Deployment

### 1️⃣ Build and Run with Docker
Ensure you have **Docker** installed, then create a `Dockerfile` with the following content:

```dockerfile
# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
```

### 2️⃣ Create `docker-compose.yml`

```yaml
version: '3'
services:
  translator-app:
    build: .
    ports:
      - "5000:5000"
```

### 3️⃣ Build and Run the Container
Run the following commands to build and start the container:
```bash
docker-compose up --build -d
```

The app will be available at **`http://localhost:5000/`**.

### 4️⃣ Stop and Remove Containers
To stop and remove the running containers, use:
```bash
docker-compose down
```

---

## 🚀 Deploying Docker Container to Cloud

### 1️⃣ Deploy on AWS Elastic Beanstalk
1. Install the AWS Elastic Beanstalk CLI:
   ```bash
   pip install awsebcli --upgrade
   ```
2. Initialize the project:
   ```bash
   eb init -p docker translator-app
   ```
3. Create an environment and deploy:
   ```bash
   eb create translator-env
   ```

### 2️⃣ Deploy on Google Cloud Run
1. Authenticate with GCP:
   ```bash
   gcloud auth login
   ```
2. Build and push Docker image:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/translator-app
   ```
3. Deploy to Cloud Run:
   ```bash
   gcloud run deploy translator-app --image gcr.io/YOUR_PROJECT_ID/translator-app --platform managed --region us-central1 --allow-unauthenticated
   ```

### 3️⃣ Deploy on DigitalOcean
1. Install and log in to DigitalOcean CLI:
   ```bash
   doctl auth init
   ```
2. Create an app:
   ```bash
   doctl apps create --spec app.yaml
   ```

### 4️⃣ Deploy on Heroku
1. Install the Heroku CLI:
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh
   ```
2. Login and create an app:
   ```bash
   heroku login
   heroku create translator-app
   ```
3. Push the Docker container:
   ```bash
   heroku container:push web -a translator-app
   heroku container:release web -a translator-app
   ```

---

## 🖥️ Usage Guide
1️⃣ **Enter text** in Sanskrit or English.
2️⃣ **Select translation type**:
   - Sanskrit → English
   - English → Hindi
3️⃣ Click **Translate**.
4️⃣ View the translated text on the screen.

---

## 🛠️ Technology Stack
- **Flask** (Python Web Framework)
- **Hugging Face MarianMT** (Pre-trained translation models)
- **Bootstrap** (Frontend Styling)
- **Torch & Transformers** (AI Model Inference)
- **Docker** (Containerization)
- **AWS, GCP, DigitalOcean, Heroku** (Cloud Deployment)

---

## 📌 Future Improvements
🔹 Add **Hindi → Sanskrit** translation
🔹 Deploy on **AWS / Render / Hugging Face Spaces**
🔹 Add support for **batch translations**
🔹 Use **Google Translate API** as an alternative

---

## 📜 License
This project is **open-source** and free to use.

---

## 🤝 Contributions
Feel free to contribute! Fork the repo and submit a pull request.

---

## 📞 Contact
For any questions or issues, contact **[Your Name]** at **info@bhaasaantar.com**.

