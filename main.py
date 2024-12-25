from pymake.CMakeLists import *

def main() -> None:
    cmake = cmake = CMakeLists(args.project_name, args.version, args.languages, args.cxx_standard, args.cxx_standard_not_required)
    cmake.find_project_files()
    cmake.generate_cmake()

if __name__ == "__main__":
    
    args = parse_arguments()
    
    if args.project_name:
        main()
    