from tabulate import tabulate

def print_manual():
    print('Usage: buildflaskapp [app_name] [options]\n')

    print('Example: buildflaskapp hello-world -d -bs -gsap\n')


    print(tabulate(
        [
            ['-d', '--debugger', 'Debugger mode on'],
            ['-sl3', '--sqlite3', 'Sqlite3 mode on'],
            ['-cj', '--css-js', 'Import Stylesheet and script tag'],
            ['-bs', '--bootstrap', 'Import bootstrap'],
            ['-jq', '--jQuery', 'Import jQuery'],
            ['-gsap', '--gsap', 'Import gsap'],
            ['-fa', '--font-awesome', 'Import font awesome'],
            ['-dc', '--docker-container', 'Generate Dockerfile and docker-compose.yml'],
            ['-h', '--help', 'Print help'],
            ['-v', '--version', 'Print version']
        ],
        headers=['Options','','Description']))