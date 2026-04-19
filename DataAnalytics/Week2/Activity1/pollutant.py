import pandas as pd
import glob
import matplotlib.pyplot as plt

def main():
    files = glob.glob("data/PRSA_Data*.csv")

    print("Files found:", files)

    # Read and combine
    df_list = [pd.read_csv(file) for file in files]
    combined_df = pd.concat(df_list, ignore_index=True)

    print("\n===== COMBINED DATA =====")
    print(combined_df.head())

    print("\n===== Data types =====") 
    print(combined_df.dtypes)

    print("\n===== Rows and Columns Count =====")
    print("Rows count :", combined_df.shape[0])
    print("Column count :", combined_df.shape[1])

    print("\n===== INFO =====")
    combined_df.info()

if __name__ == "__main__":
    main()