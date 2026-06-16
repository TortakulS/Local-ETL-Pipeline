import pandas as pd


def transform_data(datas):
    print(datas.isnull().sum())
    datas = datas.dropna(subset=['Customer ID'])
    customer_purchase_count = (
        datas.groupby('Customer ID')['Order ID']
        .size()
        .reset_index(name="purchase_count")
    )
    
    total_price = (
        datas.groupby("Customer ID")["Total Sales"]
        .sum()
        .reset_index(name="total_price")
    )
    
    gender_purchase_count = (
    datas.groupby("Customer Gender")["Category"]
      .size()
      .reset_index(name="Gpurchase_count")
      .sort_values(
          ["Customer Gender", "Gpurchase_count"],
          ascending=[True, False]
      )
    )
    month = (
        datas.groupby("Purchase Date")
        .size()
        .reset_index(name="monthly_sales_count")
    )
    monthly_sales = month[month["Purchase Date"].dt.month == 6]
    
    return {
        "customer_purchase_count": customer_purchase_count,
        "total_price": total_price,
        "gender_purchase_count": gender_purchase_count,
        "monthly_sales": monthly_sales
    }


