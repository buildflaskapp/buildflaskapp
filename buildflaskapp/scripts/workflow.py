import os
import sys
import shutil
from buildflaskapp.scripts.messages import empty_name, failure_msg, success_msg
import re
import json
import urllib.request

templates_folder = "/templates"
static_folder = "/static"
valid_args_list = ['-d','--debugger', '-cj', '--css-js', '-dc', '--docker-container', '-bs', '--bootstrap', '-jq', '--jQuery', '-gsap', '--gsap', '-fa', '--font-awesome', '-sl3', '--sqlite3']

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
  args = sys.argv[2:]
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
def create_app(app_name, debugger_mode, sqlite3_mode):
    app_py_file = open(app_name + "/app.py", "w+")
    app_py = """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0')
"""
    app_py_file.writelines([app_py])
    app_py_file.close()

    if (debugger_mode):
      set_debug_on(app_name, debugger_mode)

    if(sqlite3_mode):
      set_sqlite3_mode(app_name, sqlite3_mode)

def set_debug_on(app_name, debugger_mode):
  if debugger_mode:
    debug_on_string = "app.run(host='0.0.0.0', debug=True)"
    app_run_string = "app.run(host='0.0.0.0')"

    app_py_file = open(app_name + '/app.py', 'rt')
    lines = app_py_file.read()
    lines = lines.replace(app_run_string, debug_on_string)
    app_py_file.close()

    app_py_file = open(app_name + '/app.py', 'wt')
    app_py_file.write(lines)
    app_py_file.close()

def set_sqlite3_mode(app_name, sqlite3_mode):
  if sqlite3_mode:
    app_py_file = open(app_name + '/app.py', 'rt')
    lines = app_py_file.read()
    import_flask_string = 'from flask import Flask, render_template'
    import_sqlite_string = 'from flask_sqlalchemy import SQLAlchemy'
    lines = lines.replace(import_flask_string, import_flask_string + '\n' + import_sqlite_string)
    app_py_file.close()

    app_py_file = open(app_name + '/app.py', 'wt')
    app_py_file.write(lines)
    app_py_file.close()

    app_py_file = open(app_name + '/app.py', 'rt')
    lines = app_py_file.read()
    app_instance = 'app = Flask(__name__)'
    app_sqlite3_config_track_modif = "app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False"
    app_sqlite3_config = "app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test-db.sqlite3'\ndb = SQLAlchemy(app)"
    lines = lines.replace(app_instance, app_instance + '\n' + app_sqlite3_config_track_modif + '\n' + app_sqlite3_config)
    app_py_file.close()

    app_py_file = open(app_name + '/app.py', 'wt')
    app_py_file.write(lines)
    app_py_file.close()

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


# create templates folder in directory
def create_templates_folder(app_name, import_css_js, import_bootstrap, import_jquery, import_gsap, import_font_awesome):
  os.makedirs(app_name + templates_folder)
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

  if (import_css_js):
    add_css_js(app_name, import_css_js)

  if (import_bootstrap):
    add_bootstrap(app_name, import_bootstrap)

  if (import_jquery):
    add_jquery(app_name, import_jquery)

  if (import_gsap):
    add_gsap(app_name, import_gsap)

  if (import_font_awesome):
    add_font_awesome(app_name, import_font_awesome)

def add_css_js(app_name, import_css_js):
  if import_css_js:
    stylesheet_string = "<link rel='stylesheet' href='/static/stylesheet/style.css'>\n"
    js_string = "<script src='/static/js/app.js'></script>\n"
    head_tag = "</head>"
    body_tag = "</body>"

    input_file = open(app_name + templates_folder + '/index.html', 'rt')
    lines = input_file.read()
    lines = lines.replace(head_tag, stylesheet_string + head_tag)
    input_file.close()

    input_file = open(app_name + templates_folder + '/index.html', 'wt')
    input_file.write(lines)
    input_file.close()

    input_file = open(app_name + templates_folder + '/index.html', 'rt')
    lines = input_file.read()
    lines = lines.replace(body_tag, js_string + body_tag)
    input_file.close()

    input_file = open(app_name + templates_folder + '/index.html', 'wt')
    input_file.write(lines)
    input_file.close()

def get_cdn_library_version(github_user, library):
    if library is not 'bootstrap' and library is not 'Font-Awesome':
        with urllib.request.urlopen(f'https://api.github.com/repos/{github_user}/{library}/tags') as url:
            data = json.loads(url.read().decode())
            version = data[0]['name']
    #Using the tags on bootstrap may give us an alpha version so we use the latest release version
    else:
        with urllib.request.urlopen(f'https://api.github.com/repos/{github_user}/{library}/releases/latest') as url:
            data = json.loads(url.read().decode())
            version = data['tag_name']
    return version


def add_bootstrap(app_name, import_bootstrap):
    if import_bootstrap:
        version = get_cdn_library_version('twbs', 'bootstrap')
        version = version[1:]
        bootstrap_cdn = f'<link href="https://stackpath.bootstrapcdn.com/bootstrap/{version}/css/bootstrap.min.css" rel="stylesheet">\n'
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
        version = get_cdn_library_version('jquery', 'jquery')
        jquery_cdn = f'<script src="https://code.jquery.com/jquery-{version}.min.js" crossorigin="anonymous"></script>\n'
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
        version = get_cdn_library_version('greensock', 'GSAP')
        gsap_cdn = f'<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/{version}/gsap.min.js"></script>\n'
        body_tag = "</body>"

        input_file = open(app_name + templates_folder + '/index.html', 'rt')
        lines = input_file.read()
        lines = lines.replace(body_tag, gsap_cdn + body_tag)
        input_file.close()

        input_file = open(app_name + templates_folder + '/index.html', 'wt')
        input_file.write(lines)
        input_file.close()


def add_font_awesome(app_name, import_font_awesome):
  if import_font_awesome:
    version = get_cdn_library_version('FortAwesome', 'Font-Awesome')
    font_awesome_cdn = f'<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/{version}/css/all.min.css" rel="stylesheet">\n'
    head_tag = "</head>"

    input_file = open(app_name + templates_folder + '/index.html', 'rt')
    lines = input_file.read()
    lines = lines.replace(head_tag, font_awesome_cdn + head_tag)
    input_file.close()

    input_file = open(app_name + templates_folder + '/index.html', 'wt')
    input_file.write(lines)
    input_file.close()

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
    linePython = "version: '3.7' \nservices: \n  web: \n    build: app \n    ports: \n      - '5000:5000'"
    dockercompose_yml.writelines([linePython])
    dockercompose_yml.close()

def create_requirements_txt(app_name, flask_mode, sqlite3_mode):
  requirements_txt_file = open(app_name + '/requirements.txt', 'a')
  if (flask_mode):
    add_to_requirements(app_name, "flask")
  
  if (sqlite3_mode):
    add_to_requirements(app_name, "Flask-SQLAlchemy")

  requirements_txt_file.close()

def add_to_requirements(app_name, module_name):
  requirements_txt_file = open(app_name + '/requirements.txt', 'a')
  requirements_txt_file.write(module_name + '\n')
  requirements_txt_file.close()
