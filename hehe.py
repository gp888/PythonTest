# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
#获得当前路径
root = os.getcwd()

#定义函数
def files_name(root,queryStr):
    #walk函数会返回三个元组：
    #root代表当前目录
    #dirs代表该目录下所有文件夹，包括子文件夹
    #files代表文件名称，包括子文件名称

    #遍历
    for root,dirs,files in os.walk(root,topdown=True):
        #取出文件名与路径拼接
        for name in files:
            #split返回元组（路径，文件名）
            if queryStr in name:
                print('存在文件:%s'%(os.path.join(root,name)))
#运行函数，root可以是自定义路径
# files_name(root,'.py')





def main():
    str = input('输入查询字符串：')
    path_name = input('输入查询路径（默认为工作路径）:')
    if path_name == '':
        path_name = '.'#给懒癌患者一个交代
    minus = len(path_name)

    def list_file(str,path):
        list_all =os.listdir(path)
        for name_f in list_all:
            path_c = os.path.join(path,name_f) 
            if os.path.isfile(path_c) and str in os.path.splitext(name_f)[0]:
                print(path_c[minus:])#把路径前缀去掉
            elif os.path.isdir(path_c):
                list_file(str,path_c)


    list_file(str,path_name)

if __name__ == '__main__':
    main()