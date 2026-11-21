
import os
import re

os.system("rm VERSION.txt")

with open("pyproject.toml", "r") as f:
    content = f.read()



def readversionfile():
    with open("VERSION.txt", "r") as f:
        versioncontent = f.read()
    return versioncontent
    
def repl(match):
    major, minor, patch = map(int, match.groups())
    new_ver = f"{major}.{minor}.{patch + 1}"
    with open("VERSION.txt", "w") as vf:
        vf.write(new_ver)
    return f"version = \"{new_ver}\""

updated = re.sub(r"^version\s*=\s*\"(\d+)\.(\d+)\.(\d+)\"", repl, content, count=1, flags=re.MULTILINE)
with open("pyproject.toml", "w") as f:
    f.write(updated)

newversionnumber = readversionfile()

#os.system("rm VERSION.txt")

print("new version : %s" % newversionnumber)

os.system("""
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add pyproject.toml
          git commit -m "chore(release): bump version to new version"
          git push
""")

os.system('git tag -a v%s -m "Release version %s"' %(newversionnumber,newversionnumber))
os.system('git push origin v%s' % newversionnumber)
