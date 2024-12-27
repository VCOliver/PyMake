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
        attrs = []
        for attr, value in self.__dict__.items():
            attrs.append(f"{attr}: {value}")
            
        return "CreateArguments(\n" + "\n".join(attrs) + "\n)"
        
class BuildArguments(ParsedArguments):
    def __init__(self, namespace: argparse.Namespace):
        super().__init__(namespace)
        self.clean = namespace.clean