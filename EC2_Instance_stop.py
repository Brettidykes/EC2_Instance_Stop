import boto3  

def stop_all_running_instances():
    ec2 = boto3.client('ec2')  # Initialize EC2 client to interact with the EC2 service
    
    # Get all EC2 instances that are currently running
    running_instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]  # Filter to only get instances in 'running' state
    )
    
    # Initialize an empty list to hold the instance IDs of running instances
    instances_to_stop = [
        instance['InstanceId']  # Extract the 'InstanceId' for each instance
        for reservation in running_instances['Reservations']  # 'Reservations' contain the instances returned by EC2
        for instance in reservation['Instances']  # Loop through each instance in the 'Reservations'
    ]
    
    if instances_to_stop:
        # If there are running instances, stop them
        ec2.stop_instances(InstanceIds=instances_to_stop)  # Stop the instances by passing the list of instance IDs
        print(f"Stopping instances: {instances_to_stop}")  # Output the list of stopped instances for logging/debugging
    else:
        # If no instances are running, output that no action was taken
        print("No running instances found.")

# Lambda handler function - this is the entry point when the Lambda function is triggered
def lambda_handler(event, context):
    stop_all_running_instances()  # Call the function to stop all running instances
