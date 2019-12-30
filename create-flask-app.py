#!/usr/bin/env python3
import os
import sys
import shutil

app_folder = sys.argv[1]
static_folder = "/static"
templates_folder = "/templates"
addDebug = False
addStyleScript = False

def createStaticFolder():
    # This is where stylesheets goes
    print("-css & js mode on")
    os.makedirs(app_folder + static_folder + "/stylesheet")
    cssFile = open(app_folder + static_folder + "/stylesheet" + "/style.css", "w+")
    cssFile.close()

    # This is where javascript goes
    os.makedirs(app_folder + static_folder + "/js")
    jsFile = open(app_folder + static_folder + "/js" + "/app.js", "w+")
    jsFile.close()

def createTemplatesFolder():
    os.makedirs(app_folder + templates_folder)
    if (addStyleScript):
        lineHtml = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hello World</title>\n<link rel='stylesheet' href='/static/stylesheet/style.css'>\n</head>\n<body>\n<h1>Hello World!!</h1>\n<script src='/static/js/app.js'></script>\n</body>\n</html>\n"
    else:
        lineHtml = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hello World</title>\n</head>\n<body>\n<h1>Hello World!!</h1>\n</body>\n</html>\n"
    indexHtml = open(app_folder + templates_folder + "/index.html", "w+")
    indexHtml.writelines([lineHtml])
    indexHtml.close()

def createAppPy():
    appPy = open(app_folder + "/app.py", "w+")
    if (addDebug):
        print("-debug mode on")
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run(debug=True, host='0.0.0.0')\n"
    else:
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run(host='0.0.0.0')\n"
    appPy.writelines([linePython])
    appPy.close()

try:
    os.mkdir(app_folder)
    if len(sys.argv) > 2:
        if '-dB' in sys.argv:
            addDebug = True
        if '-sS' in sys.argv:
            addStyleScript = True
            createStaticFolder()
    else:
        print("No options passed in")

    createTemplatesFolder()
    createAppPy()
    if '-dC' in sys.argv:
        print('Folders have to be moved')
        # move folders in app folder
        os.makedirs(app_folder + "/app")
        files = os.listdir(app_folder)
        for f in files:
            if f != 'app':
                shutil.move(app_folder + '/' + f, app_folder + "/app")

        # create requirements.txt
        requirements_txt = open(app_folder + "/app/requirements.txt", "w+")
        linePython = "flask\n"
        requirements_txt.writelines([linePython])
        requirements_txt.close()

        # create Dockerfile
        dockerfile_txt = open(app_folder + "/app/Dockerfile", "w+")
        linePython = "FROM python:3.7-alpine \nWORKDIR /app \nCOPY . /app \nRUN pip3 install -r requirements.txt \nENTRYPOINT [\"python3\"] \nCMD [\"app.py\"]"
        dockerfile_txt.writelines([linePython])
        dockerfile_txt.close()

        # create docker-compose.yml
        dockercompose_yml = open(app_folder + "/docker-compose.yml", "w+")
        linePython = "version: '3' \nservices: \n  web: \n    build: app \n    ports: \n      - '5000:5000'"
        dockercompose_yml.writelines([linePython])
        dockercompose_yml.close()
except OSError:
    print("Creation of directory failed: %s" % sys.argv[1])
else:
    print("Creation of directory success: %s" % sys.argv[1])
