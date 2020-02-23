def print_manual():
    print('Usage: create-flask-app [app_name] -[arguments]\n')
    print('Options and arguments available for creating flask apps:')
    print('  -d or --debugger\t\t Enables debugger mode on'.expandtabs(10))
    print('  -cj or --css-js\t\t Import stylesheet and script tag'.expandtabs(10))
    print('  -dc or --docker-container\t\t Generate Dockerfile and docker-compose.yml'.expandtabs(10))
    print('  -h or --help\t\t Print help'.expandtabs(10))