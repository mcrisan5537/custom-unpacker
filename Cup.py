import os
from os import path

from FileHeader import FileHeader


class Cup:
    @staticmethod
    def create_archive(*file_paths):
        file_header_list = []

        for file_path in file_paths:
            if path.exists(path.join(os.getcwd(), file_path)):
                print('file exists')
                file_header_list.append(FileHeader.from_file(file_path))
            else:
                print("file doesn't exist")

        header_size_list = map(lambda header: header.header_size, file_header_list)
        current_offset = sum(header_size_list)
        for file_header in file_header_list:
            print(current_offset)
            file_header.set_offset(current_offset)
            current_offset += file_header.file_size

        with open('archive.cup', 'wb') as archive:
            for file_header in file_header_list:
                archive.write(file_header.header_array)

            for file_path in file_paths:
                with open(file_path, 'rb') as file:
                    while chunk := file.read(1024):
                        archive.write(chunk)

    @staticmethod
    def list(archive_path):
        pass

    def full_unpack(self):
        pass

    def unpack(self):
        pass