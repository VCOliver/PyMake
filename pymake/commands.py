import os
import shutil
import subprocess
from .CMakeLists import CMakeLists
from .arguments import BuildArguments, CreateArguments
from .utils import VCOLOR, RESET_STYLE

def printv(message: str, verbose: bool) -> None:
    pymake = f"{VCOLOR}pymake:{RESET_STYLE}"
    if verbose:
        print(f"{pymake} {message}")

def build(args: BuildArguments) -> None:
    build_dir = "build"
    if args.clean:
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)
            printv(f"Removed build directory.", args.verbose)
        else:
            raise NotADirectoryError(f"Build directory does not exist: {build_dir}")
    else:
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
            printv("Created build directory.", args.verbose)
            
        subprocess.run(["cmake", "-S", ".", "-B", build_dir], check=True)
        printv("CMake files generated.", args.verbose)
        
        subprocess.run(["make", "-C", build_dir], check=True)
        printv("Project built.", args.verbose)
                
        

def create(args: CreateArguments) -> None:
    print(type(args.verbose))
    if args.create_dirs:
        dirs = ["src", "include", "build"]
        for d in dirs:
            if not os.path.exists(d):
                os.makedirs(d)
                printv(f"Created directory: {d}", args.verbose)
            else:
                printv(f"Directory already exists: {d}", args.verbose)
    cmake = CMakeLists(args.project_name, 
                       args.version, 
                       args.languages, 
                       args.cxx_standard, 
                       args.cxx_standard_not_required, 
                       args.cxx_extensions,
                       verbose=args.verbose)
    cmake.find_project_files()
    cmake.generate_cmake()