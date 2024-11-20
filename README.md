# Student Registration System

A full-stack web application built with Django REST Framework and React for managing student registrations. This application provides a complete CRUD (Create, Read, Update, Delete) interface for student records.

## Features

- Add new students with name, address, and fee information
- View list of all registered students
- Update existing student information
- Delete student records
- Responsive design with Bootstrap
- RESTful API backend

## Technology Stack

### Backend
- Django 4.2.16
- Django REST Framework
- SQLite Database
- Python 3.9+

### Frontend
- React
- Axios for API calls
- Bootstrap for styling
- JavaScript ES6+

## Project Structure

```
DwR/
├── SchoolProject/          # Django project directory
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── StudentApp/            # Django app directory
│   ├── models.py          # Student model
│   ├── serializers.py     # REST framework serializers
│   ├── views.py          # API views
│   └── ...
└── front-end/            # React frontend
    ├── src/
    │   ├── components/
    │   │   └── Student.jsx
    │   └── App.js
    └── public/
        └── index.html
```

## API Endpoints

- `GET /student/` - List all students
- `POST /student/` - Create a new student
- `GET /student/<id>/` - Retrieve a specific student
- `PUT /student/<id>/` - Update a specific student
- `DELETE /student/<id>/` - Delete a specific student

## Setup and Installation

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmed8047762/Student-Registration-with-DRF-and-React.git
   cd Student-Registration-with-DRF-and-React
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework django-cors-headers
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd front-end
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The application will be available at:
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

## Usage

1. Start both backend and frontend servers
2. Open http://localhost:3000 in your browser
3. Use the form to add new students
4. View all students in the table below
5. Use Edit and Delete buttons to modify existing records

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [Your Email]
Project Link: https://github.com/ahmed8047762/Student-Registration-with-DRF-and-React
