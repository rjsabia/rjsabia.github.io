import os
import openai

openai.api_key = os.getenv('OPEN_AI_KEY_01')

# trick for installing
# !pip3 install GitPython

from git import Repo
from pathlib import Path

PATH_TO_BLOG_REPO = Path("/Users/bloodrubber/Desktop/AI_Python_Course/GitHub/rjsabia.github.io/.git")
# print(PATH_TO_BLOG_REPO.parent)
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent

PATH_TO_CONTENT = PATH_TO_BLOG/"content"
# print(PATH_TO_CONTENT)

PATH_TO_CONTENT.mkdir(exist_ok=True,parents=True)

def update_blog(commit_message='Updates blog'):
    # GitPython -- Rep Location
    repo = Repo(PATH_TO_BLOG_REPO)
    # git add
    repo.git.add(all=True)
    # git commit -m "updates blog"
    repo.index.commit(commit_message)
    # git push
    origin = repo.remote(name='origin')
    origin.push()

random_text_string = "BWAH 33333"

with open(PATH_TO_BLOG/"index.html",'w') as f:
    f.write(random_text_string)

update_blog()











