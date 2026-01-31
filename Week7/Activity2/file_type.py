from abc import ABC, abstractmethod

class FileConverter(ABC):
    @abstractmethod
    def convert(self):
        pass

class JSONFileConverter():
    def convert(self):
        print("JSON FILE CREATED")

class XMLFileConverter():
    def convert(self):
        print("XML FILE CREATED")

class CSVFileConverter():
    def convert(self):
        print("CSV FILE CREATED")
