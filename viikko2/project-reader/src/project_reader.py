from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        deserialized_content = tomli.loads(content)
        packs:dict = deserialized_content["tool"]["poetry"]["dependencies"]
        dev_packs:dict = deserialized_content["tool"]["poetry"]["group"]["dev"]["dependencies"]
        authors:list = deserialized_content["tool"]["poetry"]["authors"]
        formed_project = Project(deserialized_content["tool"]["poetry"]["name"], deserialized_content["tool"]["poetry"]["description"], list(packs.keys()), list(dev_packs.keys()), authors, deserialized_content["tool"]["poetry"]["license"])
        return formed_project
