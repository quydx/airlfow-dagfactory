from pprint import pprint

from airflow.operators.python import PythonOperator

from airflow_dagfactory import load_yaml_dags

load_yaml_dags(globals_dict=globals(), suffix=['dag.yaml'])

pprint(globals())
