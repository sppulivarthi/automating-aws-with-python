# automating-aws-with-python

# Setup
pipenv --three # creates pipfile and its dependencies for the project
pipenv install boto3
pipenv install -d i python

#Run
pipenv run ipython

#01-Webotron
webotron is a script that will sync a local directory to an s3 bucket, and optionally configure Route 53 and cloudFront as well.
