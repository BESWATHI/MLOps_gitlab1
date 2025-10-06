# LAB1 - MLOps (IE-7374) 

This lab focuses on setting up a Python project for automated testing using Pytest and Unittest within a GitHub repository.
The core functionality implemented in this lab is a Word Counter program that counts the frequency of each word in a given sentence.



## Step 1: Creating a Virtual Environment
To create a virtual environment, follow these steps:

1. Open a Command Prompt or Terminal in the directory where you want to create your project.
2. Choose a name for your virtual environment (e.g "lab_01") and run the appropriate command:
    ```
    python -m venv lab_01
    ```
3. Activate the virtual environment
    ```
    lab01\Scripts\activate
    ```
After activation, you will see the virtual environment's name in your command prompt or terminal, indicating that you are working within the virtual environment.


### Step 2: Creating a GitHub Repository and Folder Structure
Once your environment is ready:

Create a GitHub repository (name it something like MLOps_Lab1).

Clone it locally.

Inside your repo, create the following structure:

Lab1/
├── data/
├── src/
│   └── main.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
├── workflows/
├── requirements.txt
└── README.md

### Step 3: Implementing the Word Counter in main.py

The main logic is implemented in src/main.py


### Step 4: Writing Tests with Pytest and Unittest
Using Pytest
test/test_pytest.py verifies the function using assert-based tests

Using Unittest
test/test_unittest.py checks the same logic with the unittest framework

### Step 5: Running the Tests

Make sure you’re inside the Lab1 directory before running tests.

Run Pytest
''' 
    pytest -v
'''    

Run Unittest
'''
    python -m unittest discover -s test -v
'''

### Step 6: Running the Program Manually

You can test your program directly with:
'''
    python src/main.py
'''    


