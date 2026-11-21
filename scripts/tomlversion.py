
import os
import re
with open("pyproject.toml", "r") as f:
    content = f.read()


def repl(match):
    major, minor, patch = map(int, match.groups())
    new_ver = f"{major}.{minor}.{patch + 1}"
    with open("new_version.txt", "w") as vf:
        vf.write(new_ver)
    return f"version = \"{new_ver}\""

updated = re.sub(r"^version\s*=\s*\"(\d+)\.(\d+)\.(\d+)\"", repl, content, count=1, flags=re.MULTILINE)
with open("pyproject.toml", "w") as f:
    f.write(updated)

os.system("rm new_version.txt")


os.system("""
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add pyproject.toml
          git commit -m "chore(release): bump version to new version"
          git push
""")
