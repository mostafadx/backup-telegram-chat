# Update and upgrade the system
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python3-venv

# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate