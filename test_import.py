import sys
import os

print("Current directory:", sys.path[0])
print("Working directory:", os.getcwd())
print("Files in current directory:", [f for f in os.listdir('.') if os.path.isfile(f)])
print("Folders in current directory:", [d for d in os.listdir('.') if os.path.isdir(d)])

try:
    import catalog_project
    print("Module catalog_project imported successfully!")
except Exception as e:
    print(f"Error importing catalog_project: {e}")

try:
    import catalog_project.settings
    print("Module catalog_project.settings imported successfully!")
except Exception as e:
    print(f"Error importing catalog_project.settings: {e}")