#!/usr/bin/env python3
import os
import sys

new_folder = sys.argv[1]
static_folder = "/static"
templates_folder = "/templates"
addDebug = False
addStyleScript = False

def createStaticFolder():
    # This is where stylesheets goes
    print("-sS mode on")
    os.makedirs(new_folder + static_folder + "/stylesheet")
    styleCss = open(new_folder + static_folder + "/stylesheet" + "/style.css", "w+")
    styleCss.close()

    # This is where javascript goes
    os.makedirs(new_folder + static_folder + "/js")
    styleJs = open(new_folder + static_folder + "/js" + "/app.js", "w+")
    styleJs.close()

def createTemplatesFolder():
    os.makedirs(new_folder + templates_folder)
    if (addStyleScript):
        lineHtml = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hello World</title>\n<link rel='stylesheet' href='/static/stylesheet/style.css'>\n</head>\n<body>\n<h1>Hello World!!</h1>\n<script src='/static/js/app.js'></script>\n</body>\n</html>\n"
    else:
        lineHtml = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hello World</title>\n</head>\n<body>\n<h1>Hello World!!</h1>\n</body>\n</html>\n"
    indexHtml = open(new_folder + templates_folder + "/index.html", "w+")
    indexHtml.writelines([lineHtml])
    indexHtml.close()

def createAppPy():
    appPy = open(new_folder + "/app.py", "w+")
    if (addDebug):
        print("Debug mode on")
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run(debug=True)\n"
    else:
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run()\n"
    appPy.writelines([linePython])
    appPy.close()

try:
    os.mkdir(new_folder)
    createTemplatesFolder()
    if len(sys.argv) > 2:
        if '-dB' in sys.argv:
            addDebug = True
        if '-sS' in sys.argv:
            addStyleScript = True
            createStaticFolder()
    else:
        print("No options passed in")

    createAppPy()
except OSError:
    print("Creation of directory failed: %s" % sys.argv[1])
else:
    print("Creation of directory success: %s" % sys.argv[1])
