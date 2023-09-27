import os
import time
import platform

current_os = platform.system().lower()
py = 'python3' if current_os == "linux" else 'python'
if not os.path.exists("./hackAI"):
    print("Creating Virtual Environment.")
    os.system(f"{py} -m venv hackAI")
else:
    print("Virtual Environment Exists Skipping Creation.\n")

os.system("clear")

activate_command = ""
if platform == "windows":
    activate_command = "hackAI\Scripts\activate"
elif platform == "linux":
    activate_command = "source hackAI/bin/activate"

# activate pyenv
os.system(activate_command)

if not os.path.exists("./requirements.txt"):
    print("requirements.txt file not found")
else:
    os.system("pip install -r requirements.txt")

print("\nSetup Complete\nStarting the App.")
time.sleep(5)
os.system("clear")
os.system(f"{py} ./src/main.py")