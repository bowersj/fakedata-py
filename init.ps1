Write-Output "Creating Virtual Environment 'env'"
python -m virtualenv env

./activate.ps1

Write-Output "Installing Dependencies"
pip install -r requirements