import os
import subprocess
import argparse

def parse_arguments():
    cpp_standards = [98, 3, 11, 14, 17, 20, 23]
    supported_languages = ["CXX", "C", "CSharp", "CUDA", "OBJC", "OBJCXX"]
    
    parser = argparse.ArgumentParser(prog="PyMake", description="A CMake generator for small projects")
    parser.add_argument("project_name", type=str, help="The name of the CMake Project")
    parser.add_argument("-v", "--version", type=str, help="Project version")
    parser.add_argument("-l", "--languages", nargs="*", default="CXX", choices=supported_languages, help="Which languages needed to build the project")
    parser.add_argument("--cxx-standard", type=int, default=17, choices=cpp_standards, help="Which version of compiler to use")
    parser.add_argument("--cxx-standard-not-required", action="store_false", help="Whether or not to require the compiler version specified")
    
    return parser.parse_args()

class CMakeLists:    
    def __init__(self, project_name: str, proj_version:str =None, languages: str | list="CXX", cxx_std=17, cxx_stc_required=True):
        self.__project_name = project_name
        self.__proj_version = proj_version
        self.__languages = languages
        self.__version: str = self.__get_cmake_version()
        self.__cxx_std: int = cxx_std
        self.__cxx_std_not_required: bool = cxx_stc_required
        self.__root_dir: str = os.getcwd()
        self.__src_dir: str = os.path.join(self.__root_dir, "src")
        self.__include_dir: str = os.path.join(self.__root_dir, "include")

    def __get_cmake_version(self) -> str:
        
        try:
            # Run the 'cmake --version' command
            result = subprocess.run(['cmake', '--version'], capture_output=True, text=True, check=True)
            # Print the output
            version = result.stdout.strip().split()[2]
            return version
        except FileNotFoundError:
            RED = "\033[31m"
            RESET = "\033[0m"
            print(f"{RED}CMake is not installed or not in PATH.{RESET}")
            raise
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running CMake: {e}")
            raise
        
    def __find_files(self, start_dir: str, extensions: tuple = (".cpp", )) -> list:
        """Find files with specified extensions, ignoring 'build' directories."""
        return [
            os.path.relpath(os.path.join(dirpath, file), start=start_dir)
            for dirpath, dirnames, files in os.walk(start_dir)
            if "build" not in dirpath.split(os.sep)
            for file in files if file.endswith(extensions)
        ]
            
    def find_project_files(self):
        def parse_langs(languages: list):
            langs = languages
            extensions = []
            
            if "C" in langs:
                extensions.append(".c")
            if "CXX" in langs:
                extensions.append(".cpp")
            if "CSharp" in langs:
                extensions.append(".cs")
            if "OBJC" in langs:
                extensions.append(".m")
            if "OBJCXX" in langs:
                extensions.append(".mm")
            if "CUDA" in langs:
                extensions.append(".cu")
                
            return tuple(extensions)
                
        extentions = parse_langs(self.__languages)
        
        src_files = self.__find_files(self.__root_dir, extensions=extentions)
        #self.__include_files = self.__find_files(self.__include_dir)
        
        if not src_files:
            raise FileNotFoundError("No source files found in 'src' directory.")
        
        self.__src_files = src_files
        
    def generate_cmake(self):
        
        PROJECT_NAME = r'${PROJECT_NAME}'
        SOURCES = r'${SOURCES}'
        
        version = " VERSION "+self.__proj_version if self.__proj_version else ""
        src_files = "\n    ".join(self.__src_files)
        
        cmake_content = f"""cmake_minimum_required(VERSION {self.__version})
project({self.__project_name}{version} LANGUAGES {' '.join(self.__languages)})

# Set the C++ standard
set(CMAKE_CXX_STANDARD {self.__cxx_std})
set(CMAKE_CXX_STANDARD_REQUIRED {self.__cxx_std_not_required})

# Include directories
include_directories(include)

# Source files
set(SOURCES
    {src_files}
)

# Add the executable
add_executable({PROJECT_NAME} {SOURCES})
"""
        
        cmake_path = os.path.join(self.__root_dir, "CMakeLists.txt")
        with open(cmake_path, "w") as cmake_file:
            cmake_file.write(cmake_content)
            
        print(f"CMakeLists.txt generated in {self.__root_dir}.")
        
    @property
    def project_name(self):
        return self.__project_name
    
    @project_name.setter
    def project_name(self, newname: str):
        if not isinstance(newname, str):
            raise TypeError("Name must be of type string.")
        self.__project_name = newname
        
    @property
    def cmake_version(self):
        return self.__version
    