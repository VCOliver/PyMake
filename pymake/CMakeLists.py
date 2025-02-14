import os
import subprocess
from .utils import VCOLOR, RESET_STYLE

class CMakeLists:    
    def __init__(self, project_name: str, 
                 proj_version:str =None, 
                 languages: list=["CXX"], 
                 cxx_std=17, 
                 cxx_stc_not_required=False,
                 cxx_extensions=True,
                 verbose=False):
        self._verbose: bool = verbose
        self.__project_name = project_name
        self.__proj_version = proj_version
        self.__languages = languages
        self.__version: str = self.__get_cmake_version()
        self.__cxx_std: int = cxx_std
        self.__cxx_std_not_required: bool = "OFF" if cxx_stc_not_required else "ON"
        self.__cxx_extensions: bool = "ON" if cxx_extensions else "OFF"
        self.__root_dir: str = os.getcwd()
        self.__src_dir: str = os.path.join(self.__root_dir, "src")
        self.__include_dir: str = os.path.join(self.__root_dir, "include")
        
    def _printv(self, message: str):
        if self._verbose:
            print(f"{VCOLOR}pymake:{RESET_STYLE} {message}")

    def __get_cmake_version(self) -> str:
        try:
            result = subprocess.run(['cmake', '--version'], capture_output=True, text=True, check=True)
            version = result.stdout.strip().split()[2]
            self._printv(f"CMake version found: {version}")
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
        self._printv(f"Languages selected: {self.__languages}")
        
        src_files = self.__find_files(self.__root_dir, extensions=extentions)
        self._printv(f"Source files found: {src_files}")
        
        if not src_files:
            raise FileNotFoundError("No source files found in 'src' directory.")
        
        self.__src_files = src_files
        
    def generate_cmake(self):
        PROJECT_NAME = r'${PROJECT_NAME}'
        SOURCES = r'${SOURCES}'
        
        version = ""
        if self.__proj_version:
            version = " VERSION "+self.__proj_version
            self._printv(f"Project version specified: {self.__proj_version}")
        
        self._printv(f"Generating CMakeLists.txt for project: '{self.__project_name}'")
        
        src_files = "\n    ".join(self.__src_files)
        languages = " ".join(self.__languages)
        
        cmake_content = f"""# -------------------------------------------------------------------
# CMake configuration file
# Automatically generated by pymake, a script developed by VCOliver
# -------------------------------------------------------------------

cmake_minimum_required(VERSION {self.__version})
project({self.__project_name}{version} LANGUAGES {languages})

# Set the C++ standard
set(CMAKE_CXX_STANDARD {self.__cxx_std})
set(CMAKE_CXX_STANDARD_REQUIRED {self.__cxx_std_not_required})
set(CMAKE_CXX_EXTENSIONS {self.__cxx_extensions})

# Include directories
include_directories(include)

# Source files
set(SOURCES
    {src_files}
)

# Add the executables
add_executable({PROJECT_NAME} {SOURCES})
"""
        
        cmake_path = os.path.join(self.__root_dir, "CMakeLists.txt")
        with open(cmake_path, "w") as cmake_file:
            cmake_file.write(cmake_content)
            
        self._printv(f"CMakeLists.txt generated in {self.__root_dir}.")
        
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