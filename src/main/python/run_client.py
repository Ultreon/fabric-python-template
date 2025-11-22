#!//usr/bin/env python3

def main():
    import sys, os, zipapp, json
    with open('pyfabric-project.json', "r") as f:
        project = json.load(f)

    minecraft_version = project['versions']['minecraft']
    fabric_loader_version = project['versions']['loader']

    os.makedirs('./run/mods/', exist_ok=True)

    zipapp.create_archive('src', './run/mods/examplemod.jar', compressed=True, main='exammple.__main__:init')

    print(f'Launching Minecraft {minecraft_version} with Fabric Loader {fabric_loader_version}...')
    os.system(f'"{sys.executable}" ./devlauncher/launch.pyz "{os.path.join(os.getcwd(), "run")}" --minecraft-version {minecraft_version} --loader-version {fabric_loader_version}')


if __name__ == '__main__':
    main()
