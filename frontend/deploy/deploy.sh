# Get aws command lin
sudo apt-get install python-pip python-dev
sudo pip install -r $(pwd)/deploy/requirements.txt

# Run web pack and push the files to S3
npm run build-dev
aws s3 sync dist s3://dev.getsyllable.ca --metadata-directive REPLACE \
--cache-control max-age=3600
aws cloudfront create-invalidation --distribution-id EQK07MC757ELW --paths '/*'
