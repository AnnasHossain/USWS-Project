import os

# Bestimmen Sie den relativen Pfad zur api_key-Datei
base_dir = os.path.dirname(os.path.realpath(__file__))
api_key_path = os.path.join(base_dir, '../api_key')

# Read the API key from a file
with open('api_key', 'r') as file:
    api_key = file.read().strip()