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

    print("\n===== CHECKING FOR NULL VALUES =====")
    print(combined_df["PM2.5"].isnull().sum())
    print(combined_df["PM10"].isnull().sum())

    print("\n===== REPLACING NULL VALUES =====")
    # Make sure data is sorted by time first!
    combined_df = combined_df.sort_values(by=["year", "month", "day", "hour"])

    # Interpolate (main method)
    combined_df["PM2.5"] = combined_df["PM2.5"].interpolate(method="linear")
    combined_df["PM10"] = combined_df["PM10"].interpolate(method="linear")

    # Handle edge cases (start/end gaps)
    combined_df["PM2.5"] = combined_df["PM2.5"].bfill().ffill()
    combined_df["PM10"] = combined_df["PM10"].bfill().ffill()

    print("\n===== CHECKING FOR NULL VALUES AFTER REPLACING =====")
    print(combined_df["PM2.5"].isnull().sum())
    print(combined_df["PM10"].isnull().sum())

    # Task 3
    print("PM2.5 Mean :", combined_df["PM2.5"].mean())
    print("PM2.5 Median :", combined_df["PM2.5"].median())
    print("PM2.5 Min :", combined_df["PM2.5"].min())
    print("PM2.5 Max :", combined_df["PM2.5"].max())
    print("PM2.5 Standard Deviation :", combined_df["PM2.5"].std())

    # Task 4
    ## Need to catch outliers, Also need to check for data duplication
    avg_by_station = combined_df.groupby("station")["PM2.5"].mean()
    print(avg_by_station)

    # Task 5
    # Histogram of PM2.5
    plt.figure(figsize=(6,4))
    combined_df["PM2.5"].hist(bins=1000)

    plt.title("Histogram of PM2.5")
    plt.xlabel("PM2.5 Level")
    plt.ylabel("Frequency")
    plt.show()

    

if __name__ == "__main__":
    main()