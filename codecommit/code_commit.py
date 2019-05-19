import boto3
import pyboto3

# A class for putting, commiting and deleting files from AWS code commit
class codeCommit:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.codecommit"""

    # A method to commit a file to AWS code commit
    def commit_file(self, commit_id, repo_name, branch_name, author_name, auth_email, file_path, file_content, commit_message):
        return self._client.create_commit(
            repositoryName=repo_name,
            branchName=branch_name,
            authorName=author_name,
            parentCommitId=commit_id,
            email=auth_email,
            commitMessage=commit_message,
            keepEmptyFolders=True,
            putFiles=[
                {
                    'filePath': file_path,
                    'fileContent': file_content
                }
            ]
        )

    # A method to commit a file to AWS code commit
    def commit_file_new_repo(self, repo_name, branch_name, author_name, auth_email, file_path, file_content, commit_message):
        return self._client.create_commit(
            repositoryName=repo_name,
            branchName=branch_name,
            authorName=author_name,
            email=auth_email,
            commitMessage=commit_message,
            keepEmptyFolders=True,
            putFiles=[
                {
                    'filePath': file_path,
                    'fileContent': file_content
                }
            ]
        )

    # A method for deleting files in AWS code commit
    def delete_file(self, repo_name, branch_name, author_name, auth_email, commit_message, file_path):
        return self._client.create_commit(
            repositoryName=repo_name,
            branchName=branch_name,
            authorName=author_name,
            email=auth_email,
            commitMessage=commit_message,
            keepEmptyFolders=True,
            deleteFiles=[
                {
                    'filePath': file_path,
                    'isMove': True
                },
            ]
        )

    def put_file(self, repo_name, branch_name, file_content, file_path, cid, commit_message, author_name, author_email):
        return self._client.put_file(
            repositoryName=repo_name,
            branchName=branch_name,
            fileContent=file_content,
            filePath=file_path,
            fileMode='NORMAL',
            parentCommitId=cid,
            commitMessage=commit_message,
            name=author_name,
            email=author_email
        )

    def create_repository(self, repo_name, repo_description):
        return self._client.create_repository(
            repositoryName=repo_name,
            repositoryDescription=repo_description
        )
