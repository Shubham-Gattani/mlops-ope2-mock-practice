import os

# Define folder structure
folders = [
    "app",
    "data",
    "models",
    "scripts",
    ".github/workflows",
    "locust"
]

# Define files to create with optional initial content
files = {
    "app/main.py": "",
    "app/utils.py": "",
    "app/model.joblib": "",  # placeholder; real model will overwrite later
    "scripts/train.py": "",
    "scripts/poison_data.py": "",
    "scripts/add_location_column.py": "",
    "scripts/drift_detection.py": "",
    ".github/workflows/cd.yml": "",
    "locust/locustfile.py": "",
}

def create_structure():
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Create files
    for filepath, content in files.items():
        # Avoid overwriting existing files
        if not os.path.exists(filepath):
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Created file: {filepath}")
        else:
            print(f"Skipped (already exists): {filepath}")

    print("\nProject scaffolding completed successfully!")

if __name__ == "__main__":
    create_structure()
