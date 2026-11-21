'''
build wheel
'''
import os
#os.system("python -m build --wheel")
os.system("rm -rf dist")
os.system("uv build --wheel")