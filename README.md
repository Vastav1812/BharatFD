#  BharatFD - Frequently Asked Questions Multilinguistic API

![Django](https://img.shields.io/badge/Django-4.2.7-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue)
![Render](https://img.shields.io/badge/Deployed_on-Render-purple)
![Python](https://img.shields.io/badge/Python-3.11-yellow)
![REST API](https://img.shields.io/badge/REST-API-orange)

##  Overview

**BharatFD** is a multilingual Frequently Asked Questions (FAQ) API built with **Django REST Framework (DRF)**.  
It supports dynamic content management using **Django Admin**, **PostgreSQL**, and **Redis caching** for optimized performance.

## Features

- ✅ **RESTful API** for FAQ retrieval
- ✅ **Admin panel** for managing FAQs
- ✅ **Multilingual support** using **Google Translate API**
- ✅ **Redis caching** for fast responses
- ✅ **Deployed on Render** (Free Plan)
- ✅ **PostgreSQL as the database backend**
- ✅ **Static file handling via WhiteNoise**

##  Tech Stack

| Technology     | Purpose                           |
|--------------|--------------------------------|
| Django       | Backend Framework              |
| Django REST Framework | API Implementation      |
| PostgreSQL   | Database for structured data   |
| Redis        | Caching for fast responses     |
| Gunicorn     | WSGI HTTP Server for Django    |
| Render       | Cloud Deployment               |
| WhiteNoise   | Serving Static Files Efficiently |

---

##  Installation & Setup

### 1️ **Clone the Repository**
```sh
git clone https://github.com/Vastav1812/BharatFD.git
cd BharatFD
```
### 2️ **Create & Activate Virtual Environment**
```sh

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
### 3️ **Install Dependencies**
```sh

pip install -r requirements.txt
```
### 4️ **Set Up Environment Variables**
Create a .env file in the project root:

```sh

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@host:port/dbname
REDIS_URL=redis://127.0.0.1:6379/1
```
### Running the Application
### 5️ **Apply Migrations**
```sh

python manage.py migrate
```
###6️ **Collect Static Files**
```sh

python manage.py collectstatic --noinput
```
### 7️ **Start the Server**
```sh

python manage.py runserver
```
### Access API at:
```
http://127.0.0.1:8000/api/faqs/
```

### Admin Panel:
```
http://127.0.0.1:8000/admin/
(Default Superuser: admin / admin)
```
![Screenshot](Screenshots/admin_login.png)

![Screenshot](Screenshots/admin.png)
---

##  **Endpoints**

### **1️ Retrieve All FAQs**
####  **Endpoint**
```
GET /api/faqs/
```
#### **Example Request**
```
curl -X GET "http://127.0.0.1:8000/api/faqs/" -H "Accept: application/json"
```
####  **Example Response**
```json
[
    {
        "id": 1,
        "question": "What is Django?",
        "answer": "Django is a high-level Python web framework.",
        "language": "en"
    },
    {
        "id": 2,
        "question": "What is Python?",
        "answer": "Python is a programming language for web development and data science.",
        "language": "en"
    }
]
```
![Screenshot](Screenshots/english.png)

### 2️ **Retrieve FAQs in Hindi (हिंदी)**
### Endpoint
```bash
GET /api/faqs/?lang=hi
```
### Example Request
```sql
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=hi" -H "Accept: application/json"
```
### Example Response
```json

[
    {
        "id": 1,
        "question": "Django क्या है?",
        "answer": "Django एक उच्च-स्तरीय पायथन वेब फ्रेमवर्क है।",
        "language": "hi"
    },
    {
        "id": 2,
        "question": "Python क्या है?",
        "answer": "Python एक प्रोग्रामिंग भाषा है जो वेब विकास और डेटा विज्ञान के लिए उपयोग की जाती है।",
        "language": "hi"
    }
]
```
![Screenshot](Screenshots/hindi.png)
### 3 **Retrieve FAQs inBengali (বাংলা)**
### Endpoint
```bash
GET /api/faqs/?lang=bn
```
### Example Request
```sql
curl -X GET "http://127.0.0.1:8000/api/faqs/?lang=bn" -H "Accept: application/json"

```
### Example Response
```json
[
    {
        "id": 1,
        "question": "Django কি?",
        "answer": "Django একটি উচ্চ-স্তরের পাইথন ওয়েব ফ্রেমওয়ার্ক।",
        "language": "bn"
    },
    {
        "id": 2,
        "question": "Python কি?",
        "answer": "Python হল একটি প্রোগ্রামিং ভাষা যা ওয়েব উন্নয়ন এবং ডেটা বিজ্ঞানের জন্য ব্যবহৃত হয়।",
        "language": "bn"
    }
]

```
![Screenshot](Screenshots/bengali.png)





