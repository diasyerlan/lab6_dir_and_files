import os

path = "test.txt"

if os.path.exists(path):
    if os.access(path, os.R_OK):
        os.remove(path)
        print(f"{path} deleted successfully")
    else:
        print(f"You do not have access to {path}")
else:
    print(f"{path} does not exist")