#!/usr/bin/env python3
import os
import sys
import shutil
import re

templates_folder = "/templates"
static_folder = "/static"
valid_args_list = ['-dB', '--debug', '-sS', '--css-js', '-dC', '--docker']

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

# get application name
def get_app_name():
  try:
      app_name = sys.argv[1]
  except:
      print(f"{bcolors.WARNING}App name cannot be empty. Please consider using --help")
      print(f"{bcolors.FAIL}Creation of directory failed: ")
      sys.exit(1)
  return app_name

def is_name_valid(app_name):
  # regex to accept only alphanumeric
  if (bool(re.match(r"^[a-zA-Z0-9\-]*$", app_name)) and (app_name.startswith('-') is False) and (app_name != "app")):
    return True
  else:
    return False

#get all arguments passed
def get_args():
  args = sys.argv
  args.pop(0)
  return args

def is_args_valid(args):
    valid_args =  all(arg in valid_args_list for arg in args)
    return valid_args

# create directory for application
def create_dir(app_name):
  try:
    os.mkdir(app_name)
  except FileExistsError:
    print('Directory already exists')
    print(f"{bcolors.FAIL}Creation of directory failed: %s" % app_name)
    sys.exit(1)

# create app.py in directory 'app_name'
def create_app(app_name, debugger_mode):
    appPy = open(app_name + "/app.py", "w+")
    if (debugger_mode):
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run(debug=True, host='0.0.0.0')\n"
    else:
        linePython = "from flask import Flask, render_template\n" + "app = Flask(__name__)\n\n" + "@app.route('/')\n" + "def hello():\n" + "\treturn render_template('index.html')\n\n" + "if __name__ == '__main__':\n" + "\tapp.run(host='0.0.0.0')\n"
    appPy.writelines([linePython])
    appPy.close()

# create templates folder in directory
def create_templates_folder(app_name, import_css_js):
    os.makedirs(app_name + templates_folder)
    if (import_css_js):
        lineHtml ="""
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World</title>
    <link rel='stylesheet' href='/static/stylesheet/style.css'>
  </head>
  <body>
    <h1>Hello World!!</h1>
    <script src='/static/js/app.js'></script>
  </body>
</html>
"""
    else:
        lineHtml = """
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World!!</h1>
  </body>
</html>
"""
    indexHtml = open(app_name + templates_folder + "/index.html", "w+")
    indexHtml.writelines([lineHtml])
    indexHtml.close()

# create static folder in directory
def create_static_folder(app_name):
    # This is where stylesheets goes
    os.makedirs(app_name + static_folder + "/stylesheet")
    cssFile = open(app_name + static_folder + "/stylesheet" + "/style.css", "w+")
    cssFile.close()

    # This is where javascript goes
    os.makedirs(app_name + static_folder + "/js")
    jsFile = open(app_name + static_folder + "/js" + "/app.js", "w+")
    jsFile.close()

# manage docker contents in app folder
def create_dockerfile(app_name):
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

app_name = get_app_name()
args = get_args()
args.remove(app_name)

def print_manual():
    print('Usage: create-flask-app [app_name] -[arguments]\n')
    print('Options and arguments available for creating flask apps:')
    print('  -dB or --debug\t\t Enables debugger mode on'.expandtabs(10))
    print('  -sS or --css-js\t\t Import stylesheet and script tag'.expandtabs(10))
    print('  -dC or --docker\t\t Generate Dockerfile and docker-compose.yml'.expandtabs(10))
    print('  -h or --help\t\t Print help'.expandtabs(10))

# validate name of app!!
if (is_name_valid(app_name)):

    # validate all arguments first!!
    if(is_args_valid(args)):
    
        # Create folder named app_name
        create_dir(app_name)

        # Arguments
        debugger_mode = False
        import_css_js = False
        use_docker = False

        if '-dB' in args or '--debug' in args:
            debugger_mode = True
            print("- Debugger mode on")
        if '-sS' in args or '--css-js' in args:
            import_css_js = True
            print("- Css and Js mode on")
            create_static_folder(app_name)
        if '-dC' in args or '--docker' in args:
            use_docker = True
            print("- Docker mode on")
            print('  |__ cd %s' % app_name)
            print('  |__ \"docker-compose up -d\" to start app')

        if (debugger_mode is False and import_css_js is False and use_docker is False):
            print("- Debugger mode off")
            print("- Css and Js mode off")
            print("- Docker mode off")

        # create templates folder to hold index.html
        create_templates_folder(app_name, import_css_js)

        # create app.py in root directory(app_name)
        create_app(app_name, debugger_mode)

        # move application to docker container; 
        if (use_docker):
            # generate Dockerfile
            create_dockerfile(app_name)

        print(f"{bcolors.OKGREEN}Creation of directory success: %s" % app_name)

    else:
        print('Unknown argument! Please check the help section\n')
        print_manual()
        print(f"{bcolors.FAIL}Creation of directory failed: %s" % app_name)
        sys.exit(1)
else:
    if (app_name == '-h' or app_name == '--help'):
        print_manual()
    else:
        print(f'{bcolors.WARNING}Please choose another app name')
        print(f"{bcolors.FAIL}Creation of directory failed: %s" % app_name)