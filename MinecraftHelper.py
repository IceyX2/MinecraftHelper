import atexit
import subprocess

def cleanup():
    subprocess.call("python cmdconfigunloader.py", shell=True)

# Register the cleanup function to be called on program termination
atexit.register(cleanup)

subprocess.call("python cmdconfigloader.py", shell=True)
print("Checking for updates")

print("----------------------------------------------------")
print("                   [Available]")
print("Skyblock [Hypixel] = \"hysky\"")
print("Oneblock [Saphire] = \"sapone\"")
print("Survival [Vanilla] = \"survival\"")
print("----------------------------------------------------")

help_input = input("What do you need help with: ")