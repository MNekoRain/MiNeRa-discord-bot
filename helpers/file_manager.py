
from dataclasses import dataclass

from os import listdir
from os.path import isfile, isdir, exists


arhive = []


@dataclass(order=True)
class File:
    name: str
    path: str
    current_directory: str
    format: str


@dataclass(order=True)
class Directory:
    name: str
    path: str
    current_directory: str
    objects: list[tuple]


def add(dir_path):
    objects = []
    for obj in listdir(dir_path):
        obj_ = dir_path + f"\\{obj}"
        if isfile(obj_):
            objects.append((obj, "file"))
        elif isdir(obj_):
            objects.append((obj, "directory"))
        else:
            print(f"[OPERATION][GETFILES][ADD]  Found a unknown object from {obj_}")
    
    return objects


def forInDir(self, dir):
    for obj in listdir(dir):
        obj_ = dir + f"\\{obj}"
        if obj.startswith("_"):
            continue
        if isfile(obj_):
            arhive.append(File(obj, obj_, self.getName(path=dir), self.getFormat(file=obj)))
        elif isdir(obj_):
            forInDir(self, obj_)
        else:
            print(f"[OPERATION][ALLFILES]  Found a unknown object from {obj_}")


class FileManager:
    def __init__(self, *, file_path: str = None, dir_path: str = None):
        self.file_path: str = file_path
        self.dir_path: str = dir_path

        if self.file_path is not None:
            if not exists(self.file_path) or not isfile(self.file_path):
                print(f"[FILEMANAGER][INIT]  File path {self.file_path} is not exists or is not file")
        if self.dir_path is not None:
            if not exists(self.dir_path) or not isdir(self.dir_path):
                print(f"[FILEMANAGER][INIT]  Directory path {self.dir_path} is not exists or is not directory")

    def getName(self, *, path: str = None):
        if path[::-1].find("\\") != -1:
            index = path[::-1].find("\\")
        elif path[::-1].find("/") != -1:
            index = path[::-1].find("/")
        else:
            index = 0

        return path[index:len(path)]

    def getFormat(self, *, file: str = None):
        if file is not None:
            name = file
        else:
            if self.file_path[::-1].find("\\") != -1:
                index = self.file_path[::-1].find("\\")
            elif self.file_path[::-1].find("/") != -1:
                index = self.file_path[::-1].find("/")
            else:
                index = 0
            name = self.file_path[index:len(self.file_path)]
        dot_index = len(name) - 1 - (name[::-1].find(".") if name[::-1].find(".") != -1 else 0)

        return name[dot_index:len(name)]

    def getDirectories(self):
        dirs = []
        for obj in listdir(self.dir_path):
            obj_ = self.dir_path + f"\\{obj}"
            if isdir(obj_):
                dirs.append(Directory(obj, obj_, self.getName(path=self.dir_path), add(obj_)))
        
        return dirs


    def getObjects(self):
        objects = []
        for obj in listdir(self.dir_path):
            obj_ = self.dir_path + f"\\{obj}"
            if isfile(obj_):
                objects.append(File(obj, obj_, self.getName(path=self.dir_path), self.getFormat(file=obj)))
            elif isdir(obj_):
                objects.append(Directory(obj, obj_, self.getName(self.dir_path), add(obj_)))
            else:
                print(f"[OPERATION][GETOBJECTS]  Found unknown object from {obj_}")

        return objects

    def allFiles(self):
        forInDir(self, self.dir_path)
        all_files = sorted(arhive)
        arhive.clear()
        return all_files
