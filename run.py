import os
import time
if not os.path.exists("./hackAI"):
    print("Creating Virtual Environment.")
    os.system("python3 -m venv hackAI")
else:
    print("Virtual Environment Exists Skipping Creation.\n")

os.system("clear")

if not os.path.exists("./requirements.txt"):
    print("requirements.txt file not found")
else:
    os.system("pip install -r requirements.txt")

print("\nSetup Complete\nStarting the App.")
time.sleep(5)
os.system("clear")
os.system("python3 ./src/main.py")