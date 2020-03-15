#!/usr/bin/env python3
from scripts.workflow import get_app_name, is_name_valid
from scripts.workflow import get_args,  is_args_valid
from scripts.workflow import create_dir, create_app, create_templates_folder, create_static_folder, create_dockerfile
from scripts.manual import print_manual
from scripts.messages import empty_name, success_msg, failure_msg
import sys

app_name = get_app_name()
args = get_args()
args.remove(app_name)

# validate name of app!!
if (is_name_valid(app_name)):

    # validate all arguments first!!
    if(is_args_valid(args)):
    
        # Create folder named app_name
        create_dir(app_name)

        # Arguments
        debugger_mode = False
        import_css_js = False
        import_bootstrap = False
        import_jquery = False
        import_gsap = False
        use_docker = False


        if '-d' in args or '--debugger' in args:
            debugger_mode = True
            print("- Debugger mode on")
            print("  |__ added debug=True")
        else:
            print("- Debugger mode off")

        if '-cj' in args or '--css-js' in args:
            import_css_js = True
            create_static_folder(app_name)
            print("- Css and Js mode on")
            print("  |__ import static/stylesheet/style.css")
            print("  |__ import static/js/app.css")
        else:
            print("- Css and Js mode off")

        if '-bs' in args or '--bootstrap' in args:
            import_bootstrap = True
            print("- Bootstrap mode on")
            print("  |__ import bootstrap CDN in templates/index.html")
        else:
            print("- Bootstrap mode off")

        if '-jq' in args or '--jquery' in args:
            import_jquery = True
            print("- jQuery mode on")
            print("  |__ import jQuery CDN in templates/index.html")
        else:
            print("- jQuery mode off")

        if '-gsap' in args or '--gsap' in args:
            import_gsap = True
            print("- GSAP mode on")
            print("  |__ import gsap CDN in templates/index.html")
        else:
            print("- GSAP mode off")

        if '-dc' in args or '--docker-container' in args:
            use_docker = True
            print("- Docker mode on")
            print('  |__ cd %s' % app_name)
            print('  |__ \"docker-compose up -d\" to start app')
        else:
            print("- Docker mode off")

        if '-bs' in args or '--bootstrap' in args:
            import_bootstrap = True

        if '-jq' in args or '--jQuery' in args:
            import_jquery = True

        if '-gsap' in args or '--gsap' in args:
            import_gsap = True

        # create templates folder to hold index.html
        create_templates_folder(app_name, import_css_js, import_bootstrap, import_jquery, import_gsap)

        # create app.py in root directory(app_name)
        create_app(app_name, debugger_mode)

        # move application to docker container; 
        if (use_docker):
            # generate Dockerfile
            create_dockerfile(app_name)

        success_msg(app_name)
    else:
        print('Unknown argument detected! Please check the help section\n')
        print_manual()
        failure_msg(app_name)
else:
    if (app_name == '-h' or app_name == '--help'):
        print_manual()
    else:
        print('Please choose another app name')
        failure_msg(app_name)