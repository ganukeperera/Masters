import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def main():

    # Read and combine
    df = pd.read_csv("age_networth.csv")
    print(df.head())

    # Extract columns
    age = df["Age"]
    net_worth = df["Net Worth"]

    # Compute Pearson correlation
    corr, p_value = pearsonr(age, net_worth)

    print("Pearson Correlation:", corr)
    print("P-value:", p_value)

    
if __name__ == "__main__":
    main()