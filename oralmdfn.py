import cx_Oracle
import boto3
from docutils.nodes import row

def lambda_handler(event, context):

    connection = cx_Oracle.connect("username/password@database-1.dinkjuhgle4rfn.us-east-1.rds.amazonaws.com:1521/orcl") # update your DB connection here
    cursor = connection.cursor()
    cursor.execute("select sysdate from DUAL")
    row = cursor.fetchone()
    print(row)

    return {
        "statusCode": 200,
        "body": context.invoked_function_arn
    }