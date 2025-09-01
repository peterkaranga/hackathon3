document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const studyNotes = document.getElementById('study-notes');
    const cardCount = document.getElementById('card-count');
    const flashcardsContainer = document.getElementById('flashcards-container');
    const loading = document.getElementById('loading');
    
    // Sample flashcard data for demonstration
    const sampleFlashcards = [
        { question: "What is the powerhouse of the cell?", answer: "Mitochondria" },
        { question: "What process converts light energy to chemical energy in plants?", answer: "Photosynthesis" },
        { question: "What is the basic unit of heredity?", answer: "Gene" },
        { question: "What is the name of the process by which cells divide?", answer: "Mitosis" },
        { question: "What is the largest organ in the human body?", answer: "Skin" }
    ];
    
    // Function to generate sample flashcards (simulates API response)
    function generateSampleFlashcards() {
        // Show loading animation
        loading.style.display = 'block';
        
        // Clear previous flashcards
        flashcardsContainer.innerHTML = '';
        
        // Simulate API delay
        setTimeout(() => {
            const count = parseInt(cardCount.value) || 5;
            
            // Create flashcards
            for (let i = 0; i < Math.min(count, sampleFlashcards.length); i++) {
                createFlashcard(sampleFlashcards[i].question, sampleFlashcards[i].answer, i+1);
            }
            
            // Hide loading animation
            loading.style.display = 'none';
        }, 1500);
    }
    
    // Function to create a flashcard element
    function createFlashcard(question, answer, number) {
        const flashcard = document.createElement('div');
        flashcard.className = 'flashcard';
        flashcard.innerHTML = `
            <div class="flashcard-inner">
                <div class="flashcard-front">
                    <div class="card-number">${number}</div>
                    <div class="question">${question}</div>
                    <p>Click to flip</p>
                </div>
                <div class="flashcard-back">
                    <div class="card-number">${number}</div>
                    <div class="answer">${answer}</div>
                    <p>Click to flip back</p>
                </div>
            </div>
        `;
        
        // Add flip functionality
        flashcard.addEventListener('click', function() {
            this.classList.toggle('flipped');
        });
        
        flashcardsContainer.appendChild(flashcard);
    }
    
    // Event listener for generate button
    generateBtn.addEventListener('click', function() {
        if (studyNotes.value.trim() === '') {
            alert('Please enter some study notes first!');
            return;
        }
        
        generateSampleFlashcards();
    });
    
    // Initialize with some sample text
    studyNotes.value = "The mitochondria are the powerhouse of the cell. Photosynthesis is the process used by plants to convert light energy into chemical energy. Genes are the basic unit of heredity. Mitosis is the process of cell division. The skin is the largest organ of the human body.";
});