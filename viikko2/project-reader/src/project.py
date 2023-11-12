class Project:
    def __init__(self, name:str, description:str, dependencies:list, dev_dependencies:list, authors:list, licence:str=None):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = licence

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __structurize_data(self, data):
        returnable_string = ""
        if len(data) > 0:
            for value in data:
                returnable_string += f"\n - {value}"
        else:
            returnable_string = "-"
        return returnable_string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"
            f"\nAuthors: {self.__structurize_data(self.authors)}\n"
            f"\nDependencies: {self.__structurize_data(self.dependencies)}\n"
            f"\nDevelopment dependencies: {self.__structurize_data(self.dev_dependencies)}\n"
        )
