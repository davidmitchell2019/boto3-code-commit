import boto3


class ClientFactory:
    def __init__(self, client):
        self._client = boto3.client(client, region_name="eu-west-2")
        # aws_access_key_id = ACCESS_KEY
        # aws_secret_access_key = SECRET_KEY
        # TODO: pass access key and secret key into client locator for authentication
        
    def get_client(self):
        return self._client


class DynamoDBClient(ClientFactory):
    def __init__(self):
        super().__init__('dynamodb')