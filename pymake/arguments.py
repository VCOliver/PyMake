import argparse

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        if "invalid choice" in message:
            invalid_command = message.split("'")[1]
            print(f"Error: '{invalid_command}' is not a valid command.")
        else:
            print(f"Error: {message}")
        print("Run 'pymake --help' for more information.")
        self.exit(2)
        
class ParsedArguments:
    def __init__(self, namespace: argparse.Namespace):
        self.__namespace = namespace
        self.verbose = namespace.verbose
        
    def parse_commands(self):
        self.__namespace.func(self.__namespace)
        
class CreateArguments(ParsedArguments):
    def __init__(self, namespace: argparse.Namespace):
        super().__init__(namespace)
        self.project_name = namespace.project_name
        self.version = namespace.version
        self.languages = namespace.languages
        self.cxx_standard = namespace.cxx_standard
        self.cxx_standard_not_required = namespace.cxx_standard_not_required
        self.cxx_extensions = namespace.cxx_extensions
        self.create_dirs = namespace.create_dirs

    def __str__(self):
        return (f"CreateArguments(project_name={self.project_name}, version={self.version}, "
                f"languages={self.languages}, cxx_standard={self.cxx_standard}, "
                f"cxx_standard_not_required={self.cxx_standard_not_required}, "
                f"cxx_extensions={self.cxx_extensions}, create_dirs={self.create_dirs}, verbose={self.verbose})")
        
class BuildArguments(ParsedArguments):
    def __init__(self, namespace: argparse.Namespace):
        super().__init__(namespace)
        self.clean = namespace.clean