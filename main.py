"""
Project: Project Name
Author: Victor Cruz
Date Created: 2024-12-20
Last Modified: 2024-12-25
Description: This script generates a CMake file, including specifying languages and versioning, among other options.
"""

from pymake.cli import CommandInterface

def main() -> None:
    parser = CommandInterface().create_parsers()
    args = parser.parse_arguments()
    print(args)
    args.parse_commands()

if __name__ == "__main__":
    main()