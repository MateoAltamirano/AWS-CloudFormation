#!/usr/bin/python3
import getopt, sys

argument_list = sys.argv[1:]
short_options = "cdus"
long_options = ["create", "delete", "update", "set"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
    command = arguments[0][0]
except getopt.error as err:
    print (str(err))
    sys.exit(2)
    
################################################################################
import boto3
PROJECT = 'AWS-CloudFormation'
cloudformation = boto3.client('cloudformation')

with open('template.yaml','r') as file:
    template = file.read()
if command in ('--create','-c'):
    response = cloudformation.create_stack(
        StackName=PROJECT,
        TemplateBody=template
    )
    print(response)
elif command in ("--update", "-u"):

    response = cloudformation.update_stack(
        StackName=PROJECT,
        TemplateBody=template
    )
    print(response)

elif command in ("--delete", "-d"):
    response = cloudformation.delete_stack(
        StackName=PROJECT
    )
    print(response)