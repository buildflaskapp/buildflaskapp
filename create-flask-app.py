import os
import sys

# current_path = os.getcwd()
new_folder = sys.argv[1]
# print("Your current working path is %s" % current_path)
static_folder = "/static"
templates_folder = "/templates"


# Index.html lines
lineHtml = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hello World</title>\n</head>\n<body>\n<h1>Hello World!!</h1>\n</body>\n</html>\n"

# App.py lines
linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n" + "@app.route('/')\n\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run()\n"

try:
    os.mkdir(new_folder)
except OSError:
    print("Creation of directory failed: %s" % sys.argv[1])
else:
    print("Creation of directory success: %s" % sys.argv[1])

try:
    os.makedirs(new_folder + static_folder)
    os.makedirs(new_folder + templates_folder)
    
    indexHtml = open(new_folder + templates_folder + "/index.html", "w+")
    indexHtml.writelines([lineHtml])
    indexHtml.close()

    appPy = open(new_folder + "/app.py", "w+")
    appPy.writelines([linePython])
    appPy.close()
except OSError:
    print("Creation of sub directory failed: %s" % sys.argv[1])
else:
    print("Creation of sub directory success: %s" % sys.argv[1])