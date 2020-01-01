def print_manual():
    print('Usage: create-flask-app [app_name] -[arguments]\n')
    print('Options and arguments available for creating flask apps:')
    print('  -dB or --debug\t\t Enables debugger mode on'.expandtabs(10))
    print('  -sS or --css-js\t\t Import stylesheet and script tag'.expandtabs(10))
    print('  -dC or --docker\t\t Generate Dockerfile and docker-compose.yml'.expandtabs(10))
    print('  -h or --help\t\t Print help'.expandtabs(10))