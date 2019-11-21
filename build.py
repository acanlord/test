import os
from jinja2 import Template

pages = []
blog = []

def read_files():
    for _, _, files in os.walk("./content"):
        for filename in files:
            title = filename.replace(".html", "")
            title = title.capitalize()
            pages.append({
                "filename": "./content/" + filename,
                "title": title,
                "output": "./docs/{}".format(filename)
            })
    for _, _, files in os.walk("./blog"):
        for filename in files:
            title = filename.replace(".html", "")
            title = title.capitalize()
            blog.append({
                "filename": "./blog/" + filename,
                "title": title,
                "output": "./docs/{}".format(filename)
            })


def gen_html():

    for p in pages:
        template = open("./templates/base.html").read()
        partial = open(p["filename"]).read()
        #template = template.replace("{{title}}", p["title"])
        #template = template.replace("{{content}}", partial)
        open(p["output"], "w+").write(template)


def gen_blog():

    for p in blog:
        template = open("./templates/blog.html").read()
        partial = open(p["filename"]).read()
        template = template.replace("{{title}}", p["title"])
        template = template.replace("{{blog}}", partial)
        open(p["output"], "w+").write(template)

#Jinja stuff, Work in progress
def fix_template():

    for p in pages:
        index_html = open(p["filename"]).read() 
        #template_html = open("templates/base.html").read() 
        template = Template(index_html)
        template = template.render("{{title}}", p["title"])
        open(p["output"], "w+").write(template)



def main():
    read_files()
    gen_html()
    fix_template()
    #gen_blog()
    print("Your files have been generated")

if __name__ == "__main__":
    main()
