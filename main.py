
from data.load_data import get_data
from utils.preprocess import preprocess_data
from models.model import train_model, save_model
from sklearn.metrics import classification_report

def main():
    X, y = get_data()
    X_train, X_test, y_train, y_test = preprocess_data(X, y) #preprocess data also called splitting the data
    model = train_model(X_train, y_train)  #training the RandomForestClassifier
    y_pred = model.predict(X_test)  #predicting
    print(classification_report(y_test, y_pred)) #evaluating
    save_model(model)

if __name__ == "__main__":
    main()
