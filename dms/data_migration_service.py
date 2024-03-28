import boto3

class DataMigrationService():
    def __init__(self, region_name: str):
        self.client = boto3.client('dms', region_name=region_name)

    def describe_replication_tasks(
        self,
        task_arn: str,
        filter_name: str='replication-task-id',
        marker : str = 'string',
        max_records: int=100,
        without_settings: bool = False
    ) -> dict:
        """
            [Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dms/client/describe_replication_tasks.html)
        
            Params:
                - filter_name=replication-task-arn | replication-task-id | migration-type | endpoint-arn | replication-instance-arn
        """
        tasks = self.client.describe_replication_tasks(
            Filters = [
                {
                    'Name': filter_name,
                    'Values': [task_arn]
                },
            ],
            Marker=marker,
            MaxRecords=max_records,
            WithoutSettings=without_settings
        )

        return tasks
