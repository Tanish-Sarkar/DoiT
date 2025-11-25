# DoiT Routes Summary

## Authentication
| URL | Method | Purpose |
|-----|--------|---------|
| `/login` | GET/POST | User login |
| `/register` | GET/POST | User registration |
| `/logout` | GET | User logout |

## Tasks
| URL | Method | Purpose |
|-----|--------|---------|
| `/` | GET | View all tasks |
| `/add` | POST | Create new task |
| `/toggle/<id>` | POST | Cycle task status |
| `/update/<id>` | GET/POST | Edit task title |
| `/delete/<id>` | POST | Delete task |
| `/clear_all` | POST | Delete all tasks |

## Flash Messages
- ✅ Success: Registration, Login, Task created/updated/deleted
- ❌ Danger: Invalid credentials, Duplicate user, Validation errors
- ℹ️ Info: Logout, Clear all tasks

## Authentication Required
All task routes (`/`, `/add`, `/toggle/<id>`, `/update/<id>`, `/delete/<id>`, `/clear_all`) require user to be logged in.
