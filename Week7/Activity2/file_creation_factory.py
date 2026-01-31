from enum import Enum
from file_type import JSONFileConverter, XMLFileConverter, CSVFileConverter

class File(Enum):
    """Define the enum for the file types"""
    CSV = "CSV"
    JSON = "JSON"
    XML = "XML"

class FileCreatorFactory:
    @staticmethod
    def create_file_convertor(file_type: File):
        if file_type == File.CSV.value:
            return CSVFileConverter()
        elif file_type == File.JSON.value:
            return JSONFileConverter()
        elif file_type == File.XML.value:
            return XMLFileConverter()
        else:
            raise ValueError("Invalid file type")