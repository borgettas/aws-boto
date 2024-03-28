import boto3

class Glue():
    """
        [Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/glue.html)
    """
    
    def __init__(self, region_name: str):
        self.client = boto3.client('glue', region_name=region_name)


    def get_job(self, job_name: str):
        job = self.client.get_job(JobName=job_name)
        return job


    def get_jobs(self):
        jobs = self.client.get_jobs(
            # NextToken='string',
            MaxResults=123
        )
        return jobs


    def list_jobs(self):
        jobs = self.client.list_jobs(
            # NextToken='string',
            MaxResults=123,
            Tags={
                'string': 'string'
            }
        )
        return jobs

    
    def update_job(job_name: str, job_update: dict):
        pass