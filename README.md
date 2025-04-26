# 📊 Breast Cancer Prediction Model

This project builds a simple Machine Learning model using scikit-learn to predict whether a tumor is **Malignant** (cancerous) or **Benign** (non-cancerous) based on medical features.

---

## 🔧 Project Structure

```
.
├── data/
│   └── load_data.py
├── models/
│   └── model.py
├── utils/
│   └── preprocess.py
├── saved_models/
│   └── model.pkl
├── notebooks/
│   └── exploration.ipynb
├── main.py
├── README.md
```

---

## 🔍 How It Works

1. **Load Data:**
   - Use `sklearn.datasets.load_breast_cancer()` to fetch the dataset.
2. **Preprocess Data:**
   - Split into training and testing sets.
3. **Train Model:**
   - Train a Random Forest Classifier.
4. **Evaluate:**
   - Print a detailed classification report (Precision, Recall, F1-Score).
5. **Save Model:**
   - Save the trained model as a `.pkl` file for future use.

---

## 🔄 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/breast-cancer-prediction.git
cd breast-cancer-prediction
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

> Note: If there's no `requirements.txt`, manually install:
```bash
pip install scikit-learn pandas matplotlib seaborn
```

---

## 💪 Running the Project

```bash
python main.py
```

Output will show:
- Classification report.
- Saved model at `saved_models/model.pkl`

---

## 📊 Exploratory Data Analysis (EDA)

Check the `notebooks/exploration.ipynb` for:
- Distribution of classes.
- Correlation heatmaps of features.

---

## 🌐 Technologies Used
- Python 3.x
- scikit-learn
- pandas
- matplotlib
- seaborn

---

## 🚀 Future Improvements
- Hyperparameter tuning.
- Try other ML models like XGBoost.
- Deploy the model using a simple Flask or Streamlit app.

---

## 👤 Author
- [Your Name](https://github.com/your-username)

---

## 📢 License
This project is open source and available under the [MIT License](LICENSE).

