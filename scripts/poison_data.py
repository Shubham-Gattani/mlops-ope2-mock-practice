import pandas as pd
import numpy as np
from pathlib import Path

INPUT_PATH = "data/v0/transactions_2022.csv"
OUTPUT_DIR = "data/poisoned"

POISON_LEVELS = [2, 8, 20]  # percentages


def poison_dataset(df, percentage):
    df_poisoned = df.copy()
    class_0_idx = df_poisoned[df_poisoned["Class"] == 0].index

    n_to_flip = int(len(class_0_idx) * (percentage / 100))
    poisoned_idx = np.random.choice(class_0_idx, size=n_to_flip, replace=False)

    df_poisoned.loc[poisoned_idx, "Class"] = 1
    return df_poisoned


def main():
    Path(OUTPUT_DIR).mkdir(exist_ok=True, parents=True)

    print(f"Loading clean dataset: {INPUT_PATH}")
    df = pd.read_csv(INPUT_PATH)

    for pct in POISON_LEVELS:
        print(f"Poisoning {pct}% of class-0 data...")
        df_poisoned = poison_dataset(df, pct)

        out_path = f"{OUTPUT_DIR}/poisoned_{pct}_percent.csv"
        df_poisoned.to_csv(out_path, index=False)
        print(f"Saved: {out_path}")

    print("Poisoning complete.")


if __name__ == "__main__":
    main()
