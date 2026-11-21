'''
publish wheel to pypi
'''
import os   
token = os.getenv("PYPI_TOKEN")
#os.system('uv publish --token "%s" --publish-url https://test.pypi.org/legacy/',token)
#os.system('uv publish --token "%s" --publish-url https://test.pypi.org/legacy/',token)
#os.system('uv publish dist/* --publish-url https://test.pypi.org/legacy/ --token %s, ""')
os.system("twine upload -u __token__ -p %s dist/*" % token)


#twine check dist/*
#twine upload dist/*