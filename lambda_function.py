import pandas as pd
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Hello this will work')
    return {
        'statusCode' : 200,
        'body': json.dumps('HelloWorld from python Lambda!')
    }