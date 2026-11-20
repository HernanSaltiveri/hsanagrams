import subprocess
import os
#result = subprocess.run(["python -m unittest", "test/testanagrams.py"])
print(os.getcwd())
os.system("python -m unittest discover -s test")