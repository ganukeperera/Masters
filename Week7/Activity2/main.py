from file_creation_factory import FileCreatorFactory

def main():
    file_type = input("Enter file conversion type (csv/json/xml): ").upper()
    converter = FileCreatorFactory.create_file_convertor(file_type)
    converter.convert()

if __name__ == "__main__":
    main()
