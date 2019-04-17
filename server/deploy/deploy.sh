if [ -z "$1" ]
then
    echo "Please run the script with prod or dev"
    exit 1
fi

bash $(pwd)/deploy/setup-eb.sh
echo 1 | eb init Syllable --region us-east-2 # 1 is for default environment. Doesn't actually matter.
eb deploy "syllable-"$1
