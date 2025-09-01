from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database configuration
db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'flashcard_db')
}

# Hugging Face API configuration
HF_API_KEY = os.getenv('HF_API_KEY')
HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query_huggingface(payload):
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-flashcards', methods=['POST'])
def generate_flashcards():
    data = request.json
    notes = data.get('notes', '')
    count = data.get('count', 5)
    
    if not notes:
        return jsonify({'error': 'No notes provided'}), 400
    
    # Generate prompt for Hugging Face
    prompt = f"Generate {count} quiz questions with answers based on the following text: {notes}"
    
    try:
        # Call Hugging Face API
        output = query_huggingface({
            "inputs": prompt,
            "parameters": {
                "max_length": 512,
                "temperature": 0.7
            }
        })
        
        # Process the response and extract questions and answers
        flashcards = process_hf_response(output)
        
        # Save to database
        save_to_database(notes, flashcards)
        
        return jsonify({'flashcards': flashcards})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_hf_response(response):
    # This function would need to be implemented based on the actual response format
    # from the Hugging Face model
    flashcards = []
    # Placeholder implementation
    if isinstance(response, list) and len(response) > 0:
        # Extract text from response
        text = response[0].get('generated_text', '')
        
        # Simple parsing logic - this would need to be more sophisticated
        lines = text.split('\n')
        for line in lines:
            if '?' in line and ':' in line:
                parts = line.split(':', 1)
                if len(parts) == 2:
                    flashcards.append({
                        'question': parts[0].strip(),
                        'answer': parts[1].strip()
                    })
    
    # Fallback to sample data if parsing fails
    if not flashcards:
        flashcards = [
            {'question': 'What is the powerhouse of the cell?', 'answer': 'Mitochondria'},
            {'question': 'What process converts light energy to chemical energy?', 'answer': 'Photosynthesis'}
        ]
    
    return flashcards

def save_to_database(notes, flashcards):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS study_sessions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flashcards (
                id INT AUTO_INCREMENT PRIMARY KEY,
                session_id INT,
                question TEXT,
                answer TEXT,
                FOREIGN KEY (session_id) REFERENCES study_sessions(id)
            )
        ''')
        
        # Insert study session
        cursor.execute('INSERT INTO study_sessions (notes) VALUES (%s)', (notes,))
        session_id = cursor.lastrowid
        
        # Insert flashcards
        for card in flashcards:
            cursor.execute(
                'INSERT INTO flashcards (session_id, question, answer) VALUES (%s, %s, %s)',
                (session_id, card['question'], card['answer'])
            )
        
        connection.commit()
        cursor.close()
        connection.close()
        
    except Exception as e:
        print(f"Database error: {e}")

@app.route('/get-flashcards', methods=['GET'])
def get_flashcards():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute('''
            SELECT s.id, s.created_at, f.question, f.answer 
            FROM study_sessions s
            JOIN flashcards f ON s.id = f.session_id
            ORDER BY s.created_at DESC, f.id
        ''')
        
        results = cursor.fetchall()
        
        # Group flashcards by session
        sessions = {}
        for row in results:
            session_id = row['id']
            if session_id not in sessions:
                sessions[session_id] = {
                    'date': row['created_at'],
                    'flashcards': []
                }
            sessions[session_id]['flashcards'].append({
                'question': row['question'],
                'answer': row['answer']
            })
        
        cursor.close()
        connection.close()
        
        return jsonify({'sessions': sessions})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)