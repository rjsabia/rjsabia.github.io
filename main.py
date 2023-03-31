import os
import openai
import shutil


# environmental variables
openai.api_key = os.getenv('OPEN_AI_KEY_01')
# GITHUB_KEY = os.getenv('GITHUB_KEY_02')
GITHUB_KEY = os.getenv('GITHUB_KEY_03')

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

# random_text_string = "You are a cry sack yo"

# with open(PATH_TO_BLOG/"index.html",'w') as f:
    # f.write(random_text_string)

# update_blog()

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
            # print("Here is what the path name should be: ", new_title)
            return path_to_new_content

    else:
        raise FileExistsError("File already exist, please check file name. Aborting operation!")

path_to_new_content = create_new_blog('Testing title fool : ]','Sup March 30 , 4:30','uglyAF.png')
# print(path_to_new_content)

# --> Index.html ---> Blog Post
from bs4 import BeautifulSoup as Soup

with open(PATH_TO_BLOG/"index.html") as index:
    soup = Soup(index.read())
    # print("This is soup: ", str(soup)) # testing for html to see what it is

# checking for duplicate links
# write the blog post link ---> index.html
def check_for_duplicate_links(path_to_new_content, links):
    urls = [str(link.get("href")) for link in links] # this should be [1.html,2.html,etc etc]
    content_path = str(Path(*path_to_new_content.parts[-2:]))
    return content_path in urls

def write_to_index(path_to_new_content):
    with open(PATH_TO_BLOG/'index.html') as index:
        soup = Soup(index.read())

    links = soup.find_all('a')
    last_link = links[-1]

    if check_for_duplicate_links(path_to_new_content,links):
        raise ValueError("Link already exist fool!")

    # below is referencing alot of the beautiful soup library
    link_to_new_blog = soup.new_tag("a",href=Path(*path_to_new_content.parts[-2:]))
    link_to_new_blog.string = path_to_new_content.name.split('.')[0]
    last_link.insert_after(link_to_new_blog)

    with open(PATH_TO_BLOG/'index.html','w') as f:
        f.write(str(soup.prettify(formatter='html')))


write_to_index(path_to_new_content)
update_blog()

def create_prompt(title):
    prompt = """
    Biography:
    My Name is Russ and I am a Python instructor for coding. I especially focus my teaching on coding AI based python applications.

    Blog
    Title: {}
    tags: tech, python, coding, AI, machine learning, Open AI, Open AI API
    Summary: I talk about what the future of AI could hold for Python applications and Sass products.
    Full Text: """.format(title)
    return prompt

title = "The future of Python, AI, and the one person Sass companies"
# print(create_prompt(title))

response = openai.Completion.create(engine='text-davinci-003',
                                    prompt=create_prompt(title),
                                    max_tokens=1000,
                                    temperature=0.7,
                                    frequency_penalty=0.5)

# print(response['choices'][0]['text'])

blog_content = response['choices'][0]['text']
print(blog_content)

def dalle2_prompt(title):
    # prompt = f"Pixel art showing {title}"
    prompt = f"Show {title} in a retrowave and chillwave art style"
    return prompt

image_prompt = dalle2_prompt(title)

response = openai.Image.create(prompt=image_prompt,
                               n=1,size="1024x1024")

image_url = response['data'][0]['url']
print(image_url)































