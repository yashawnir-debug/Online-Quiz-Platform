import streamlit as st
import random
import sqlite3
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import plotly.express as px
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Online Quiz Platform",
    page_icon="🧠",
    layout="wide"
)


# ============================================================
# DATABASE
# ============================================================

DB_NAME = "quiz_history.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS quiz_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            difficulty TEXT,
            score INTEGER,
            total_questions INTEGER,
            percentage REAL,
            correct INTEGER,
            created_at TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_quiz_result(category, difficulty, score, total_questions):

    percentage = (score / total_questions) * 100

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO quiz_history
        (
            category,
            difficulty,
            score,
            total_questions,
            percentage,
            correct,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        category,
        difficulty,
        score,
        total_questions,
        percentage,
        score,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def load_quiz_history():

    conn = sqlite3.connect(DB_NAME)

    try:
        df = pd.read_sql_query("""
            SELECT
                category AS Category,
                difficulty AS Difficulty,
                score AS Score,
                total_questions AS Questions,
                percentage AS Percentage,
                correct AS Correct,
                created_at AS Date
            FROM quiz_history
            ORDER BY created_at ASC
        """, conn)

    finally:
        conn.close()

    return df


init_db()


# ============================================================
# QUESTIONS
# ============================================================

questions = [

    # ========================================================
    # PYTHON - EASY
    # ========================================================

    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },

    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },

    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which data type is used to store True or False?",
        "options": ["String", "Integer", "Boolean", "Float"],
        "answer": "Boolean"
    },

    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which function is used to display output in Python?",
        "options": ["display()", "show()", "print()", "output()"],
        "answer": "print()"
    },

    {
        "category": "Python",
        "difficulty": "Easy",
        "question": "Which of these is a Python list?",
        "options": ["(1,2,3)", "[1,2,3]", "{1,2,3}", "<1,2,3>"],
        "answer": "[1,2,3]"
    },

    # ========================================================
    # PYTHON - MEDIUM
    # ========================================================

    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "Which method adds an element to the end of a list?",
        "options": ["add()", "insert()", "append()", "push()"],
        "answer": "append()"
    },

    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "What is the output of len([10, 20, 30])?",
        "options": ["2", "3", "10", "30"],
        "answer": "3"
    },

    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "Which collection stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary"
    },

    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "Which keyword is used to handle exceptions?",
        "options": ["try", "check", "error", "handle"],
        "answer": "try"
    },

    {
        "category": "Python",
        "difficulty": "Medium",
        "question": "Which function converts a string into an integer?",
        "options": ["str()", "float()", "int()", "number()"],
        "answer": "int()"
    },

    # ========================================================
    # PYTHON - HARD
    # ========================================================

    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "What programming concept occurs when a function calls itself?",
        "options": ["Iteration", "Recursion", "Inheritance", "Encapsulation"],
        "answer": "Recursion"
    },

    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "Which feature allows a class to inherit properties from another class?",
        "options": ["Inheritance", "Iteration", "Compilation", "Parsing"],
        "answer": "Inheritance"
    },

    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "Which Python feature is commonly used to create anonymous functions?",
        "options": ["lambda", "anonymous", "function", "def"],
        "answer": "lambda"
    },

    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "What does a decorator primarily modify?",
        "options": [
            "Function or class behavior",
            "Database tables",
            "Operating system",
            "Hardware"
        ],
        "answer": "Function or class behavior"
    },

    {
        "category": "Python",
        "difficulty": "Hard",
        "question": "Which data structure follows LIFO?",
        "options": ["Queue", "Stack", "Tree", "Graph"],
        "answer": "Stack"
    },

    # ========================================================
    # AI/ML - EASY
    # ========================================================

    {
        "category": "AI/ML",
        "difficulty": "Easy",
        "question": "What does AI stand for?",
        "options": [
            "Automated Internet",
            "Artificial Intelligence",
            "Advanced Information",
            "Artificial Integration"
        ],
        "answer": "Artificial Intelligence"
    },

    {
        "category": "AI/ML",
        "difficulty": "Easy",
        "question": "What does ML stand for?",
        "options": [
            "Machine Learning",
            "Modern Language",
            "Machine Logic",
            "Model Learning"
        ],
        "answer": "Machine Learning"
    },

    {
        "category": "AI/ML",
        "difficulty": "Easy",
        "question": "Which is an example of supervised learning?",
        "options": [
            "Classification",
            "Clustering",
            "Dimensionality reduction",
            "Association"
        ],
        "answer": "Classification"
    },

    {
        "category": "AI/ML",
        "difficulty": "Easy",
        "question": "Which technology allows computers to understand human language?",
        "options": ["NLP", "CPU", "RAM", "HTML"],
        "answer": "NLP"
    },

    {
        "category": "AI/ML",
        "difficulty": "Easy",
        "question": "Which is an example of AI?",
        "options": [
            "Voice assistant",
            "Calculator",
            "Keyboard",
            "USB cable"
        ],
        "answer": "Voice assistant"
    },

    # ========================================================
    # AI/ML - MEDIUM
    # ========================================================

    {
        "category": "AI/ML",
        "difficulty": "Medium",
        "question": "Which algorithm is commonly used for classification?",
        "options": [
            "Logistic Regression",
            "K-Means",
            "PCA",
            "Apriori"
        ],
        "answer": "Logistic Regression"
    },

    {
        "category": "AI/ML",
        "difficulty": "Medium",
        "question": "Which algorithm is used for clustering?",
        "options": [
            "Linear Regression",
            "K-Means",
            "Logistic Regression",
            "Decision Tree Regression"
        ],
        "answer": "K-Means"
    },

    {
        "category": "AI/ML",
        "difficulty": "Medium",
        "question": "What is overfitting?",
        "options": [
            "Model performs well only on training data",
            "Model has no data",
            "Model is too simple",
            "Model has no parameters"
        ],
        "answer": "Model performs well only on training data"
    },

    {
        "category": "AI/ML",
        "difficulty": "Medium",
        "question": "Which metric is commonly used for classification?",
        "options": [
            "Accuracy",
            "Mean Squared Error",
            "RMSE",
            "MAE"
        ],
        "answer": "Accuracy"
    },

    {
        "category": "AI/ML",
        "difficulty": "Medium",
        "question": "What is a feature in machine learning?",
        "options": [
            "Input variable",
            "Output only",
            "Error message",
            "Model name"
        ],
        "answer": "Input variable"
    },

    # ========================================================
    # AI/ML - HARD
    # ========================================================

    {
        "category": "AI/ML",
        "difficulty": "Hard",
        "question": "Which optimization algorithm is commonly used to train neural networks?",
        "options": [
            "Gradient Descent",
            "K-Means",
            "Apriori",
            "Random Forest"
        ],
        "answer": "Gradient Descent"
    },

    {
        "category": "AI/ML",
        "difficulty": "Hard",
        "question": "Which activation function is commonly used in hidden layers?",
        "options": ["ReLU", "CSV", "SQL", "HTML"],
        "answer": "ReLU"
    },

    {
        "category": "AI/ML",
        "difficulty": "Hard",
        "question": "What does CNN stand for?",
        "options": [
            "Convolutional Neural Network",
            "Computer Neural Node",
            "Central Network Node",
            "Connected Neural Network"
        ],
        "answer": "Convolutional Neural Network"
    },

    {
        "category": "AI/ML",
        "difficulty": "Hard",
        "question": "What does RNN stand for?",
        "options": [
            "Recursive Neural Network",
            "Recurrent Neural Network",
            "Random Neural Network",
            "Regression Neural Network"
        ],
        "answer": "Recurrent Neural Network"
    },

    {
        "category": "AI/ML",
        "difficulty": "Hard",
        "question": "Which technique helps reduce overfitting in neural networks?",
        "options": [
            "Dropout",
            "Sorting",
            "Compilation",
            "Parsing"
        ],
        "answer": "Dropout"
    },

    # ========================================================
    # DATA SCIENCE - EASY
    # ========================================================

    {
        "category": "Data Science",
        "difficulty": "Easy",
        "question": "Which Python library is mainly used for numerical computing?",
        "options": ["NumPy", "HTML", "Flask", "Django"],
        "answer": "NumPy"
    },

    {
        "category": "Data Science",
        "difficulty": "Easy",
        "question": "Which Python library is commonly used for data manipulation?",
        "options": ["Pandas", "TensorFlow", "Flask", "Requests"],
        "answer": "Pandas"
    },

    {
        "category": "Data Science",
        "difficulty": "Easy",
        "question": "Which library is commonly used for data visualization?",
        "options": ["Matplotlib", "NumPy", "OS", "Sys"],
        "answer": "Matplotlib"
    },

    {
        "category": "Data Science",
        "difficulty": "Easy",
        "question": "What is a dataset?",
        "options": [
            "Collection of data",
            "Programming language",
            "Computer hardware",
            "Operating system"
        ],
        "answer": "Collection of data"
    },

    {
        "category": "Data Science",
        "difficulty": "Easy",
        "question": "Which chart is useful for showing trends over time?",
        "options": ["Line chart", "Pie chart", "Histogram", "Box plot"],
        "answer": "Line chart"
    },

    # ========================================================
    # DATA SCIENCE - MEDIUM
    # ========================================================

    {
        "category": "Data Science",
        "difficulty": "Medium",
        "question": "Which technique is used to handle missing values?",
        "options": [
            "Imputation",
            "Compilation",
            "Encryption",
            "Rendering"
        ],
        "answer": "Imputation"
    },

    {
        "category": "Data Science",
        "difficulty": "Medium",
        "question": "Which measure represents the middle value of sorted data?",
        "options": ["Mean", "Median", "Mode", "Range"],
        "answer": "Median"
    },

    {
        "category": "Data Science",
        "difficulty": "Medium",
        "question": "Which chart is useful for visualizing the relationship between two numerical variables?",
        "options": [
            "Scatter plot",
            "Pie chart",
            "Histogram",
            "Bar chart"
        ],
        "answer": "Scatter plot"
    },

    {
        "category": "Data Science",
        "difficulty": "Medium",
        "question": "What does SQL stand for?",
        "options": [
            "Structured Query Language",
            "Simple Query Language",
            "System Query Logic",
            "Structured Question Language"
        ],
        "answer": "Structured Query Language"
    },

    {
        "category": "Data Science",
        "difficulty": "Medium",
        "question": "Which process removes incorrect or duplicate data?",
        "options": [
            "Data cleaning",
            "Data compiling",
            "Data rendering",
            "Data encryption"
        ],
        "answer": "Data cleaning"
    },

    # ========================================================
    # DATA SCIENCE - HARD
    # ========================================================

    {
        "category": "Data Science",
        "difficulty": "Hard",
        "question": "What is dimensionality reduction?",
        "options": [
            "Reducing the number of features",
            "Increasing dataset size",
            "Adding more rows",
            "Removing labels only"
        ],
        "answer": "Reducing the number of features"
    },

    {
        "category": "Data Science",
        "difficulty": "Hard",
        "question": "Which technique is commonly used for dimensionality reduction?",
        "options": [
            "PCA",
            "KNN",
            "Random Forest",
            "Naive Bayes"
        ],
        "answer": "PCA"
    },

    {
        "category": "Data Science",
        "difficulty": "Hard",
        "question": "What is correlation?",
        "options": [
            "Measure of relationship between variables",
            "Data deletion method",
            "Sorting technique",
            "Programming language"
        ],
        "answer": "Measure of relationship between variables"
    },

    {
        "category": "Data Science",
        "difficulty": "Hard",
        "question": "Which metric measures the average squared prediction error?",
        "options": [
            "MSE",
            "Accuracy",
            "Precision",
            "Recall"
        ],
        "answer": "MSE"
    },

    {
        "category": "Data Science",
        "difficulty": "Hard",
        "question": "What does normalization generally do?",
        "options": [
            "Scales values to a common range",
            "Deletes rows",
            "Adds labels",
            "Removes columns"
        ],
        "answer": "Scales values to a common range"
    },

    # ========================================================
    # GENERAL KNOWLEDGE - EASY
    # ========================================================

    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Chennai", "Kolkata"],
        "answer": "New Delhi"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "How many days are there in a week?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "Which is the largest ocean?",
        "options": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Pacific Ocean",
            "Arctic Ocean"
        ],
        "answer": "Pacific Ocean"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Easy",
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },

    # ========================================================
    # GENERAL KNOWLEDGE - MEDIUM
    # ========================================================

    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which is the largest continent?",
        "options": ["Africa", "Asia", "Europe", "Australia"],
        "answer": "Asia"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": [
            "Oxygen",
            "Nitrogen",
            "Carbon dioxide",
            "Hydrogen"
        ],
        "answer": "Nitrogen"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which is the longest river in India?",
        "options": ["Ganga", "Yamuna", "Godavari", "Krishna"],
        "answer": "Ganga"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "India", "Thailand"],
        "answer": "Japan"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Medium",
        "question": "Which is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },

    # ========================================================
    # GENERAL KNOWLEDGE - HARD
    # ========================================================

    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "Which is the deepest ocean trench?",
        "options": [
            "Mariana Trench",
            "Java Trench",
            "Tonga Trench",
            "Puerto Rico Trench"
        ],
        "answer": "Mariana Trench"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "Which element has the chemical symbol Au?",
        "options": ["Silver", "Gold", "Copper", "Iron"],
        "answer": "Gold"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "Which is the largest desert in the world?",
        "options": [
            "Sahara Desert",
            "Gobi Desert",
            "Antarctic Desert",
            "Arabian Desert"
        ],
        "answer": "Antarctic Desert"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "What is the approximate speed of light in vacuum?",
        "options": [
            "3 × 10⁸ m/s",
            "3 × 10⁶ m/s",
            "3 × 10⁴ m/s",
            "3 × 10² m/s"
        ],
        "answer": "3 × 10⁸ m/s"
    },

    {
        "category": "General Knowledge",
        "difficulty": "Hard",
        "question": "Which device connects different networks?",
        "options": [
            "Monitor",
            "Keyboard",
            "Router",
            "Printer"
        ],
        "answer": "Router"
    }
]


