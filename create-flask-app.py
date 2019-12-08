import os
import sys

# current_path = os.getcwd()
new_folder = sys.argv[1]
# print("Your current working path is %s" % current_path)
static_folder = "/static"
templates_folder = "/templates"

line1 = "from flask import Flask, render_template\n"
line2 = "app = Flask(__name__)\n"
line3 = "@app.route('/')\n\n"

line4 = "def hello():\n"
line5 = "\treturn render_template('index.html')\n\n"

line6 = "if __name__ == '__main__':\n"
line7 = "\tapp.run()\n"

try:
    os.mkdir(new_folder)
except OSError:
    print("Creation of directory failed: %s" % sys.argv[1])
else:
    print("Creation of directory success: %s" % sys.argv[1])

try:
    os.makedirs(new_folder + static_folder)
    os.makedirs(new_folder + templates_folder)
    # index-html = open(new_folder + "/index.html", "w+")
    appPy = open(new_folder + "/app.py", "w+")
    appPy.writelines([line1, line2, line3, line4, line5, line6, line7])
    appPy.close()
except OSError:
    print("Creation of sub directory failed: %s" % sys.argv[1])
else:
    print("Creation of sub directory success: %s" % sys.argv[1])