<div align="center">

<h1>
  🔐 Flask Template – User Management System
</h1>

[![GitHub stars](https://img.shields.io/github/stars/Arviixzuhs/Flask-template?style=for-the-badge)](https://github.com/Arviixzuhs/Flask-template/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Arviixzuhs/Flask-template?style=for-the-badge)](https://github.com/Arviixzuhs/Flask-template/network)
[![GitHub issues](https://img.shields.io/github/issues/Arviixzuhs/Flask-template?style=for-the-badge)](https://github.com/Arviixzuhs/Flask-template/issues)

**A clean, modular and production‑ready Flask template  
with authentication, JWT, and user management built‑in.**

</div>

---

## 📚 Table of Contents

- [About The Project](#-about-the-project)
- [Architecture Overview](#-architecture-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Project Structure](#-project-structure)
- [Scripts](#-scripts)
- [Design Principles](#-design-principles)
- [Contributing](#-contributing)
- [Author](#-author)

---

## 🚀 About The Project

This **Flask Template** is a lightweight but powerful starter kit for building secure backend services.

It includes:

- A modular architecture ready for scaling
- Built‑in authentication with JWT
- User CRUD operations
- Environment‑based configuration
- SQLite database integration with SQLAlchemy

Perfect for APIs, prototypes, or production‑ready microservices.

---

## 🏗 Architecture Overview

```
Flask-template/
└── src/        # Application source code
```

### Core Concepts

- **Flask** for routing and application logic  
- **SQLAlchemy ORM** for database modeling  
- **JWT Authentication** for secure access  
- **Blueprint-based modularity** for clean separation of concerns  

---

## ✨ Key Features

- 🔐 **JWT Authentication** (login, register, token validation)
- 🧂 **Password hashing** using bcrypt
- 🧩 **Modular service structure** (auth, user, decorators)
- 🗄 **SQLite database** with SQLAlchemy ORM
- 🛡 **Middleware for protected routes**
- ⚙️ **Environment-based configuration**
- 🚀 **Ready-to-extend architecture**

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Flask‑SQLAlchemy
- Flask‑Migrate
- Bcrypt
- PyJWT

### Database
- SQLite (default, easily replaceable)

---

## ⚙️ Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Arviixzuhs/Flask-template.git
cd Flask-template
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Initialize Database

```bash
flask db init
flask db migrate
flask db upgrade
```

### 4️⃣ Run the Application

```bash
python run.py
```

Server runs at:

```
http://localhost:5000
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```
FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET=your_jwt_secret
DATABASE_URL=sqlite:///database.db
```

---

## 📁 Project Structure

```
.
├── run.py
├── src
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── env.py
│   ├── decorators/
│   │   ├── __init__.py
│   │   ├── auth_middleware.py
│   ├── modules/
│   │   ├── auth/
│   │   │   ├── __init__.py
│   │   │   ├── auth_service.py
│   │   ├── user/
│   │   │   ├── __init__.py
│   │   │   ├── user_service.py
│   ├── routes.py
│   ├── sqlite/
│   │   ├── __init__.py
│   │   ├── database.py
├── requirements.txt
```

---

## 🧪 Scripts

```bash
python run.py        # Start development server
flask db migrate     # Create migration
flask db upgrade     # Apply migration
```

---

## 🎯 Design Principles

- Clean modular architecture  
- Separation of concerns (auth, user, config, middleware)  
- Secure authentication by default  
- Minimal but scalable structure  
- Easy to extend for real-world applications  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch  
3. Follow Python & Flask best practices  
4. Submit a pull request  

---

## 👨‍💻 Author

Developed by **Arviixzuhs**

If this template helps you, consider leaving a ⭐ on the repository.
