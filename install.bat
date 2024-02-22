@echo off
echo Setting up virtual environment...

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Upgrade pip
python -m pip install --upgrade pip

# Upgrade wheel
pip install --upgrade wheel

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo Installation complete.
