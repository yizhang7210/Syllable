# Get aws command line
sudo apt-get install python-pip python-dev
sudo pip install -r $(pwd)/deploy/requirements.txt

# Run web pack and push the files to S3
npm run build

aws s3 sync dist s3://www.getsyllable.ca --metadata-directive REPLACE \
--cache-control max-age=3600
aws cloudfront create-invalidation --distribution-id E2G65GUDUDAZ14 --paths '/*'
