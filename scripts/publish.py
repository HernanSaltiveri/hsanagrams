'''
publish wheel to pypi
'''
import os   
#token = os.getenv("PYPI_HERNAN_API_KEY")
#os.system('uv publish --token "%s" --publish-url https://test.pypi.org/legacy/',token)
#os.system('uv publish --token "%s" --publish-url https://test.pypi.org/legacy/',token)
os.system('uv publish dist/* --publish-url https://test.pypi.org/legacy/ --token %s, ""')


#twine check dist/*
#twine upload dist/*