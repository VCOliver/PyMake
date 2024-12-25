import argparse
from pymake.utils import str_to_bool

def parse_arguments():
    cpp_standards = [98, 3, 11, 14, 17, 20, 23]
    supported_languages = ["CXX", "C", "CSharp", "CUDA", "OBJC", "OBJCXX"]
    
    parser = argparse.ArgumentParser(prog="PyMake", description="A CMake generator for small projects")
    parser.add_argument("project_name", type=str, help="The name of the CMake Project")
    parser.add_argument("-v", "--version", type=str, help="Project version")
    parser.add_argument("-l", "--languages", nargs="*", default=["CXX"], choices=supported_languages, metavar="LANG", help="Which languages needed to build the project")
    parser.add_argument("--cxx-standard", type=int, default=17, choices=cpp_standards, help="Which version of compiler to use")
    parser.add_argument("--cxx-standard-not-required", action="store_true", help="Whether or not to require the compiler version specified")
    parser.add_argument("--cxx-extensions", type=str_to_bool, default=True, choices=[True, False], metavar="{on, off}", help="Whether compiler specific extensions should be used")
    
    return parser.parse_args()