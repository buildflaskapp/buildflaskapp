import buildflaskapp
from buildflaskapp.scripts.workflow import get_app_name, is_name_valid
from buildflaskapp.scripts.workflow import get_args,  is_args_valid
from buildflaskapp.scripts.workflow import create_dir, create_app, create_templates_folder, create_static_folder, create_dockerfile
from buildflaskapp.scripts.workflow import create_requirements_txt
from buildflaskapp.scripts.manual import print_manual
from buildflaskapp.scripts.messages import empty_name, success_msg, failure_msg
from buildflaskapp.scripts.__version__ import __version__
import sys

app_name = get_app_name()
args = get_args()

def main():
    if (is_name_valid(app_name)):

        # validate all arguments first!!
        if(is_args_valid(args)):
            
            # Create folder with app_name
            create_dir(app_name)

            # Arguments
            flask_mode = True
            debugger_mode = False
            sqlite3_mode = False
            import_css_js = False
            import_bootstrap = False
            import_jquery = False
            import_gsap = False
            import_font_awesome = False
            use_docker = False


            # Checking which argument has been input
            if '-d' in args or '--debugger' in args:
                debugger_mode = True
                print("- Debugger mode on")
                print("  |__ added debug=True")

            if '-cj' in args or '--css-js' in args:
                import_css_js = True
                create_static_folder(app_name)
                print("- Css and Js mode on")
                print("  |__ import static/stylesheet/style.css")
                print("  |__ import static/js/app.css")

            if '-bs' in args or '--bootstrap' in args:
                import_bootstrap = True
                print("- Bootstrap mode on")
                print("  |__ import bootstrap CDN in templates/index.html")

            if '-jq' in args or '--jquery' in args:
                import_jquery = True
                print("- jQuery mode on")
                print("  |__ import jQuery CDN in templates/index.html")

            if '-gsap' in args or '--gsap' in args:
                import_gsap = True
                print("- GSAP mode on")
                print("  |__ import gsap CDN in templates/index.html")

            if '-fa' in args or '--font-awesome' in args:
                import_font_awesome = True
                print("- Font Awesome mode on")
                print("  |__ import font awesome CDN in templates/index.html")
            
            if '-sl3' in args or '--sqlite3' in args:
                sqlite3_mode = True
                print("- Sql Lite 3 mode on")
                print("  |__ import sqlite3")

            if '-dc' in args or '--docker-container' in args:
                use_docker = True
                print("- Docker mode on")
                print('  |__ cd %s' % app_name)
                print('  |__ \"docker-compose up -d\" to start app')

            # create templates folder to hold index.html
            create_templates_folder(app_name, import_css_js, import_bootstrap, import_jquery, import_gsap, import_font_awesome)

            # create app.py in root directory(app_name)
            create_app(app_name, debugger_mode, sqlite3_mode)

            # create a requirements.txt file for all modules

            # move application to docker container; 
            if (use_docker):
                # generate Dockerfile
                create_dockerfile(app_name)

            success_msg(app_name)
            create_requirements_txt(app_name, flask_mode, sqlite3_mode)
        else:
            print('Unknown argument detected! Please check the help section\n')
            print_manual()
            failure_msg(app_name)
    else:
        if (app_name == '-h' or app_name == '--help'):
            print_manual()
        elif (app_name == '-v' or app_name == '--version'):
            print("v{}".format(__version__))
        else:
            print('Please choose another app name')
            failure_msg(app_name)
