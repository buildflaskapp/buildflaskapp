from tabulate import tabulate

def print_manual():
    print('Usage: buildflaskapp [app_name] [options]\n')

    print('Example: buildflaskapp hello-world -d -bs -gsap\n')

    print(tabulate(
        [
            ['-d', '--debugger', 'Debugger mode on'],
            ['-sl3', '--sqlite3', 'Sqlite3 mode on'],
            ['-cj', '--css-js', 'Generate css and javascript file'],
            ['-bs', '--bootstrap', 'Import bootstrap cdn'],
            ['-jq', '--jQuery', 'Import jQuery cdn'],
            ['-gsap', '--gsap', 'Import gsap cdn'],
            ['-fa', '--font-awesome', 'Import font awesome cdn'],
            ['-dc', '--docker-container', 'Generate Dockerfile and docker-compose.yml'],
            ['-h', '--help', 'Print help'],
            ['-v', '--version', 'Print version']
        ],
        headers=['Options','','Description']))