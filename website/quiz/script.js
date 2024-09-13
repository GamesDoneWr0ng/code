let quizData = null

let selectedAnswer = null;
let currentQuestionIndex = 0;
let score = 0;

const questionCounter = document.querySelector(".question-counter");
const questionElement = document.querySelector(".question");
const answerOptions = document.querySelector(".answer-options");
const feedbackElement = document.querySelector(".feedback");
const submitButton = document.querySelector(".submit-btn");
const nextButton = document.querySelector(".next-btn");


fetch("questions.json")
    .then(response => response.json())
    .then(data => {
        quizData = data;
        loadQuestion();
        console.log(quizData)
    })
    .catch(error => {
        console.log("Error loading the JSON file:", error);
        questionElement.textContent = "Failed to load the quiz data."
    })

// load current question
function loadQuestion() {
    const currentQuestion = quizData.questions[currentQuestionIndex];

    questionElement.textContent = currentQuestion.question;
    questionCounter.textContent = "Question " + currentQuestionIndex + " of " + quizData.questions.length;

    answerOptions.innerHTML = '';
    currentQuestion.alternatives.forEach((alternative, index) => {
        const button = document.createElement("button");
        button.textContent = alternative;
        button.setAttribute("data-index", index);
        button.addEventListener("click", selectAnswer);
        answerOptions.appendChild(button)
    });

    feedbackElement.style.display = "none";
    submitButton.style.display = "block";
    nextButton.style.display = "none";
    selectedAnswer = null;
}

function selectAnswer(event) {
    const buttons = document.querySelectorAll(".answer-options button");
    buttons.forEach(button => button.classList.remove("selected"));
    event.target.classList.add("selected");
    selectedAnswer = event.target.textContent;
}

submitButton.addEventListener("click", () => {
    if (!selectedAnswer) return;

    const currentQuestion = quizData.questions[currentQuestionIndex];

    if (selectedAnswer === currentQuestion.answer) {
        feedbackElement.textContent = "Correct! " +currentQuestion.answer;
    } else {
        feedbackElement.textContent = "Incorrect! The correct answer is " + currentQuestion.answer;
    }

    feedbackElement.style.display = "block";
    nextButton.style.display = "block";
    submitButton.style.display = "none";
});

nextButton.addEventListener("click", () => {
    currentQuestionIndex++;

    if (currentQuestionIndex < quizData.questions.length) {
        selectedAnswer = null;
        loadQuestion();
    } else {
        quizCompleted();
    }
});

function quizCompleted() {
    questionElement.textContent = "Quiz Complete";
    answerOptions.innerHTML = "";
    feedbackElement.style.display = "none";
    submitButton.style.display = "none";
    nextButton.style.display = "none";
    questionCounter.style.display = "none";
}