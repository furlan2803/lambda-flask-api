rm -f lambda_package.zip
zip -r lambda_package.zip lambda_function
pip install -r lambda_function/requirements.txt -t lambda_function/
zip -r lambda_package.zip lambda_function/*




