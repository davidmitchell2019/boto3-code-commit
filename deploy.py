from src.codecommit.code_commit import codeCommit
from src.codecommit.client_locator import CODECOMMITClient

def main():

    username = "David"
    data = "some jason data to post"
    ccommit_client = CODECOMMITClient().get_client()
    cclient = codeCommit(ccommit_client)
    cclient.post_data_to_repo(username, data)

if __name__ == '__main__':
    main()
