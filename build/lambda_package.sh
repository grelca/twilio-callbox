#/usr/bin/bash

rm -rf dist

mkdir -p dist/lambda
cp -R src dist/lambda
mv dist/lambda/src/lambda_function.py dist/lambda/lambda_function.py

pipenv install
pip freeze > dist/requirements.txt
pip install -r dist/requirements.txt -t dist/lambda

cd dist/lambda
chmod -R 755 *
zip -r ../lambda.zip *
