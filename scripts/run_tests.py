'''
run all tests
'''
import subprocess
import os
#os.system("python -m unittest discover -s test")
#os.system("uv run python -m unittest")
os.system("python test/testanagrams.py")
#os.system("uv run python test/testanagrams.py")
#os.system("uv sync")
#os.system("uv run pytest test/testanagrams.py --junitxml=test-results/report.xml")
#os.system("pytest test/testanagrams.py --junitxml=test-results/report.xml")