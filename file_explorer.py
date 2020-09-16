from pathlib import Path
import os


class FileExplorer:
    """Class to represent a full-fledged file explorer"""
    def __init__(self):
        self.currentDirectory = Path.home()

    # FILE META
    # method to get name of cwd
    def cwdName(self):
        return self.currentDirectory.name

    # check if path is directory
    def isPathDir(self, path):
        return path.exists() and path.is_dir()

    # get info about file
    def getFileInfo(self, path: Path):
        if path.exists():
            return path.stat()

    # method to list files in current directory
    def cwdContents(self):
        # check if current path is a directory
        if not self.currentDirectory.is_dir():
            return []

        # list children
        children = []
        for child in self.currentDirectory.iterdir():
            children.append(child)

        return children

    # NAVIGATION
    # method to go 'home'
    def home(self):
        self.currentDirectory = Path.home()

    # method to 'up' the directory hierarchy
    def up(self, steps=1):
        self.currentDirectory = self.currentDirectory.parent

    # method to go 'down' the directory hierarchy
    def down(self, destination):
        for content in self.currentDirectory.iterdir():
            if content.name == destination:
                self.currentDirectory = content
                return True

        # no result found, return false
        return False

    # go to an arbitrary directory
    def goToDir(self, target):
        # check if target is absolute
        if target.exists() and target.is_dir():
            self.currentDirectory = target

    # MISC
    def getFileRep(self, file):
        fileInfo = os.stat(file)
        fileRep = {
            'name': file.name,
            'is_dir': file.is_dir(),
            'size': fileInfo.st_size
        }
        return fileRep
