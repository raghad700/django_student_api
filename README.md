# Student API Project

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Pip package manager

### Installation
```bash
git clone https://github.com/yourusername/django_student_api.git
cd django_student_api
pip install -r requirements.txt
```

### Running the Server
```bash
python manage.py runserver
```

## 📚 API Documentation

### Available Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome page |
| `/students/` | GET | Get all students |

### Sample Response
```json
[
    {
        "id": 1,
        "name": "رغد الجباوي",
        "age": 25,
        "major": "ذكاء اصطناعي"
    }
]
```

## 🧪 Testing the API
### Using Browser:
Visit `http://localhost:8000/students/`

### Using cURL:
```bash
curl http://localhost:8000/students/
```

