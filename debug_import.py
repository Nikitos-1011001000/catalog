import sys
import os

print("Current working directory:", os.getcwd())
print("sys.path:", sys.path)
print("\nFiles in current directory:", os.listdir('.'))
print("\nIs __init__.py present?", os.path.exists('__init__.py'))
if os.path.exists('__init__.py'):
    print("__init__.py size:", os.path.getsize('__init__.py'), "bytes")

print("\nAttempting import...")
try:
    import catalog_project
    print("✓ Module imported successfully!")
except Exception as e:
    print(f"✗ Import failed: {e}")