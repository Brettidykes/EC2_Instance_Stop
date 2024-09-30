# EC2_Instance_Stop
Python script that stops all running EC2 instances.


# Stop Running EC2 Instances with Python and Boto3

This Python script stops all currently running EC2 instances in your AWS account using the [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library. It can be used locally or deployed as an AWS Lambda function for scheduled automation (e.g., stopping instances daily).

## Features

- Stop all running EC2 instances automatically.
- Uses AWS Boto3 SDK to interact with EC2 service.
- Can be executed locally or as part of an AWS Lambda function.
- Easily customizable to include other instance states or actions.

## Prerequisites

Before running the script, ensure that you have:

- Python 3.8 or higher installed.
- AWS credentials configured locally (or in Lambda if deploying there).
- The necessary permissions to stop EC2 instances (`ec2:DescribeInstances`, `ec2:StopInstances`).

## Setup and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stop-ec2-instances.git
cd stop-ec2-instances
```

### 2. Install Dependencies

Make sure you have Boto3 installed. If not, you can install it using pip:

```bash
pip install boto3
```

### 3. AWS Credentials Configuration

Ensure that your AWS credentials are correctly set up by either:
- Configuring them via the AWS CLI:

```bash
aws configure
```

- Or setting the following environment variables:

```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
```

### 4. Run the Script

To stop all running EC2 instances, simply run the script in your terminal:

```bash
python stop_instances.py
```

The script will output the IDs of the instances being stopped or will inform you if no instances are running.

### 5. Deploy to AWS Lambda (Optional)

If you want to automate this script to run on a schedule, you can deploy it as an AWS Lambda function:

1. **Create a Lambda function** in the AWS Console with Python 3.8 or higher as the runtime.
2. **Paste the script code** into the Lambda function's code editor.
3. **Set up permissions** for the Lambda function to access EC2 instances:
   - Attach an appropriate IAM role with the `AmazonEC2FullAccess` policy or custom EC2 permissions.
4. **Set a trigger** with AWS EventBridge (formerly CloudWatch Events) to schedule the Lambda function to run at a specific time (e.g., daily at 7 PM).

## Script Overview

### Main Script

```python
import boto3

def stop_all_running_instances():
    ec2 = boto3.client('ec2')
    
    # Describe all running instances
    running_instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    # Collect all running instance IDs
    instances_to_stop = [
        instance['InstanceId']
        for reservation in running_instances['Reservations']
        for instance in reservation['Instances']
    ]
    
    # Stop the instances if any are running
    if instances_to_stop:
        print(f"Stopping instances: {instances_to_stop}")
        ec2.stop_instances(InstanceIds=instances_to_stop)
    else:
        print("No running instances found.")

# Lambda handler function for AWS Lambda
def lambda_handler(event, context):
    stop_all_running_instances()

# Call the function if running locally
if __name__ == "__main__":
    stop_all_running_instances()
```



## Author

[Brett Dykes](https://github.com/Brettidykes)
