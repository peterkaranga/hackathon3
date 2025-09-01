# hackathon3
AI Study Buddy – Flashcard Generator
https://img.shields.io/badge/AI-Powered-blue https://img.shields.io/badge/Backend-Flask-green https://img.shields.io/badge/Database-MySQL-orange https://img.shields.io/badge/Hosted-Netlify-cyan

AI Study Buddy is a web application that generates interactive flashcards from study notes using Artificial Intelligence. It solves the student pain point of manually creating study materials by automatically generating quiz questions and answers from provided text.

Features
🤖 AI-powered flashcard generation using Hugging Face API

🎨 Colorful, animated flashcards with flip animations

💾 MySQL database integration for storing and retrieving flashcards

📱 Responsive design that works on desktop and mobile devices

🎯 Simple, intuitive user interface

Tech Stack
Frontend: HTML5, CSS3, JavaScript

Backend: Python Flask

Database: MySQL

AI Integration: Hugging Face Question-Answering API

Deployment: Netlify (frontend), Heroku/Railway (backend)

Project Structure
text
ai-study-buddy/
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── database/
│   └── database_schema.sql
│
└── README.md
Installation & Setup
Prerequisites
Python 3.8+

MySQL Server

Hugging Face API account

Backend Setup
Clone the repository:

bash
git clone <repository-url>
cd ai-study-buddy/backend
Create a virtual environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
pip install -r requirements.txt
Set up environment variables:

bash
# Create .env file
echo DB_USER=root > .env
echo DB_PASSWORD=your_mysql_password >> .env
echo DB_HOST=localhost >> .env
echo DB_NAME=flashcard_db >> .env
echo HF_API_KEY=your_hugging_face_api_key >> .env
Set up the database:

bash
mysql -u root -p < ../database/database_schema.sql
Run the Flask application:

bash
python app.py
The backend will be running on http://localhost:5000.

Frontend Setup
Navigate to the frontend directory:

bash
cd ../frontend
For local development, you can use a simple HTTP server:

bash
# Python 3
python -m http.server 8000

# Or with Node.js
npx http-server
Open your browser and navigate to http://localhost:8000

Deployment
Frontend to Netlify
Build the frontend (if needed)

Connect your repository to Netlify

Set build directory to frontend/

Deploy

Backend to Heroku/Railway
Install Heroku CLI and login

Create a new Heroku app:

bash
heroku create your-app-name
Set environment variables:

bash
heroku config:set DB_USER=your_db_user
heroku config:set DB_PASSWORD=your_db_password
# Set other environment variables similarly
Deploy:

bash
git subtree push --prefix backend heroku main
Database Setup
For production, consider using a cloud database service like:

Amazon RDS

Google Cloud SQL

PlanetScale

Heroku Postgres (with appropriate changes to the code)

Usage
Open the application in your web browser

Paste your study notes into the text area

Select the number of flashcards to generate (1-10)

Click "Generate Flashcards"

Click on any flashcard to flip it and see the answer

Study with your AI-generated flashcards!

API Endpoints
POST /generate-flashcards - Generate flashcards from study notes

GET /get-flashcards - Retrieve stored flashcards from the database

Environment Variables
Variable	Description	Example
DB_USER	MySQL username	root
DB_PASSWORD	MySQL password	password123
DB_HOST	MySQL host	localhost
DB_NAME	Database name	flashcard_db
HF_API_KEY	Hugging Face API key	hf_xxxxxxxxxxxx
Customization
You can customize the application by:

Modifying the flashcard design in styles.css

Changing the AI model in app.py

Adjusting the database schema in database_schema.sql

Adding new features to the frontend JavaScript

Troubleshooting
Common Issues
Database connection errors: Check your MySQL credentials and ensure the database is running

Hugging Face API errors: Verify your API key and check your quota

CORS errors: Ensure the frontend URL is allowed in the Flask CORS configuration

Debug Mode
To enable debug mode, set FLASK_ENV=development before running the app:

bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
Contributing
Fork the repository

Create a feature branch: git checkout -b feature-name

Commit your changes: git commit -am 'Add new feature'

Push to the branch: git push origin feature-name

Submit a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Hugging Face for providing the AI API

Flask and MySQL communities for excellent documentation

Netlify for easy frontend hosting

Support
If you encounter any issues or have questions, please:

Check the troubleshooting section above

Search for existing issues in the GitHub repository

Create a new issue with detailed information about your problem
