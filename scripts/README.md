## Build Flask App

An easy to use flask app generator that allows users to create flask apps simply by running one command. You can check out the official website [here](https://build-flask-app.kouul.website).

<p align="center">
<img src="../img/logo.gif">
</p>

Below you will find how the functions are organised and the functions name are pretty much self-explanatory!

### Workflow.py:
##### Validate name of folder to be created
- get_app_name
- is_name_valid

##### Validate arguments passed in request
- get_args
- is_args_valid

##### Create folder
- create_dir
  - create_app
    - set_debug_on
    - set_sqlite3_mode

  - create_templates_folder
  - create_static_folder
    - add_css_js
    - add_bootstrap
    - add_jquery
    - add_gsap
    - add_font_awesome

  - create_dockerfile
  - create_requirements_txt
    - add_to_requirements(module_name)

## Manual.py