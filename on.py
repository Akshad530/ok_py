import streamlit as st
import random

# Define MultiApp class to handle multi-page structure
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Sidebar for page navigation
        app = st.sidebar.selectbox('Choose a page', self.apps, format_func=lambda app: app['title'])
        app['function']()

# Home Page
def show_home_page():
    st.title("Welcome to Python Learning Portal!")
    st.write("This is a Python learning portal with multiple pages for Python information, examples, and quizzes.")
    st.write("Use the sidebar to navigate between the pages.")

# Python Overview Page
def show_python_overview():
    st.title("📘 Python Overview")
    st.write("Python is a high-level, interpreted programming language. It is known for its simplicity and readability.")

    st.subheader("Advantages of Python:")
    st.write("- Easy to learn and use")
    st.write("- Large supportive community")
    st.write("- Extensive libraries and frameworks")

    st.subheader("Common Uses of Python:")
    st.write("- Web development (Flask, Django)")
    st.write("- Data science (Pandas, NumPy, Matplotlib)")
    st.write("- Machine learning (Scikit-learn, TensorFlow)")

# Python Types Page
def show_python_types():
    st.title("🔢 Python Data Types")
    st.write("Python supports several built-in data types such as integers, strings, lists, tuples, dictionaries, and more.")

    st.subheader("1. Integer")
    st.write("An integer is a whole number, positive or negative.")
    st.code('x = 10  # Integer')

    st.subheader("2. String")
    st.write("A string is a sequence of characters.")
    st.code('name = "John"  # String')

    st.subheader("3. List")
    st.write("A list is an ordered collection of items which can be of different types.")
    st.code('my_list = [1, 2, 3, "Python", True]  # List')

    st.subheader("4. Tuple")
    st.write("A tuple is similar to a list, but it is immutable (cannot be changed after creation).")
    st.code('my_tuple = (1, 2, 3)  # Tuple')

    st.subheader("5. Dictionary")
    st.write("A dictionary is a collection of key-value pairs.")
    st.code('my_dict = {"name": "John", "age": 30}  # Dictionary')

# Python Examples Page
def show_python_examples():
    st.title("💻 Python Examples")
    st.write("Here are some simple Python examples demonstrating various concepts:")

    st.subheader("Example 1: Hello World")
    st.code('print("Hello, World!")')

    st.subheader("Example 2: Basic Calculation")
    st.code('x = 10\n y = 20\n print(x + y)')

    st.subheader("Example 3: Looping through a list")
    st.code('my_list = [1, 2, 3]\n for i in my_list:\n   print(i)')

# Python Quiz Page
def show_python_quiz():
    st.title("📝 Python Quiz")
    st.write("Test your knowledge of Python by answering the following questions.")
    
    questions = [
        {"question": "What data type is used to store whole numbers in Python?", "options": ["int", "str", "list", "dict"], "answer": "int"},
        {"question": "Which of these is a mutable data type in Python?", "options": ["tuple", "list", "string", "int"], "answer": "list"},
        {"question": "How do you define a function in Python?", "options": ["def function()", "function def()", "function()", "define function()"], "answer": "def function()"},
    ]
    
    score = 0
    for q in questions:
        st.subheader(q['question'])
        answer = st.radio("Choose your answer", q['options'])
        if answer == q['answer']:
            score += 1

    st.write(f"Your score: {score}/{len(questions)}")
    if score == len(questions):
        st.success("Excellent! You have great knowledge of Python.")
    elif score > 0:
        st.warning("Good job, but you can do even better!")
    else:
        st.error("Oops! Try again and improve your Python knowledge.")

# Create the MultiApp instance
app = MultiApp()

# Add pages to the app
app.add_app("Home", show_home_page)
app.add_app("Python Overview", show_python_overview)
app.add_app("Python Data Types", show_python_types)
app.add_app("Python Examples", show_python_examples)
app.add_app("Python Quiz", show_python_quiz)

# Run the app
if __name__ == "__main__":
    app.run()
