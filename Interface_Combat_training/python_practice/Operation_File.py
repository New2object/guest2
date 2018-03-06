# coding=utf-8
'''
  在Python中对文件和目录的操作经常用到os模块和shutil模块、
  接下来主要介绍一些Operation(ɑ:pəˈreɪʃn) File and Catalog the common Method
'''

import os


class OperationFileCatalog(object):
    # 把CatalogsPath变成Class Method
    @classmethod
    def CatalogsPath(slef):
        # 获得当前 Python script job the CatalogPath: os.getcwd()
        Catalogpath = ("当前的目录路径为: %s" % (os.getcwd()))
        return Catalogpath

    @classmethod
    def ReturnAllFiles(self):
        # return 指定目录下的all Files和Catalogs Name、os.listdir() 如返回C盘下的file:
        Returnallfile = ("以list的形式返回指定目录下的所有文件和目录:  %s" % (os.listdir("C:\\")))
        return Returnallfile

    @classmethod
    def DeleteOneFile(self):
        # 删除一个文件: os.remove(filepath):
        Deleteonefile = ("删除某一个文件:  %s" % (os.remove(os.getcwd() + "\\new")))
        return Deleteonefile

    @classmethod
    def DeleteNullCatalog(self):
        # 删除多个Null Catalogs: os.removedirs(filepath)
        Deletenullcatalog = ("删除多个空目录:  %s" % (os.removedirs(os.getcwd() + "\\new2")))
        return Deletenullcatalog

    @classmethod
    def PathJudgeFile(self):
        # 判断给出的路径是否是一个文件: os.path.isfile(filepath)
        Pathjudgefile = ("判断给出的路径是否是一个文件: %s" % (os.path.isfile(os.getcwd())))
        return Pathjudgefile

    @classmethod
    def PathJudgeCatalog(self):
        # 判断给出的路径是否是一个Catalog: os.path.isdir(filepath)
        Pathjudgefile = ("判断给出的路径是否是一个目录: %s" % (os.path.isdir(os.getcwd())))
        return Pathjudgefile

    @classmethod
    def AbsPath(self):
        # 判断给出的路径是否是一个绝对路径: os.path.isabs(filepath)
        Abspath = ("判断给出的路径是否是一个绝对路径: %s" % (os.path.isabs(os.getcwd())))
        return Abspath


if __name__ == '__main__':
    catalogspath = OperationFileCatalog.CatalogsPath()
    returnallfile = OperationFileCatalog.ReturnAllFiles()
    # OperationFileCatalog.DeleteOneFile()
    # OperationFileCatalog.DeleteNullCatalog()
    pathjudgefile = OperationFileCatalog.PathJudgeFile()
    pathjudgecatalog = OperationFileCatalog.PathJudgeCatalog()
    abspath = OperationFileCatalog.AbsPath()
    print(catalogspath)
    print(returnallfile)
    print(pathjudgefile)
    print(pathjudgecatalog)
    print(abspath)
