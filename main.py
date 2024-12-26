"""
Project: Project Name
Author: Victor Cruz
Date Created: 2024-12-20
Last Modified: 2024-12-25
Description: This script generates a CMake file, including specifying languages and versioning, among other options.
"""

from pymake.cli import CommandInterface
from pymake.CMakeLists import CMakeLists

def main() -> None:
    parser = CommandInterface().create_parsers()
    args = parser.parse_arguments()
    
    if args.command == "build":
        print("Building project...")
        
    if args.command == "create":
        cmake = CMakeLists(args.project_name, 
                        args.version, 
                        args.languages, 
                        args.cxx_standard, 
                        args.cxx_standard_not_required, 
                        args.cxx_extensions)
        cmake.find_project_files()
        cmake.generate_cmake()

if __name__ == "__main__":
    main()