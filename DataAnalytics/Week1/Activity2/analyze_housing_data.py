import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("housing.csv")
    # print(df.head())
    # print(df.info())
    # print(df.describe())
    # df = pd.read_csv("housing.csv")
    conn = sqlite3.connect(":memory:")
    df.to_sql("housing", conn, index=False, if_exists="replace")
    print(df.corr(numeric_only=True)["price"].sort_values(ascending=False))
    print(df.groupby("furnishingstatus")["price"].mean())

    # df["price"].hist()
    # plt.title("Housing Price Distribution")
    # plt.show()

    # plt.scatter(df["area"], df["price"])
    # plt.xlabel("Area")
    # plt.ylabel("Price")
    # plt.title("Area vs Price")
    # plt.show()

    # df.groupby("furnishingstatus")["price"].mean().plot(kind="bar")
    # plt.title("Average Price by Furnishing Status")
    # plt.show()

    top = df.sort_values("price", ascending=False)

    print(top.head(5))

if __name__ == "__main__":
    main()