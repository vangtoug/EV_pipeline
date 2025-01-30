# EV_pipeline

**- This is an initial project for creating a data pipeline using a publicly found dataset (https://catalog.data.gov/dataset/electric-vehicle-population-data).**

**- The purpose of ths project is to see and understand the flow of how raw data is taken, extracted, loaded, transformed, and presented into a dashboard that can then be used to make futture business decisions.**

**- The project entails the flow of an ELT data pipeline doing the following:**
- Find large dataset; in this case in the form of a csv file
- Take large dataset and load into Google Cloud Storage bucket
- Extract the data utilizing Apache Airflow with a Python DAG in VS (Visual Studio) Code
- Load respective DAG in to Google Composer; test and verify, then load correct data into Google BigQuery
- Transformation using DBT Cloud models that are published/built to Google BigQuery
- Finally, the transformed data is then visualized in Power Bi

**- Lessons learned and future plans:**
- Finding and giving the right grants and accesses so that these programs can all work together seamlessly; took longer than expected
- Use multiple datasets that are similar and joining them in an ELT or ETL data pipeline
- Using cloud apps vs loaded local apps has advantages/disadvantages; eg. using DBT Cloud vs. DBT Core
- In future projects, work towards getting DAG query to run DBT model tasks; ETL vs. ELT
- Use other types of open source database tools and apps 

**Data Pipeline Flow Chart**

![Data Pipeline Flow Chart](EV-ELT-pipeline-flow-chart.png)

**Airflow Chart**
![Airflow Chart](Airflow-Composer-EV-ELT-pipeline.png)

**BigQuery Project View**
![BigQuery Project View](BigQuery-EV-ELT-pipeline.png)

**Visuals in Power Bi**
![Visuals in Power Bi](PowerBi-EV-ELT-visual.png)




