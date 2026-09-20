# Sales Analytics Data Pipeline - AWS

End-to-end Data Engineering Pipeline for retail sales analysis using AWS & PySpark.

## 📊 Architecture
![Architecture](architecture.png)
Raw CSV -> AWS S3 (Raw Layer) -> AWS Glue (PySpark ETL) -> S3 (Processed) -> Athena / MySQL -> QuickSight Dashboard

## 🛠️ Tech Stack
- **Languages:** Python, PySpark, SQL
- **AWS Services:** S3, Lambda, Glue, Athena, QuickSight
- **Database:** MySQL
- **Tools:** Git, VS Code

## ⚙️ Pipeline Steps
1.  **Ingestion:** Uploaded raw sales CSV to S3 bucket `sales-raw-data`
2.  **ETL:** Created Glue Job with PySpark to clean, de-duplicate and transform data
3.  **Processing:** Stored transformed data in S3 `sales-processed-data` as Parquet
4.  **Querying:** Used Athena to query and validate data
5.  **Visualization:** Built QuickSight dashboard for KPIs - Total Sales, Region-wise Sales, Monthly Trends

## 📈 Dashboard Insights
- Total Sales by Region
- Top Selling Products
- Monthly Revenue Trend

## 🚀 How to Run
1. Clone repo
2. Configure AWS credentials
3. Run `glue_job.py`

## 🔗 Links
- LinkedIn:www.linkedin.com/in/gangiredlasriramakoti

Built by Sriramakoti - Aspiring Data Engineer
