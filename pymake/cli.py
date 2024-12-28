import argparse
from pymake.utils import str_to_bool
from pymake.commands import create, build
from pymake.arguments import BuildArguments, CreateArguments, CustomArgumentParser

class CommandInterface:
    def __init__(self):
        self.__cpp_standards = [98, 3, 11, 14, 17, 20, 23]
        self.__supported_languages = ["CXX", "C", "CSharp", "CUDA", "OBJC", "OBJCXX"]
        self.name = "PyMake"
        self.description = "A CMake generator for small projects"
        self.usage = "pymake <command> [options]"
    
    def create_parsers(self):
        self.parser = CustomArgumentParser(prog=self.name, usage=self.usage, description=self.description)        
        self._add_subparsers()
        return self

    def _add_subparsers(self):
        self.subparsers = self.parser.add_subparsers(dest="command", title="Commands", description="Available commands:")
        self._create_parser()
        self._build_parser()

    def _create_parser(self) -> None:
        create_parser = self.subparsers.add_parser("create", help="Create a new CMake project")
        create_parser.add_argument("project_name", type=str, help="The name of the project")
        create_parser.add_argument("-v", "--version", type=str, help="The version of the project")
        create_parser.add_argument("-l", "--languages", nargs="*", default=["CXX"], choices=self.__supported_languages, metavar="LANG", help="Which languages needed to build the project")
        create_parser.add_argument("--cxx-standard", type=int, default=17, choices=self.__cpp_standards, help="Which version of compiler to use")
        create_parser.add_argument("--cxx-standard-not-required", action="store_true", help="Whether or not to require the compiler version specified")
        create_parser.add_argument("--cxx-extensions", type=str_to_bool, default=True, choices=[True, False], metavar="{on, off}", help="Whether compiler specific extensions should be used")
        create_parser.add_argument("-C", "--create-dirs", action="store_true", help="Whether or not to create the default directories for the project {src, include, build}")
        create_parser.add_argument("--verbose", action="store_true", help="Print the steps of the project creation process")
        create_parser.set_defaults(func=create)
        
    def _build_parser(self) -> None:
        build_parser = self.subparsers.add_parser("build", help="Build the project")
        build_parser.add_argument("--clean", action="store_true", help="Whether or not to clean the build directory")
        build_parser.add_argument("--verbose", action="store_true", help="Print the steps of the build process")
        build_parser.set_defaults(func=build)

    def parse_arguments(self):
        args = self.parser.parse_args()
        if args.command == 'create':
            return CreateArguments(args)
        else:
            return BuildArguments(args)