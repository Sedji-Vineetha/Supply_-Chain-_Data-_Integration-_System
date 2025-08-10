import os
import streamlit as st
import pandas as pd
from google.cloud import bigquery
import plotly.express as px
from kpi import calculate_lead_time, calculate_order_cycle_time, calculate_inventory_turnover, calculate_on_time_delivery

# -------------------------------
# ✅ GOOGLE CLOUD AUTHENTICATION
# -------------------------------
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "supplychaindata-5d6ab00d6911.json"

# -------------------------------
# ✅ PROJECT CONFIGURATION
# -------------------------------
PROJECT_ID = "supplychaindata"

st.set_page_config(page_title="Supply Chain Dashboard", layout="wide")
st.title("📦 Supply Chain Data Integration Dashboard")
st.markdown("### Analyze supply chain performance with KPIs, charts, and insights")
st.markdown("---")

# -------------------------------
# ✅ FETCH DATA FROM BIGQUERY
# -------------------------------
client = bigquery.Client()
query = f"SELECT * FROM `{PROJECT_ID}.supply_chain_data.orders` LIMIT 1000"

try:
    orders_df = client.query(query).to_dataframe()
    st.success("✅ Data Loaded Successfully from BigQuery")
except Exception as e:
    st.error(f"❌ BigQuery Connection Failed: {e}")
    st.stop()

# Convert dates to datetime
date_cols = ["Order Date", "Ship Date", "Delivery Date", "Expected Delivery Date"]
for col in date_cols:
    orders_df[col] = pd.to_datetime(orders_df[col], errors="coerce")

# Dummy inventory data
inventory_df = pd.DataFrame({
    'product': ['Laptop', 'Chair', 'Desk', 'Monitor'],
    'inventory_level': [100, 50, 180, 70]
})

# -------------------------------
# ✅ CALCULATE KPIs
# -------------------------------
lead_time = round(calculate_lead_time(orders_df), 2)
cycle_time = round(calculate_order_cycle_time(orders_df), 2)
inventory_turnover = round(calculate_inventory_turnover(orders_df, inventory_df), 2)
on_time_rate = round(calculate_on_time_delivery(orders_df), 2)

# -------------------------------
# ✅ CREATE TABS
# -------------------------------
tab1, tab2, tab3 = st.tabs(["📊 KPIs & Overview", "📦 Inventory Analysis", "🚚 Order Performance"])

# -------------------------------
# ✅ TAB 1: KPIs + Sales Insights
# -------------------------------
with tab1:
    st.subheader("🔹 Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg Lead Time (Days)", lead_time)
    col2.metric("Avg Order Cycle (Days)", cycle_time)
    col3.metric("Inventory Turnover", inventory_turnover)
    col4.metric("On-Time Delivery (%)", on_time_rate)

    st.markdown("#### ✅ These KPIs help track supply chain efficiency and delivery reliability.")
    st.markdown("---")

    # 📊 BAR CHART - Sales by Category
    st.subheader("📊 Sales by Category")
    sales_bar = orders_df.groupby("Category")["Sales"].sum().reset_index()
    fig_bar = px.bar(sales_bar, x="Category", y="Sales", color="Category",
                     text_auto=".2s", height=500, width=1000)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.caption("✔ This bar chart shows which product categories generate the most revenue.")

    # 🥧 PIE CHART - Orders Share by Category
    st.subheader("🥧 Order Share by Category")
    order_pie = orders_df["Category"].value_counts().reset_index()
    order_pie.columns = ["Category", "Orders"]
    fig_pie = px.pie(order_pie, names="Category", values="Orders", hole=0.3,
                     color="Category", height=500, width=900)
    st.plotly_chart(fig_pie, use_container_width=True)
    st.caption("✔ This pie chart shows the proportion of total orders per product category.")

# -------------------------------
# ✅ TAB 2: INVENTORY ANALYSIS
# -------------------------------
with tab2:
    st.subheader("📦 Inventory Levels")
    fig_inv = px.bar(inventory_df, x="product", y="inventory_level", color="product",
                     text_auto=True, height=500, width=1000)
    st.plotly_chart(fig_inv, use_container_width=True)
    st.caption("✔ This chart highlights current stock levels per product.")

    # 🚨 ALERT for Low Inventory
    low_stock = inventory_df[inventory_df["inventory_level"] < 100]
    if not low_stock.empty:
        st.warning(f"⚠ Low Stock Alert: {', '.join(low_stock['product'])} have less than 100 units available.")
    else:
        st.success("✅ All products have sufficient stock.")

    st.markdown("#### ✅ Monitoring inventory levels ensures timely restocking and avoids stockouts.")

# -------------------------------
# ✅ TAB 3: ORDER PERFORMANCE
# -------------------------------
with tab3:
    st.subheader("📈 Delivery Time Trend")
    orders_df["Delivery Days"] = (orders_df["Delivery Date"] - orders_df["Order Date"]).dt.days
    trend_line = orders_df.groupby("Order Date")["Delivery Days"].mean().reset_index()
    fig_line = px.line(trend_line, x="Order Date", y="Delivery Days", markers=True,
                       height=500, width=1000)
    st.plotly_chart(fig_line, use_container_width=True)
    st.caption("✔ This line chart shows how delivery times have varied over time.")

    # 📋 Orders Data Table
    st.subheader("📋 Recent Orders")
    st.dataframe(orders_df.head(10))
    st.caption("✔ A sample of the latest orders for quick review.")
