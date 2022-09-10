#!/usr/bin/env python3



class Markdown:
    
    def __init__(self, path):
        self.file = open(path, 'r')

    def __del__(self):
        print("Closing file...")
        self.file.close()
        print("File closed...")


    def read_line(self):
        pass


if __name__ == '__main__':
    reader = Markdown("README.md")
    reader.read_line()