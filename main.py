import os
import openai
import shutil


# environmental variables
openai.api_key = os.getenv('OPEN_AI_KEY_01')
GITHUB_KEY = os.getenv('GITHUB_KEY_02')

# trick for installing
# !pip3 install GitPython

from git import Repo
from pathlib import Path

GITHUB_URL = GITHUB_KEY

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
    origin.set_url(GITHUB_URL)  # set the GitHub URL with access token
    origin.push()

random_text_string = "You are a cry sack yo"

with open(PATH_TO_BLOG/"index.html",'w') as f:
    f.write(random_text_string)

update_blog()

def create_new_blog(title,content,cover_image):
    cover_image = Path(cover_image)

    files = len(list(PATH_TO_CONTENT.glob("*.html")))
    new_title = f"{files+1}.html"
    path_to_new_content = PATH_TO_CONTENT/new_title

    shutil.copy(cover_image,PATH_TO_CONTENT)

    if not os.path.exists(path_to_new_content):
        # Write a new file
        with open(path_to_new_content,"w") as f:
            f.write("<!DOCTYPE html\>\n")
            f.write("<html>\n")
            f.write("<head>\n")
            f.write(f"<title> {title} </title>\n")
            f.write("</head>\n")

            f.write("<body>\n")
            f.write(f"<img src='{cover_image.name}' alt='Cover Image'> <br />\n")
            f.write(f"<h1> {title} </h1>")
            # OpenAI --> Completion GPT --> 
            f.write(content.replace("\n","<br />\n"))
            f.write("</body>\n")
            f.write("</html>\n")
            print("Blog Page Created!")
            print("Here is what the path name should be: ", files)
            return path_to_new_content

    else:
        raise FileExistsError("File already exist, please check file name. Aborting operation!")

path_to_new_content = create_new_blog('Testing title beoitch : ]','Badummm, BUMMM','uglyAF.png')

print(path_to_new_content)




