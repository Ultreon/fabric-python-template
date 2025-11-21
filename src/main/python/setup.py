import zipapp

if __name__ == '__main__':
    zipapp.create_archive("src", "examplemod.jar", compressed=True, main="exammple.__main__:init")
