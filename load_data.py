
from sklearn.datasets import load_breast_cancer
import pandas as pd

def get_data():
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="target")
    return X, y
