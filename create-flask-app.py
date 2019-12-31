#!/usr/bin/env python3
import os
import sys
import shutil

app_name = sys.argv[1]
static_folder = "/static"
templates_folder = "/templates"
addDebug = False
addStyleScript = False

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

def createStaticFolder():
    # This is where stylesheets goes
    print("-css & js mode on")
    os.makedirs(app_name + static_folder + "/stylesheet")
    cssFile = open(app_name + static_folder + "/stylesheet" + "/style.css", "w+")
    cssFile.close()

    # This is where javascript goes
    os.makedirs(app_name + static_folder + "/js")
    jsFile = open(app_name + static_folder + "/js" + "/app.js", "w+")
    jsFile.close()

def createTemplatesFolder():
    os.makedirs(app_name + templates_folder)
    if (addStyleScript):
        lineHtml = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hello World</title>\n<link rel='stylesheet' href='/static/stylesheet/style.css'>\n</head>\n<body>\n<h1>Hello World!!</h1>\n<script src='/static/js/app.js'></script>\n</body>\n</html>\n"
    else:
        lineHtml = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hello World</title>\n</head>\n<body>\n<h1>Hello World!!</h1>\n</body>\n</html>\n"
    indexHtml = open(app_name + templates_folder + "/index.html", "w+")
    indexHtml.writelines([lineHtml])
    indexHtml.close()

def createAppPy():
    appPy = open(app_name + "/app.py", "w+")
    if (addDebug):
        print("-debug mode on")
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run(debug=True, host='0.0.0.0')\n"
    else:
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run(host='0.0.0.0')\n"
    appPy.writelines([linePython])
    appPy.close()

def createDockerfile():
    # move folders in app folder
    os.makedirs(app_name + "/app")
    files = os.listdir(app_name)
    for f in files:
        if f != 'app':
            shutil.move(app_name + '/' + f, app_name + "/app")

    # create requirements.txt
    requirements_txt = open(app_name + "/app/requirements.txt", "w+")
    linePython = "flask\n"
    requirements_txt.writelines([linePython])
    requirements_txt.close()

    # create Dockerfile
    dockerfile_txt = open(app_name + "/app/Dockerfile", "w+")
    linePython = "FROM python:3.7-alpine \nWORKDIR /app \nCOPY . /app \nRUN pip3 install -r requirements.txt \nENTRYPOINT [\"python3\"] \nCMD [\"app.py\"]"
    dockerfile_txt.writelines([linePython])
    dockerfile_txt.close()

    # create docker-compose.yml
    dockercompose_yml = open(app_name + "/docker-compose.yml", "w+")
    linePython = "version: '3' \nservices: \n  web: \n    build: app \n    ports: \n      - '5000:5000'"
    dockercompose_yml.writelines([linePython])
    dockercompose_yml.close()

    print("-dockerfile generated")
    print('  --> cd %s' % app_name)
    print('  --> \"docker-compose up -d\" to start app')

try:
    if ((app_name == 'app') or (app_name.startswith('-'))):
        if (app_name == '-h' or app_name == '--help'):
            print('Usage: create-flask-app [app_name] -[arguments]\n')
            print('Arguments:')
            print('  -dB \t\t debug mode on')
            print('  -sS \t\t import stylesheet and script tag')
            print('  -dC \t\t create Dockerfile and docker-compose.yml')
            print('  -h or --help \t Print help')
        else:
            print(f'{bcolors.WARNING}Please choose another app name')
            print(f"{bcolors.FAIL}Creation of directory failed: %s" % sys.argv[1])
    else:
        os.mkdir(app_name)
        if len(sys.argv) > 2:
            if '-dB' in sys.argv:
                addDebug = True
            if '-sS' in sys.argv:
                addStyleScript = True
                createStaticFolder()
        else:
            print(f'{bcolors.WARNING}No options passed in')

        createTemplatesFolder()
        createAppPy()
        if '-dC' in sys.argv:
            createDockerfile()
        print(f"{bcolors.OKGREEN}Creation of directory success: %s" % sys.argv[1])

except OSError:
    print(f"{bcolors.FAIL}Creation of directory failed: %s" % sys.argv[1])
