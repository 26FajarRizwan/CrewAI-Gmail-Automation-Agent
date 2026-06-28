import pandas as pd
import numpy as np

# 1. File load karein (Yahan apni file ka sahi naam likhen jo aapne upload ki hai)
# Agar file ka naam 'responses.csv' hai to wahi likhen
try:
    file_name = 'gaming_project.csv'  # <--- Is naam ko apni file se match karein
    df = pd.read_csv(file_name)

    print("--- STATISTICAL ANALYSIS REPORT ---\n")

    # Loop through each question (skipping the timestamp)
    for i, col in enumerate(df.columns[1:], 1):
        print(f"Question {i}: {col}")

        # Frequency: Kitne logon ne kya choose kiya
        counts = df[col].value_counts()
        print("Frequencies:\n", counts)

        # MODE: Sabse zyada select hone wala option
        mode_val = df[col].mode()[0]
        print(f"Mode (Common Trend): {mode_val}")

        # MEAN & Standard Deviation (Calculated by assigning numeric ranks 0,1,2,3)
        # Ye stats ke formulas hain jo CS students ke code mein zaroori hain
        codes = df[col].astype('category').cat.codes
        print(f"Mean Score: {codes.mean():.2f}")
        print(f"Standard Deviation: {codes.std():.2f}")

        print("-" * 50)

except Exception as e:
    print("Error: File nahi mili. Check karein ke file upload ho gayi hai aur naam sahi hai.")
    print(e)
