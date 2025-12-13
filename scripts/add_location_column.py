import pandas as pd
import numpy as np
from pathlib import Path

INPUT_PATH = "data/v0/transactions_2022.csv"
OUTPUT_PATH = "data/v0/transactions_2022_with_location.csv"

def main():
    print(f"Loading dataset: {INPUT_PATH}")
    df = pd.read_csv(INPUT_PATH)

    # Add synthetic sensitive attribute
    np.random.seed(42)
    df["location"] = np.random.choice(["Location_A", "Location_B"], size=len(df))

    print("Added 'location' column.")

    Path("data/v0").mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved updated dataset with location: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
