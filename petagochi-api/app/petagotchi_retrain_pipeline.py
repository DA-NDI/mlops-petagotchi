from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor
from airflow.providers.amazon.aws.operators.sagemaker import SageMakerTrainingOperator
from airflow.utils.dates import days_ago
import json

#I hid id's

SKLEARNCONTAINERURI = "you sklearn container"
SAGEMAKERROLE = "..."
S3OUTPUTHPATH = "s3://your-bucket/output/""

# SageMaker Training Config
training_job_config = {
    "AlgorithmSpecification": {
        "TrainingImage": SKLEARNCONTAINERURI,  
        "TrainingInputMode": "File"
    },
    "RoleArn": SAGEMAKERROLE,  
    "OutputDataConfig": {
        "S3OutputPath": S3OUTPUTHPATH
    },
    "ResourceConfig": {
        "InstanceCount": 1,
        "InstanceType": "ml.m5.large",
        "VolumeSizeInGB": 5
    },
    "StoppingCondition": {
        "MaxRuntimeInSeconds": 1200
    },
    "InputDataConfig": [
        {
            "ChannelName": "training",
            "DataSource": {
                "S3DataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": S3OUTPUTHPATH,
                    "S3DataDistributionType": "FullyReplicated"
                }
            },
            "ContentType": "text/csv",
            "InputMode": "File"
        }
    ]
}

with DAG(
    dag_id="petagotchi_retrain_pipeline",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
) as dag:

    wait_for_new_data = S3KeySensor(
        task_id="wait_for_interactions_csv",
        bucket_key="data/interactions.csv",
        bucket_name="dag123-bucket", 
        poke_interval=60,
        timeout=3600
    )

    train_model = SageMakerTrainingOperator(
        task_id="train_petagotchi_model",
        config=training_job_config,
        aws_conn_id="aws_default",
        wait_for_completion=True
    )

    wait_for_new_data >> train_model
