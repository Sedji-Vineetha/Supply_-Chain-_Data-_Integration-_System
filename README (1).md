# Supply Chain Data Integration System

#  Supply Chain Analytics Dashboard

An interactive **Streamlit-based dashboard** to visualize and monitor **Supply Chain KPIs** using **Google BigQuery** as the data source.  
It provides insights into **lead time, order cycle time, inventory turnover, and on-time delivery rates**, along with **sales and inventory analysis** through charts.

---

##  Project Overview
This dashboard is designed to:
- Fetch **real-time data** from Google BigQuery
- Display **important supply chain metrics**
- Provide **visual analysis** of sales, inventory, and deliveries
- Help in **data-driven decision making**

It is ideal for supply chain managers, analysts, and businesses that want to **monitor performance in real-time**.

---

##  Tools & Technologies Used
- **Python**                           (Backend logic & data processing)
- **Streamlit**                        (Web application framework)
- **Google BigQuery**                  (Cloud database for data storage)
- **Pandas**                           (Data manipulation)
- **Plotly Express**                   (Interactive visualizations)
- **ngrok**                            (Expose dashboard to the web from Colab)
- **Google Cloud Service Account**     (Authentication)

---

##  File Structure
supply_chain_dashboard/
│
├── app.py                                  # Main Streamlit app
├── kpi.py                                  # KPI calculation functions
├── supplychaindata-5d6ab00d6911.json       # BigQuery service account key (DO NOT SHARE)
├── requirements.txt                        # List of dependencies
└── README.md                               # Project documentation

---

##  Features
1. **KPI Metrics**
   - Average Lead Time
   - Order Cycle Time
   - Inventory Turnover
   - On-Time Delivery %

2. **Sales Analysis**
   - Bar chart for Sales by Category
   - Pie chart for Order Share by Category

3. **Inventory Monitoring**
   - Bar chart of inventory levels
   - Low stock alerts

4. **Order Performance Tracking**
   - Delivery Time Trend (Line chart)
   - Recent Orders table

---

##  Setup & Installation

### **1️ Local Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/supply_chain_dashboard.git
   cd supply_chain_dashboard
2. Install dependencies:

        pip install -r requirements.txt
      
3. Set Google Cloud credentials:
 
       export GOOGLE_APPLICATION_CREDENTIALS="supplychaindata-5d6ab00d6911.json"

4. Run the dashboard:

       The dashboard will be available at: http://localhost:8501
    
2️ Running in Google Colab
1. Install dependencies:

       !pip install streamlit pandas plotly google-cloud-bigquery pyngrok -q
       Upload files:

2. Upload files:

       from google.colab import files
       files.upload()

3. Authenticate with Google Cloud:

       import os
       os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "supplychaindata-5d6ab00d6911.json"
       from google.cloud import bigquery
       client = bigquery.Client()
       print(" BigQuery authentication successful!")

4.  Add ngrok authentication token:
  
        !ngrok config add-authtoken YOUR_NGROK_TOKEN

5.   Run Streamlit in background:

         !nohup streamlit run app.py &>/dev/null &

6.  Get public URL:
   
        from pyngrok import ngrok
        print(ngrok.connect(8501))





❗ Troubleshooting
Ngrok Tunnel Errors → Make sure no other active ngrok sessions are running on the same account.

BigQuery Authentication Failed → Ensure your JSON key file path is correct and the project ID matches.

Port Already in Use → Change the port in the Streamlit command:

    streamlit run app.py --server.port 8502

    
 Author

Vineetha.S
Email: vineetha143sedje@gmail.com

