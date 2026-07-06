# 🍔 Food Delivery Time Prediction using Machine Learning

## 📌 Project Overview

Food delivery services rely on accurate delivery time estimation to improve customer satisfaction and optimize logistics. This project develops a Machine Learning model that predicts food delivery time based on factors such as delivery distance, weather conditions, traffic level, vehicle type, preparation time, and courier experience.

The project demonstrates the complete machine learning workflow, including data preprocessing, exploratory analysis, model training, evaluation, and prediction.

---

## 🎯 Objectives

- Predict food delivery time accurately.
- Analyze the impact of different delivery factors.
- Build a regression model using Machine Learning.
- Evaluate model performance using standard metrics.

---

## 📂 Project Structure

```
Food-Delivery-Time-Prediction/
│
├── data/
│   └── Food_Delivery_Times.csv
│
├── notebooks/
│   └── Food_Delivery_Time_Prediction.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── models/
│   └── model.pkl
│
├── images/
│   ├── actual_vs_predicted.png
│   ├── error_distribution.png
│   └── correlation_heatmap.png
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📊 Dataset Information

The dataset contains **1000 food delivery records** with different delivery conditions.

### Features

| Feature | Description |
|----------|-------------|
| Order_ID | Unique order identifier |
| Distance_km | Delivery distance in kilometers |
| Weather | Weather condition |
| Traffic_Level | Traffic congestion level |
| Time_of_Day | Morning, Afternoon, Evening, Night |
| Vehicle_Type | Bike, Scooter, Car |
| Preparation_Time_min | Food preparation time |
| Courier_Experience_yrs | Delivery partner experience |
| Delivery_Time_min | Target variable |

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

# 🧠 Machine Learning Workflow

```
Dataset Collection
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Train-Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Prediction
```

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Loaded dataset using Pandas
- Converted categorical variables using One-Hot Encoding
- Handled missing values
- Prepared feature matrix and target variable
- Split dataset into training and testing data

---

# 🤖 Machine Learning Model

**Algorithm Used**

- Linear Regression

The model was trained using Scikit-learn's Linear Regression algorithm.

---

# 📈 Model Evaluation

The following metrics were used:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

### Model Performance

| Metric | Value |
|---------|-------|
| MAE | 5.99 |
| RMSE | 8.93 |
| R² Score | 0.82 |

---

# 📊 Visualizations

The project includes the following visualizations:

- Actual vs Predicted Delivery Time
- Error Distribution
- Correlation Heatmap
- Feature Analysis

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/Food-Delivery-Time-Prediction.git
```

Go into the project directory.

```bash
cd Food-Delivery-Time-Prediction
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Train the model.

```bash
python src/train.py
```

Predict delivery time.

```bash
python src/predict.py
```






# 💡 Future Improvements

- Random Forest Regression
- XGBoost Regression
- LightGBM
- Hyperparameter Tuning
- Feature Selection
- Streamlit Web Application
- Flask REST API
- Docker Deployment
- Cloud Deployment (AWS/Render)

---

# 📚 Learning Outcomes

Through this project, I learned:

- Data Cleaning
- Feature Engineering
- Data Visualization
- Regression Algorithms
- Model Evaluation
- Machine Learning Workflow
- Python for Data Science
- Git & GitHub Project Management

---

# 👨‍💻 Author

**Vignesh Gadipally**

B.Tech – Computer Science Engineering (AI & ML)

SR University

GitHub: https://github.com/vigneshgadipally06-boop

LinkedIn: https://www.linkedin.com/in/vignesh-gadipally-a2a12833b/\

Mail-vigneshgadiaplly06@gmail.com

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support motivates me to build more Machine Learning projects.