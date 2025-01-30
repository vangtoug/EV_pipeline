import os #add access to operating system modules

from airflow import models #import models functionality from airflow
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator #import airflow operator for transfers from GCS to BQ
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator #import airflow functionality for BQ dataset manipulation
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator #import standard BQ job functions for airflow
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator




from airflow.utils.dates import days_ago #Used for scheduling

DATASET_NAME = os.environ.get("GCP_DATASET_NAME", 'electric_vehicle_dataset') #specify the dataset name you want created in BQ
TABLE_NAME = os.environ.get("GCP_TABLE_NAME", 'ev_dim') #specify the table name you want created in the BQ dataset



#define and name the DAG
dag = models.DAG(
    dag_id='ev_dim',
    start_date=days_ago(1),
    schedule_interval=None, #manually triggered dag
    tags=['ev_dim'],

    )
#Task 1 to create dataset
create_test_dataset = BigQueryCreateEmptyDatasetOperator(
    task_id='extract_csv_dataset', dataset_id=DATASET_NAME, dag=dag
)
#Task 2 to read source file and populate table in BQ
load_csv = GCSToBigQueryOperator(
    task_id='load_to_BQ',
    bucket='t_e_s_t_123', #name of bucket where source data resides
    source_objects=['ElectricVehicleData.csv'], #name of the file to read (include any folders in name if they exist)
    destination_project_dataset_table=f"{DATASET_NAME}.{TABLE_NAME}",
    schema_fields=[
        {'name': 'VIN', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'county', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'state', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'postal code', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'model year', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'make', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'model', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'electric vehicle type', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'clean alternative fuel vehicle eligibility', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'electric range', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'base msrp', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'legislative district', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'dol vehicle ID', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'vehicle location', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'electric utility', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': '2020 census tract', 'type': 'STRING', 'mode': 'NULLABLE'},



    ],
    skip_leading_rows=1, #tells airflow that row 1 has the column names and should be skipped
    write_disposition='WRITE_TRUNCATE',
    dag=dag,
)

    #Task sequence
    create_test_dataset >> load_csv