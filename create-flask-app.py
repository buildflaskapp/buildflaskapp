#!/usr/bin/env python3
import sys
from scripts.workflow import create_dir, create_app, create_templates_folder, create_static_folder, create_dockerfile
from scripts.manual import print_manual
from scripts.Colors import bcolors

try:
    success = False
    app_name = sys.argv[1]
except:
    print(f"{bcolors.WARNING}App name cannot be empty")
    print(f"{bcolors.FAIL}Creation of directory failed")
    sys.exit(1)
else:
    if ((app_name == 'app') or (app_name.startswith('-'))):
        if (app_name == '-h' or app_name == '--help'):
            print_manual()
        else:
            print(f'{bcolors.WARNING}Please choose another app name')
            print(f"{bcolors.FAIL}Creation of directory failed: %s" % sys.argv[1])
    else:
        try:
            create_dir(app_name)
        except FileExistsError:
            print('Directory already exists')
            sys.exit(1)
        addDebug = False
        addStyleScript = False
        if len(sys.argv) > 2:
            if '-dB' in sys.argv:
                addDebug = True
            if '-sS' in sys.argv:
                addStyleScript = True
                create_static_folder(app_name)
        else:
            print(f'{bcolors.WARNING}No options passed in')

        create_templates_folder(app_name, addStyleScript)
        create_app(app_name, addDebug)

        if '-dC' in sys.argv:
            create_dockerfile(app_name)
        print(f"{bcolors.OKGREEN}Creation of directory success: %s" % sys.argv[1])