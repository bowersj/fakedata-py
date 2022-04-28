Write-Output "Creating Virtual Environment 'env'"
virtualenv env

./activate.ps1

Write-Output "Installing Dependencies"
pip install -r requirements