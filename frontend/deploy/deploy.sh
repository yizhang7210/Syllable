if [ -z "$1" ]
then
    echo "Please run the script with prod or dev"
    exit 1
fi

# Get aws command lin
sudo apt-get install python-pip python-dev
sudo pip install -r $(pwd)/deploy/requirements.txt

# Run web pack and push the files to S3
npm run "build-"$1

if [ "$1" = "prod" ]
then

    bucket=www.getsyllable.ca
    distributionId=E2G65GUDUDAZ14
else
    bucket=dev.getsyllable.ca
    distributionId=E1B2THL5EFIS1O
fi

aws s3 sync dist s3://$bucket --metadata-directive REPLACE \
--cache-control max-age=3600
aws cloudfront create-invalidation --distribution-id $distributionId --paths '/*'
