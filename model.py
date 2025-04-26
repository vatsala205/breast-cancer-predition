import os
import joblib
from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, path='saved_models/model.pkl'):
    # NEW: Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)

def load_model(path='saved_models/model.pkl'):
    return joblib.load(path)
