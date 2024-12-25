"""
Project: Project Name
Author: Victor Cruz
Date Created: 2024-12-20
Last Modified: 2024-12-25
Description: This script generates a CMake file, including specifying languages and versioning, among other options.
"""


from pymake.CMakeLists import *

def main() -> None:
    cmake = cmake = CMakeLists(args.project_name, 
                               args.version, 
                               args.languages, 
                               args.cxx_standard, 
                               args.cxx_standard_not_required, 
                               args.cxx_extensions)
    cmake.find_project_files()
    cmake.generate_cmake()

if __name__ == "__main__":
    
    args = parse_arguments()
    
    if args.project_name:
        main()
    