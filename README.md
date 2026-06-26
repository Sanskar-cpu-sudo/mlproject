# 🎓 Student Performance Prediction

An End-to-End Machine Learning project that predicts a student's mathematics score based on demographic and educational attributes. The project follows an industry-standard ML pipeline including data ingestion, preprocessing, model training, prediction, and deployment using Flask.

---

## 🚀 Features

- Complete End-to-End ML Pipeline
- Data Ingestion
- Data Transformation
- Model Training
- Model Evaluation
- Prediction Pipeline
- Flask Web Application
- Custom Exception Handling
- Logging
- Reusable Utility Functions
- Modular Project Structure

---

## 🛠️ Tech Stack

### Programming Language
- Python 3

### Machine Learning
- Scikit-Learn
- CatBoost
- XGBoost
- Random Forest
- Decision Tree
- Linear Regression
- AdaBoost

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Dill

### Web Framework
- Flask

### Development Tools
- Git
- GitHub
- VS Code

---

# 📂 Project Structure

```
mlproject/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   ├── test.csv
│   └── data.csv
│
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── app.py
├── setup.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Dataset

The project uses the **Student Performance Dataset** containing information such as:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

The model predicts the student's **Mathematics Score**.

---

# ⚙️ Machine Learning Workflow

```
Student Dataset
       │
       ▼
Data Ingestion
       │
       ▼
Data Transformation
       │
       ▼
Feature Engineering
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Best Model Saved
       │
       ▼
Prediction Pipeline
       │
       ▼
Flask Web Application
```

---

# 🧠 Models Used

The following regression models are trained and compared:

- Linear Regression
- Lasso Regression
- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- XGBoost Regressor
- CatBoost Regressor

The best-performing model is automatically selected and saved.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Sanskar-cpu-sudo/mlproject.git
```

Move into the project

```bash
cd mlproject
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install all dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Flask server

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# 📸 Web Application

The application allows users to enter:

- Gender
- Race/Ethnicity
- Parental Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

After submission, the trained model predicts the student's **Mathematics Score**.

---

# 📦 Requirements

Install all required packages using

```bash
pip install -r requirements.txt
```

---

# 📁 Important Files

| File | Description |
|------|-------------|
| app.py | Flask application |
| requirements.txt | Project dependencies |
| setup.py | Package configuration |
| logger.py | Logging utility |
| exception.py | Custom exception handling |
| utils.py | Helper functions |

---

# 📚 Learning Outcomes

This project demonstrates:

- End-to-End Machine Learning Pipeline
- Modular Code Structure
- Object-Oriented Programming
- Feature Engineering
- Model Selection
- Hyperparameter Evaluation
- Pipeline Serialization
- Logging
- Exception Handling
- Flask Deployment
- Production-Level Project Structure

---



---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
