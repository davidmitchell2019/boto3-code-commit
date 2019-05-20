# boto3-code-commit

Creating some code to create a repo in AWS code commit, create a file in the repo and push some data to that file when the method runs

An auto back up to git for a http responses data.

Problem domain Codecommit specific

You can push a file to code commit if, you have an empty repo or you have the parent commit ID from the previous commit.

So in this code we create an empty repo, push a file and then use that parent commit ID to push any data changes to that file.