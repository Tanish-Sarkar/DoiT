# DoiT – A Simple Task Management App

**DoiT** is a lightweight, full-stack web application built with Flask that lets users create accounts, register, log in securely, and manage their daily tasks efficiently. Track task progress through multiple states and organize your workflow with ease.

---

## 🎯 Features

- **User Authentication**
  - Secure user registration with email and username
  - Password hashing using Werkzeug security
  - User login/logout with session management

- **Task Management**
  - Create new tasks with a single click
  - Edit task titles on-the-fly
  - Delete individual tasks with confirmation
  - Cycle through task statuses: **Pending** → **Working** → **Done**
  - Visual status badges (color-coded)

- **Responsive Design**
  - Clean, modern UI with gradient headers
  - Mobile-friendly layout
  - Interactive action buttons with tooltips
  - Real-time flash messages for user feedback

- **Database-Backed**
  - SQLAlchemy ORM with SQLite
  - User and Task models with proper relationships
  - Persistent data storage

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or download the project:**
   ```bash
   cd DoiT
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   & ".\venv\Scripts\Activate.ps1"
   
   # Windows (Command Prompt)
   python -m venv venv
   venv\Scripts\activate.bat
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python run.py
   ```

5. **Open your browser:**
   - Navigate to `http://127.0.0.1:5000`
   - You'll be redirected to the login page

---

## 📋 Usage

### Creating an Account
1. Click **Login** in the navigation
2. Look for a registration link on the login page
3. Fill in your **username**, **email** (optional), and **password**
4. Confirm your password and click **Register**
5. You'll be redirected to login; use your new credentials

### Logging In
1. Enter your username and password
2. Click **Login**
3. You'll be taken to your task dashboard

### Managing Tasks
1. **Add a Task:** Type in the input field and click **Add**
2. **View Status:** See task status badges (Pending, Working, Done)
3. **Change Status:** Click the **▶ (Next)** button to cycle to the next status
4. **Edit a Task:** Click the **✎ (Edit)** button to update the title
5. **Delete a Task:** Click the **✕ (Delete)** button (with confirmation)
6. **Clear All:** Use the "Clear All Tasks" button to remove all tasks at once

---

## 🏗️ Project Structure

```
DoiT/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── models.py             # User and Task models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py           # Login, Register, Logout routes
│   │   └── tasks.py          # Task CRUD routes
│   ├── static/
│   │   └── css/
│   │       └── style.css     # Main stylesheet
│   └── templates/
│       ├── base.html         # Base template with header/footer
│       ├── login.html        # Login page
│       ├── register.html     # Registration page
│       ├── tasks.html        # Task dashboard
│       └── update_task.html  # Edit task form
├── instance/                 # Database storage
├── run.py                    # Application entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🔧 Configuration

Edit `app/__init__.py` to customize:

```python
app.config['SECRET_KEY'] = "your-secret-key"  # Change for production
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///doit.db"  # Database path
```

### For Production:
- Change `SECRET_KEY` to a strong random string
- Set `app.run(debug=False)` in `run.py`
- Use a production database (PostgreSQL, MySQL)
- Deploy with Gunicorn or similar WSGI server

---

## 🗄️ Database Models

### User Model
```python
- id (Integer, Primary Key)
- username (String, Unique)
- email (String, Unique, Optional)
- password_hash (String)
```

### Task Model
```python
- id (Integer, Primary Key)
- title (String)
- status (String) # Default: "Pending"
```

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.1.2 | Web framework |
| Flask-SQLAlchemy | 3.1.1 | ORM for database |
| Werkzeug | 3.1.3 | Security (password hashing) |
| Flask-WTF | 1.2.2 | Forms & CSRF protection |
| python-dotenv | 1.2.1 | Environment variables |

---

## 🎨 Styling

The app uses a custom CSS stylesheet with:
- **Color scheme:** Blue gradient header, light background
- **Responsive design:** Mobile-friendly layouts
- **Status badges:** Color-coded task states
- **Action buttons:** Icon-based controls with hover effects

### Main Style Features:
- Clean, minimalist design
- Smooth transitions and animations
- Focus states for accessibility
- Mobile breakpoints

---

## 🔐 Security Notes

- Passwords are hashed using Werkzeug's `generate_password_hash`
- User sessions are managed via Flask sessions
- CSRF protection available via Flask-WTF
- **TODO:** Add email validation and password strength requirements

---

## 🚧 Future Enhancements

- [ ] Due dates for tasks
- [ ] Task categories/tags
- [ ] Email verification on registration
- [ ] Password reset functionality
- [ ] Task sharing between users
- [ ] Dark mode toggle
- [ ] REST API endpoints
- [ ] Automated testing suite

---

## 💡 Tips & Tricks

- **Delete confirmation:** A confirmation dialog prevents accidental deletions
- **Status cycling:** Use the Next button to quickly iterate through task states
- **Responsive:** Works great on mobile devices
- **Flash messages:** Watch for success/error messages after each action

---

## 🐛 Troubleshooting

**Database not initializing?**
- Delete `instance/doit.db` and restart the app

**Port 5000 already in use?**
- Change in `run.py`: `app.run(debug=True, port=5001)`

**Module import errors?**
- Ensure virtual environment is activated and dependencies are installed
- Run: `pip install -r requirements.txt`

---

## 📝 License

This project is open-source and available for personal and educational use.

---

## 👤 Author

**DoiT** is a learning project created to demonstrate full-stack Flask development with user authentication, database management, and responsive UI design.

---

## 🤝 Contributing

Feel free to fork, modify, and improve! Suggestions welcome.

---

**Happy task managing! 🎉**
