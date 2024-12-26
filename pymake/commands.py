from .CMakeLists import CMakeLists

def build():
    # Add your build logic here
    print("Building the project...")

def create(args):
    cmake = CMakeLists(args.project_name, 
                       args.version, 
                       args.languages, 
                       args.cxx_standard, 
                       args.cxx_standard_not_required, 
                       args.cxx_extensions)
    cmake.find_project_files()
    cmake.generate_cmake()