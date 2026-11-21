'''
publish wheel to pypi
'''
import os   
token = os.getenv("PYPI_TOKEN")
os.system("twine upload -u __token__ -p %s dist/*" % token)

