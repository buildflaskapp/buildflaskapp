import os
import sys
import shutil
from scripts.messages import empty_name, failure_msg, success_msg
import re

templates_folder = "/templates"
static_folder = "/static"
valid_args_list = ['-d','--debugger', '-cj', '--css-js', '-dc', '--docker-container', '-bs', '--bootstrap', '-jq', '--jQuery', '-gsap', '--gsap']

# get application name
def get_app_name():
  try:
      app_name = sys.argv[1]
  except:
      print('App name cannot be empty. Please consider using --help')
      empty_name()
  return app_name

def is_name_valid(app_name):
  # regex to accept only alphanumeric
  if (bool(re.match(r"^[a-zA-Z0-9\-\_]*$", app_name)) and (app_name.startswith('-') is False) and (app_name != "app")):
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
    print('Directory already exists: ' + app_name)
    failure_msg(app_name)

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
def create_templates_folder(app_name, import_css_js, import_bootstrap, import_jquery, import_gsap):
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

  if (import_bootstrap):
    add_bootstrap(app_name, import_bootstrap)

  if (import_jquery):
    add_jquery(app_name, import_jquery)

  if (import_gsap):
    add_gsap(app_name, import_gsap)

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

def add_bootstrap(app_name, import_bootstrap):
  if import_bootstrap:
    bootstrap_cdn = '<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" rel="stylesheet">\n'
    head_tag = "</head>"

    input_file = open(app_name + templates_folder + '/index.html', 'rt')
    lines = input_file.read()
    lines = lines.replace(head_tag, bootstrap_cdn + head_tag)
    input_file.close()

    input_file = open(app_name + templates_folder + '/index.html', 'wt')
    input_file.write(lines)
    input_file.close()

def add_jquery(app_name, import_jquery):
  if import_jquery:
    jquery_cdn = '<script src="https://code.jquery.com/jquery-3.4.1.min.js" crossorigin="anonymous"></script>\n'
    body_tag = "</body>"

    input_file = open(app_name + templates_folder + '/index.html', 'rt')
    lines = input_file.read()
    lines = lines.replace(body_tag, jquery_cdn + body_tag)
    input_file.close()

    input_file = open(app_name + templates_folder + '/index.html', 'wt')
    input_file.write(lines)
    input_file.close()

def add_gsap(app_name, import_gsap):
  if import_gsap:
    gsap_cdn = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.2.4/gsap.min.js"></script>\n'
    body_tag = "</body>"

    input_file = open(app_name + templates_folder + '/index.html', 'rt')
    lines = input_file.read()
    lines = lines.replace(body_tag, gsap_cdn + body_tag)
    input_file.close()

    input_file = open(app_name + templates_folder + '/index.html', 'wt')
    input_file.write(lines)
    input_file.close()