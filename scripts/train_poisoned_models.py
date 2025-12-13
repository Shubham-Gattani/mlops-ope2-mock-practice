import pandas as pd
import joblib
import mlflow
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

POISONED_DIR = "data/poisoned"
MODEL_DIR = "models/poisoned_models"

import mlflow
mlflow.set_tracking_uri("http://127.0.0.1:8100")
mlflow.set_experiment("poisoning_experiments")



def train_model(path, poisoning_level):
    df = pd.read_csv(path)
    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    model = LogisticRegression(max_iter=2000, class_weight="balanced")
    model.fit(X_train, y_train)

    preds = model.predict(X_val)
    f1 = f1_score(y_val, preds)

    # MLflow logging
    mlflow.log_param("poisoning_level", poisoning_level)
    mlflow.log_metric("f1_score", f1)

    # Save model
    Path(MODEL_DIR).mkdir(exist_ok=True, parents=True)
    model_path = f"{MODEL_DIR}/model_poisoned_{poisoning_level}.joblib"
    joblib.dump(model, model_path)

    mlflow.log_artifact(model_path)

    print(f"[{poisoning_level}%] F1-score = {f1:.4f}")


def main():
    mlflow.set_experiment("poisoning_experiments")

    poisoning_levels = [2, 8, 20]

    for pct in poisoning_levels:
        file_path = f"{POISONED_DIR}/poisoned_{pct}_percent.csv"
        with mlflow.start_run(run_name=f"poison_{pct}_percent"):
            train_model(file_path, pct)


if __name__ == "__main__":
    main()
