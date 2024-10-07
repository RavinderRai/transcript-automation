from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import subprocess
import os
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(load_dotenv(find_dotenv()))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.clean_transcript import clean_transcript
from src.filter_transcript import filter_transcript
from src.categorize_transcript import categorize_transcripts
from src.summarize_transcript import summarize_transcripts

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 7),
    'retries': 1
}

dag = DAG(
    'transcript_automation',
    default_args=default_args,
    description='A DAG to automate trascript processing',
    schedule_interval='@daily'
)

def run_clean_transcript():
    clean_transcript(OPENAI_API_KEY=OPENAI_API_KEY)

def run_filter_transcript():
    filter_transcript(OPENAI_API_KEY=OPENAI_API_KEY)

def run_categorize_transcript():
    categorize_transcripts(OPENAI_API_KEY=OPENAI_API_KEY)

def run_summarize_transcript():
    summarize_transcripts(OPENAI_API_KEY=OPENAI_API_KEY)

clean_task = PythonOperator(
    task_id='clean_transcript',
    python_callable=run_clean_transcript,
    dag=dag
)

filter_task = PythonOperator(
    task_id='filter_transcript',
    python_callable=run_filter_transcript,
    dag=dag
)

categorize_task = PythonOperator(
    task_id = 'categorize_transcript',
    python_callable=run_categorize_transcript,
    dag=dag
)

summarize_task = PythonOperator(
    task_id='summarize_transcript',
    python_callable=run_summarize_transcript,
    dag=dag,
)

clean_task >> filter_task >> categorize_task >> summarize_task