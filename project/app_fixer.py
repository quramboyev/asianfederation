from ctypes import ArgumentError
import environ
import sys
import os


def main(app_name: str) -> None:
    try:
        content = ''
        os.chdir(f'apps/{app_name}')
        with open('apps.py') as file:
            lines = file.readlines()
            last_line = lines[-1]
            index = last_line.find('"')
            if index < 0:
                index = last_line.find("'")
            lines[-1] = last_line[:index + 1] + 'apps.' + last_line[index + 1:]
            content = ''.join(lines)
        with open('apps.py', 'w') as file:
            file.write(content)
    except FileNotFoundError as err:
        print(err)
    os.chdir('../../..')
    try:
        with open('.env') as file:
            lines = file.readlines()
            lines[-1] = lines[-1].rstrip('\n') + f',apps.{app_name}'
            content = ''.join(lines)
        os.system(f'echo "{content}" > .env')
    except FileNotFoundError as err:
        print(err)


def clear(target):
    for subdir, dirs, _ in os.walk('./'):
        if subdir.split('/')[-1] == target:
            os.system(f'rm -rf {subdir}')
        for dir in dirs:
            if dir == 'migrations':
                continue
            if dir == target:
                os.system(f'rm -rf {dir}')
                continue
            print(os.curdir, '/', dir)
            try:
                os.chdir(dir)
                clear(target)
                os.chdir('../')
            except:
                pass


def clear_all_migrations():

    current_path = environ.Path(__file__) - 1
    site_root = current_path - 1
    env_file = site_root(".env")
    if os.path.exists(env_file):
        environ.Env.read_env(env_file=env_file)

    project_apps = os.environ.get('PROJECT_APPS')
    for app in project_apps.split(','):
        app = app.split(".")[-1]
        os.system(f'rm -rf apps/{app}/migrations/ && mkdir apps/{app}/migrations && touch apps/{app}/migrations/__init__.py')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ArgumentError('only one position argument app_name')
    if sys.argv[1] == 'clear_migrations':
        clear_all_migrations()
    elif sys.argv[1] == 'clear':
        if len(sys.argv) == 2:
            sys.argv.append('__pycache__')
        clear(sys.argv[-1])
    else:
        main(sys.argv[1])
