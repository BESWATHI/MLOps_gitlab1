# Gitlab 01
A tiny Python project that implements a word_count function and tests it with both pytest and unittest. Includes a GitHub Actions workflow to run tests on every push.

# Project Structure
```
MLOps_gitlab1/
├─ .github/
│  └─ workflows/
│     ├─ pytest.yml            
│     └─ unittest.yml          
│
├─ src/
│  ├─ __init__.py
│  └─ main.py                 
│
├─ test/
│  ├─ __init__.py
│  ├─ test_pytest.py           # pytest tests
│  └─ test_unittest.py         # unittest tests
│           
│
├─ requirements.txt            # only: pytest
├─ README.md
└─ .venv                     

```


---

## ⚙️ Setup Instructions  

### 1️⃣ Create and Activate Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# OR (Windows)
.venv\Scripts\activate
```


## 2️⃣ Install Dependencies

```
pip install --upgrade pip
pip install -r requirements.txt

```

## 🧪 Running Tests Locally
```
pytest -v

```

## Run only pytest tests

```
pytest test/test_pytest.py -v
```
## Run only unittest tests
```
pytest test/test_unittest.py -v
```

## ✅ Expected Output

```
=================================== test session starts ===================================
platform darwin -- Python 3.12.2, pytest-8.4.2
collected 10 items

test/test_pytest.py::test_basic_sentence PASSED
test/test_pytest.py::test_case_insensitivity PASSED
test/test_pytest.py::test_punctuation_removal PASSED
test/test_pytest.py::test_empty_string PASSED
test/test_pytest.py::test_invalid_input_type PASSED
test/test_unittest.py::TestWordCount::test_basic_sentence PASSED
test/test_unittest.py::TestWordCount::test_case_insensitivity PASSED
test/test_unittest.py::TestWordCount::test_empty_string PASSED
test/test_unittest.py::TestWordCount::test_invalid_input_type PASSED
test/test_unittest.py::TestWordCount::test_punctuation_removal PASSED
==================================== 10 passed in 0.01 s ===================================
```

## ▶️ Run the Main Program
```
python src/main.py

```
## ✅ Expected Output
```
Input: Python is fun and Python is powerful!  
Word count: {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}
```

## 🔁 Continuous Integration (CI) — GitHub Actions

The project uses GitHub Actions to automatically run tests on every push or pull request to the main branch.

## Example Workflow — .github/workflows/pytest.yml

```
name: Testing with Pytest
run-name: "Pytest • ${{ github.ref_name }} • run ${{ github.run_number }}"

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest -v --junitxml=pytest-report.xml

      - name: Upload test report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: pytest-report.xml
```



