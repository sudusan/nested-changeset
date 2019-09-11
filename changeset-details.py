from __future__ import print_function

import json
import boto3
import os
import logging
          
logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Loading function')
cfnClient = boto3.client('cloudformation')
            
def lambda_handler(event, context):
    logger.info('Received event: ' + json.dumps(event, indent=2))
    # Get stack-name from the event
    stack_name = os.environ['STACK_NAME']
    changeset_name = os.environ['CHANGESET_NAME']
    logger.info('Stack Name is: ' + stack_name)
    logger.info('Changeset Name is: ' + changeset_name)

    try:
        # Call Describe Change Set
        response = cfnClient.describe_change_set(ChangeSetName=changeset_name, StackName=stack_name)
        # Log response from AWS CloudFormation
        logger.info("Response: " + json.dumps(response, indent=2))
        # Return the success message
        return 'Success'
    except Exception as e:
        logger.error(e)
        return str(e)