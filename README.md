# Simple JWT Authentication with Django REST Framework

A Django REST Framework project demonstrating **JWT (JSON Web Token) authentication** and REST API development. This project includes student data endpoints and uses Simple JWT to secure API access.

## 🚀 Features

- REST API development using Django REST Framework
- JWT-based authentication
- Access and refresh token generation
- Student data retrieval through API endpoints
- API testing using Postman

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- Simple JWT
- Postman
- Git and GitHub

## 📦 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RahulBhola1/simple-jwt.git
cd simple-jwt
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

Activate it:

**macOS/Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

If a `requirements.txt` file is available, use:

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

The server will run at:

`http://127.0.0.1:8000/`

## 🔑 JWT Authentication

### Obtain access and refresh tokens

**Endpoint:** `POST /api/token/`

Example request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

A successful response contains an access token and a refresh token.

### Refresh the access token

**Endpoint:** `POST /api/token/refresh/`

Example request body:

```json
{
  "refresh": "your_refresh_token"
}
```

The response provides a new access token.

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh access token |
| GET | `/student/stds` | Retrieve student data |

Use the endpoints configured in your Django project's `urls.py`. Protected endpoints require a valid access token.

## 🧪 Testing with Postman

1. Start the Django development server.
2. Send a POST request to `/api/token/` with valid login credentials.
3. Copy the returned access token.
4. Open the student API request in Postman.
5. Select **Authorization → Bearer Token**.
6. Paste the access token and send the request.

## 🔒 Security Notes

- Never commit passwords, secret keys, or real access tokens to GitHub.
- Keep Django's `SECRET_KEY` private.
- Use HTTPS in production.
- Configure token lifetimes and permissions according to your application's requirements.

## 👨‍💻 Author

**Rahul Bhola**

GitHub: [RahulBhola1](https://github.com/RahulBhola1)

---

⭐ If you find this project useful, feel free to explore the repository and follow my development journey.
