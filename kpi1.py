import pandas as pd

def calculate_lead_time(df):
    if "Ship Date" in df.columns and "Order Date" in df.columns:
        df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days
        return df["Lead Time"].mean()
    return 0

def calculate_order_cycle_time(df):
    if "Delivery Date" in df.columns and "Order Date" in df.columns:
        df["Cycle Time"] = (df["Delivery Date"] - df["Order Date"]).dt.days
        return df["Cycle Time"].mean()
    return 0

def calculate_inventory_turnover(df, inventory_df):
    if "Sales" in df.columns:
        total_sales = df["Sales"].sum()
        avg_inventory = inventory_df["inventory_level"].mean()
        return total_sales / avg_inventory if avg_inventory > 0 else 0
    return 0

def calculate_on_time_delivery(df):
    if "Delivery Date" in df.columns and "Expected Delivery Date" in df.columns:
        df["On Time"] = df["Delivery Date"] <= df["Expected Delivery Date"]
        return (df["On Time"].mean()) * 100
    return 0
