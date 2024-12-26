import argparse
from pymake.utils import str_to_bool

# def parse_arguments():
#     cpp_standards = [98, 3, 11, 14, 17, 20, 23]
#     supported_languages = ["CXX", "C", "CSharp", "CUDA", "OBJC", "OBJCXX"]
    
#     parser = argparse.ArgumentParser(prog="PyMake", description="A CMake generator for small projects")
#     parser.add_argument("project_name", type=str, help="The name of the project")
#     parser.add_argument("-v", "--version", type=str, help="Project version")
#     parser.add_argument("-l", "--languages", nargs="*", default=["CXX"], choices=supported_languages, metavar="LANG", help="Which languages needed to build the project")
#     parser.add_argument("--cxx-standard", type=int, default=17, choices=cpp_standards, help="Which version of compiler to use")
#     parser.add_argument("--cxx-standard-not-required", action="store_true", help="Whether or not to require the compiler version specified")
#     parser.add_argument("--cxx-extensions", type=str_to_bool, default=True, choices=[True, False], metavar="{on, off}", help="Whether compiler specific extensions should be used")
    
#     """Under test"""
    
#     parser.add_argument("-cdirs", "--create-dirs", action="store_true", help="Whether or not to create the default directories for the project {src, include, build}")
#     parser.add_argument("-b", "--build", action="store_true", help="Whether or not to build the project after generating the CMakeLists.txt")
#     parser.add_argument("--clean", action="store_true", help="Whether or not to clean the build directory")
    
#     return parser.parse_args()

class CommandInterface:
    def __init__(self):
        self.__cpp_standards = [98, 3, 11, 14, 17, 20, 23]
        self.__supported_languages = ["CXX", "C", "CSharp", "CUDA", "OBJC", "OBJCXX"]
        self.name = "PyMake"
        self.description = "A CMake generator for small projects"
    
    def create_parsers(self):
        self.parser = argparse.ArgumentParser(prog=self.name, description=self.description)
        self._add_subparsers()
        return self

    def _add_subparsers(self):
        self.subparsers = self.parser.add_subparsers()
        self._create_parser()
        self._build_parser()

    def _create_parser(self) -> None:
        create_parser = self.subparsers.add_parser("create", help="Create a new CMake project")
        create_parser.add_argument("project_name", type=str, help="The name of the project")
        create_parser.add_argument("-l", "--languages", nargs="*", default=["CXX"], choices=self.__supported_languages, metavar="LANG", help="Which languages needed to build the project")
        create_parser.add_argument("--cxx-standard", type=int, default=17, choices=self.__cpp_standards, help="Which version of compiler to use")
        create_parser.add_argument("--cxx-standard-not-required", action="store_true", help="Whether or not to require the compiler version specified")
        create_parser.add_argument("--cxx-extensions", type=str_to_bool, default=True, choices=[True, False], metavar="{on, off}", help="Whether compiler specific extensions should be used")
        create_parser.add_argument("-cdirs", "--create-dirs", action="store_true", help="Whether or not to create the default directories for the project {src, include, build}")
        
    def _build_parser(self) -> None:
        build_parser = self.subparsers.add_parser("build", help="Build the project")
        build_parser.add_argument("project_name", type=str, help="The name of the project")
        build_parser.add_argument("-b", "--build", action="store_true", help="Whether or not to build the project after generating the CMakeLists.txt")
        build_parser.add_argument("--clean", action="store_true", help="Whether or not to clean the build directory")

    class ParsedArguments:
        def __init__(self, namespace: argparse.Namespace):
            self.command = namespace.command
            self.project_name = namespace.project_name
            self.version = namespace.version
            self.languages = namespace.languages
            self.cxx_standard = namespace.cxx_standard
            self.cxx_standard_not_required = namespace.cxx_standard_not_required
            self.cxx_extensions = namespace.cxx_extensions
            self.create_dirs = namespace.create_dirs
            self.build = namespace.build
            self.clean = namespace.clean

    def parse_arguments(self):
        args = self.parser.parse_args()
        return self.ParsedArguments(args)