import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from pathlib import Path

INPUT_PATH = "data/v0/transactions_2022.csv"
MODEL_OUTPUT_PATH = "models/model.joblib"

def load_data(path):
    print(f"Loading data from {path}")
    return pd.read_csv(path)

def train_model():
    df = load_data(INPUT_PATH)

    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=2000, class_weight="balanced")

    print("Training model...")
    model.fit(X_train, y_train)

    print("Evaluating model...")
    preds = model.predict(X_val)
    f1 = f1_score(y_val, preds)

    print(f"Validation F1-score: {f1:.4f}")

    # Save model
    Path("models").mkdir(exist_ok=True)
    joblib.dump(model, MODEL_OUTPUT_PATH)

    print(f"Model saved to {MODEL_OUTPUT_PATH}")

if __name__ == "__main__":
    train_model()