# ============================================================
# SESSION STATE
# ============================================================

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False

if "questions" not in st.session_state:
    st.session_state.questions = []

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "saved_result" not in st.session_state:
    st.session_state.saved_result = False

if "quiz_category" not in st.session_state:
    st.session_state.quiz_category = "All"

if "quiz_difficulty" not in st.session_state:
    st.session_state.quiz_difficulty = "All"

if "num_questions" not in st.session_state:
    st.session_state.num_questions = 5


# ============================================================
# HEADER
# ============================================================

st.title("🧠 Online Quiz Platform")

st.write(
    "Test your knowledge in Python, AI/ML, Data Science and General Knowledge."
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ Quiz Settings")

    category = st.selectbox(
        "📚 Select Category",
        [
            "All",
            "Python",
            "AI/ML",
            "Data Science",
            "General Knowledge"
        ]
    )

    difficulty = st.selectbox(
        "🔥 Select Difficulty",
        [
            "All",
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    number_of_questions = st.slider(
        "📝 Number of Questions",
        min_value=5,
        max_value=15,
        value=5
    )

    st.divider()

    st.info("⏱️ Quiz Time Limit: 60 seconds")


# ============================================================
# QUIZ START SCREEN
# ============================================================

if not st.session_state.quiz_started:

    st.subheader("🚀 Start Your Quiz")

    st.write(
        "Choose your quiz settings from the sidebar."
    )

    st.markdown("""
    ### Features

    ✅ Multiple categories  
    ✅ Multiple difficulty levels  
    ✅ Random questions  
    ✅ 60-second timer  
    ✅ Automatic scoring  
    ✅ Answer review  
    ✅ Quiz history  
    ✅ Statistics dashboard  
    """)

    if st.button(
        "▶️ Start Quiz",
        type="primary"
    ):

        filtered_questions = []

        for q in questions:

            category_match = (
                category == "All"
                or q["category"] == category
            )

            difficulty_match = (
                difficulty == "All"
                or q["difficulty"] == difficulty
            )

            if category_match and difficulty_match:
                filtered_questions.append(q)

        if len(filtered_questions) < number_of_questions:

            st.error(
                f"Only {len(filtered_questions)} questions are available "
                f"for the selected settings."
            )

        else:

            selected_questions = random.sample(
                filtered_questions,
                number_of_questions
            )

            st.session_state.questions = selected_questions

            st.session_state.answers = {}

            # IMPORTANT:
            # Save selected quiz settings
            st.session_state.quiz_category = category

            st.session_state.quiz_difficulty = difficulty

            st.session_state.num_questions = number_of_questions

            st.session_state.quiz_started = True

            st.session_state.quiz_finished = False

            st.session_state.start_time = datetime.now()

            st.session_state.saved_result = False

            st.rerun()


# ============================================================
# QUIZ PAGE
# ============================================================

if (
    st.session_state.quiz_started
    and not st.session_state.quiz_finished
):

    st.header("📝 Quiz")

    # --------------------------------------------------------
    # TIMER
    # --------------------------------------------------------

    elapsed_time = (
        datetime.now() - st.session_state.start_time
    ).total_seconds()

    remaining_time = max(
        0,
        60 - int(elapsed_time)
    )

    # Refresh every second
    st_autorefresh(
        interval=1000,
        key="quiz_timer"
    )

    minutes = remaining_time // 60
    seconds = remaining_time % 60

    if remaining_time <= 10:

        st.error(
            f"⏰ Time Remaining: {minutes:02d}:{seconds:02d}"
        )

    else:

        st.info(
            f"⏱️ Time Remaining: {minutes:02d}:{seconds:02d}"
        )

    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    total_questions = len(
        st.session_state.questions
    )

    answered_questions = len(
        st.session_state.answers
    )

    progress = (
        answered_questions / total_questions
    )

    st.progress(progress)

    st.write(
        f"Answered: {answered_questions}/{total_questions}"
    )

    st.divider()

    # --------------------------------------------------------
    # TIME EXPIRED
    # --------------------------------------------------------

    if remaining_time <= 0:

        st.warning(
            "⏰ Time is up! Your quiz is being submitted."
        )

        st.session_state.quiz_finished = True

        st.rerun()

    # --------------------------------------------------------
    # QUESTIONS
    # --------------------------------------------------------

    for index, q in enumerate(
        st.session_state.questions
    ):

        st.subheader(
            f"Question {index + 1}"
        )

        st.write(
            q["question"]
        )

        current_answer = st.session_state.answers.get(
            index,
            None
        )

        selected_answer = st.radio(
            "Select your answer:",
            q["options"],
            index=(
                q["options"].index(current_answer)
                if current_answer in q["options"]
                else None
            ),
            key=f"question_{index}"
        )

        if selected_answer:

            st.session_state.answers[index] = selected_answer

        st.divider()

    # --------------------------------------------------------
    # SUBMIT
    # --------------------------------------------------------

    if st.button(
        "✅ Submit Quiz",
        type="primary"
    ):

        st.session_state.quiz_finished = True

        st.rerun()


# ============================================================
# RESULT PAGE
# ============================================================

if (
    st.session_state.quiz_started
    and st.session_state.quiz_finished
):

    st.header("🎉 Quiz Result")

    total_questions = len(
        st.session_state.questions
    )

    score = 0

    for index, q in enumerate(
        st.session_state.questions
    ):

        user_answer = st.session_state.answers.get(
            index
        )

        if user_answer == q["answer"]:

            score += 1

    percentage = (
        score / total_questions
    ) * 100

    correct = score

    incorrect = (
        total_questions - score
    )

    # --------------------------------------------------------
    # SAVE RESULT
    # --------------------------------------------------------

    if not st.session_state.saved_result:

        saved_category = (
            st.session_state.quiz_category
        )

        saved_difficulty = (
            st.session_state.quiz_difficulty
        )

        if saved_category == "All":
            saved_category = "Mixed"

        if saved_difficulty == "All":
            saved_difficulty = "Mixed"

        save_quiz_result(
            saved_category,
            saved_difficulty,
            score,
            total_questions
        )

        st.session_state.saved_result = True

    # --------------------------------------------------------
    # RESULT METRICS
    # --------------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🏆 Score",
            f"{score}/{total_questions}"
        )

    with col2:

        st.metric(
            "📊 Percentage",
            f"{percentage:.0f}%"
        )

    with col3:

        st.metric(
            "✅ Correct",
            correct
        )

    with col4:

        st.metric(
            "❌ Incorrect",
            incorrect
        )

    st.divider()

    # --------------------------------------------------------
    # PERFORMANCE MESSAGE
    # --------------------------------------------------------

    if percentage >= 80:

        st.success(
            "🌟 Excellent! You have a strong understanding of the topic."
        )

    elif percentage >= 60:

        st.info(
            "👍 Good job! Keep practicing to improve further."
        )

    elif percentage >= 40:

        st.warning(
            "📚 Keep practicing. You are making progress!"
        )

    else:

        st.error(
            "💪 Don't give up! Review the answers and try again."
        )

    st.divider()

    # --------------------------------------------------------
    # ANSWER REVIEW
    # --------------------------------------------------------

    st.header("📋 Answer Review")

    for index, q in enumerate(
        st.session_state.questions
    ):

        user_answer = st.session_state.answers.get(
            index,
            "Not Answered"
        )

        st.subheader(
            f"Question {index + 1}"
        )

        st.write(
            q["question"]
        )

        if user_answer == q["answer"]:

            st.success(
                f"✅ Your Answer: {user_answer}"
            )

        else:

            st.error(
                f"❌ Your Answer: {user_answer}"
            )

            st.info(
                f"✅ Correct Answer: {q['answer']}"
            )

        st.divider()

    # --------------------------------------------------------
    # RETAKE
    # --------------------------------------------------------

    if st.button(
        "🔄 Take Another Quiz",
        type="primary"
    ):

        st.session_state.quiz_started = False

        st.session_state.quiz_finished = False

        st.session_state.questions = []

        st.session_state.answers = {}

        st.session_state.start_time = None

        st.session_state.saved_result = False

        st.session_state.quiz_category = "All"

        st.session_state.quiz_difficulty = "All"

        st.rerun()


# ============================================================
# STATISTICS DASHBOARD
# ============================================================

st.divider()

st.header("📊 Statistics Dashboard")

history_df = load_quiz_history()


if not history_df.empty:

    # --------------------------------------------------------
    # OVERALL STATISTICS
    # --------------------------------------------------------

    total_quizzes = len(history_df)

    best_score = history_df["Percentage"].max()

    average_score = history_df["Percentage"].mean()

    total_correct = history_df["Correct"].sum()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🎯 Total Quizzes",
            total_quizzes
        )

    with col2:

        st.metric(
            "🏆 Best Score",
            f"{best_score:.0f}%"
        )

    with col3:

        st.metric(
            "📊 Average Score",
            f"{average_score:.0f}%"
        )

    with col4:

        st.metric(
            "✅ Total Correct",
            int(total_correct)
        )

    st.divider()

    # --------------------------------------------------------
    # SCORE HISTORY
    # --------------------------------------------------------

    st.subheader("📈 Score History")

    score_df = history_df.copy()

    score_df = score_df.sort_values(
        "Date"
    ).reset_index(drop=True)

    score_df["Attempt"] = range(
        1,
        len(score_df) + 1
    )

    fig_score = px.line(
        score_df,
        x="Attempt",
        y="Percentage",
        markers=True,
        title="Quiz Score Progress"
    )

    fig_score.update_yaxes(
        range=[0, 100],
        title="Score (%)"
    )

    fig_score.update_xaxes(
        title="Quiz Attempt",
        dtick=1
    )

    st.plotly_chart(
        fig_score,
        use_container_width=True
    )

    # --------------------------------------------------------
    # CATEGORY PERFORMANCE
    # --------------------------------------------------------

    st.subheader("📚 Performance by Category")

    category_df = (
        history_df
        .groupby(
            "Category",
            as_index=False
        )["Percentage"]
        .mean()
    )

    category_df["Percentage"] = (
        category_df["Percentage"].round(2)
    )

    fig_category = px.bar(
        category_df,
        x="Category",
        y="Percentage",
        text="Percentage",
        title="Average Score by Category"
    )

    fig_category.update_yaxes(
        range=[0, 100],
        title="Average Score (%)"
    )

    fig_category.update_xaxes(
        title="Category"
    )

    fig_category.update_traces(
        texttemplate="%{text:.0f}%",
        textposition="outside"
    )

    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

    # --------------------------------------------------------
    # DIFFICULTY PERFORMANCE
    # --------------------------------------------------------

    st.subheader("🔥 Performance by Difficulty")

    difficulty_df = (
        history_df
        .groupby(
            "Difficulty",
            as_index=False
        )["Percentage"]
        .mean()
    )

    difficulty_df["Percentage"] = (
        difficulty_df["Percentage"].round(2)
    )

    fig_difficulty = px.bar(
        difficulty_df,
        x="Difficulty",
        y="Percentage",
        text="Percentage",
        title="Average Score by Difficulty"
    )

    fig_difficulty.update_yaxes(
        range=[0, 100],
        title="Average Score (%)"
    )

    fig_difficulty.update_xaxes(
        title="Difficulty"
    )

    fig_difficulty.update_traces(
        texttemplate="%{text:.0f}%",
        textposition="outside"
    )

    st.plotly_chart(
        fig_difficulty,
        use_container_width=True
    )

    # --------------------------------------------------------
    # PREVIOUS ATTEMPTS
    # --------------------------------------------------------

    st.subheader("📋 Previous Attempts")

    table_df = history_df.copy()

    table_df["Score Display"] = (
        table_df["Score"].astype(str)
        + "/"
        + table_df["Questions"].astype(str)
    )

    table_df["Percentage Display"] = (
        table_df["Percentage"]
        .round(0)
        .astype(int)
        .astype(str)
        + "%"
    )

    table_df = table_df[
        [
            "Category",
            "Difficulty",
            "Score Display",
            "Percentage Display",
            "Questions",
            "Correct",
            "Date"
        ]
    ]

    table_df.columns = [
        "Category",
        "Difficulty",
        "Score",
        "Percentage",
        "Questions",
        "Correct",
        "Date"
    ]

    # FIXED:
    # Use table instead of dataframe
    st.table(table_df)

else:

    st.info(
        "Complete a quiz to generate statistics."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🧠 Online Quiz Platform | Built with Python, Streamlit, SQLite & Plotly"
)