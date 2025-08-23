from __future__ import annotations

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main() -> None:
    sales = pd.read_csv("sales.csv", parse_dates=["date"])
    sales["revenue"] = sales["units"] * sales["unit_price"]

    rev_by_region = (
        sales.groupby("region")["revenue"].sum().sort_values(ascending=False)
    )
    units_by_product = (
        sales.groupby("product")["units"].sum().sort_values(ascending=False)
    )

    print("Shape:", sales.shape)
    print("Revenue by region:\n", rev_by_region)
    print("Units by product:\n", units_by_product)

    # Charts
    plt.figure(figsize=(6, 4))
    sns.barplot(x=rev_by_region.index, y=rev_by_region.values, palette="viridis")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("revenue_by_region.png", dpi=160)
    plt.close()

    plt.figure(figsize=(6, 4))
    sns.barplot(
        x=units_by_product.index, y=units_by_product.values, palette="magma"
    )
    plt.title("Units Sold by Product")
    plt.xlabel("Product")
    plt.ylabel("Units")
    plt.tight_layout()
    plt.savefig("units_by_product.png", dpi=160)
    plt.close()


if __name__ == "__main__":
    main()

