from src.codecommit.code_commit import codeCommit
from src.codecommit.client_locator import CODECOMMITClient

def main():
    #TODO: drop all of this code into a method in the code_commit.py class
    #TODO: add the below variables into the class so they are stored in the object
    #TODO: exception handling and unit tests
    author_name = "David"
    author_email = "anemail"
    branch = "master"
    repo = "terraform"
    file_path = "terraform/request.json"
    commits = 0
    commit_message = "Terraform commit"
    ccommit_client = CODECOMMITClient().get_client()
    cclient = codeCommit(ccommit_client)
    file_content = "something here"
    pcid = ""


    # if commits = 0 then create a repo and the initial file
    # If the repo is already in use or created this will fail as commit ID can only be empty in an empty repo

    if (commits == 0):
        try:
            #create terraform repo
            repos = cclient.create_repository(repo, "A repo for Terraform request response data")
            print("terraform repo created")
            # class calls method and assigns the api response
            commit_response = cclient.commit_file_new_repo(repo, branch, author_name, author_email, file_path, file_content, commit_message)
            print("great this worked so repo must have been created with an empty directory")
            # get the commit ID of the first commit
            pcid = commit_response['commitId']
            commits += 1
        except:
            print("directory already exists or is not an empty directory")
            print(pcid)

    # if this is the second commit we can use the commit ID
    else:
        # Add the file using the cid (commit id) of the put file
        commit_response = cclient.commit_file(pcid, repo, branch, author_name, author_email, file_path, file_content, commit_message)
        pcid = commit_response['commitId']
        commits += 1


if __name__ == '__main__':
    main()
