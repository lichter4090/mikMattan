import subprocess

# List of required libraries
required_libraries = ['pygame']

# Check for multiprocessing, time, socket, json, and select
try:
    __import__('multiprocessing')
    __import__('time')
    __import__('socket')
    __import__('json')
    __import__('select')
except ImportError as e:
    module_name = str(e).split("'")[1]
    required_libraries.append(module_name)


def check_and_install_libraries(libraries):
    for library in libraries:
        try:
            # Try importing the library
            __import__(library)
        except ImportError:
            print(f"{library} is not installed. Installing it now...")
            try:
                # Use subprocess to run pip install
                subprocess.check_call(['pip', 'install', library])
                print(f"{library} has been successfully installed.")
            except subprocess.CalledProcessError:
                print(f"Failed to install {library}. Please install it manually.")


if __name__ == "__main__":
    check_and_install_libraries(required_libraries)
