#!/usr/bin/python
# coding=utf-8

__author__ = 'luowei'

import sqlite3
import re
import codecs
import os.path
import os
import re
import shutil


"""
替换文件
LuoWeideMacBook-Pro:ncm luowei$ for i in *; do  mv $i ${i/128000-/}; done;
LuoWeideMacBook-Pro:ncm luowei$ for i in *; do mv $i ${i/-/}; done;
"""

# 获取当前目录
# cwd = os.getcwd()
# dir_path = os.path.dirname(os.path.realpath(__file__))
# dir = dir_path+'/aaa'

# dir = raw_input("请输入文件夹名: ")
# ting = raw_input("请输入喜玛拉雅下载目录的sqlite文件名(直接回车，默认为'ting.sqlite')：")

# def whatisthis(s):
#     if isinstance(s, str):
#         print "ordinary string"
#     elif isinstance(s, unicode):
#         print "unicode string"
#     else:
#         print "not a string"

def renameTingMp3():
    # dir = unicode(dirString, "utf-8")
    # ting = unicode(tingString, "utf-8")
    # # pattern = re.compile("\s")
    # # pattern.match(ting)
    # if re.match('^\s*$',ting):
    #     ting = 'ting.sqlite'
    #
    # conn = sqlite3.connect(dir + '/' + ting)
    # # print "Opened database successfully"

    # 输出数据库中所有的表
    # res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # for name in res:
    #     print name[0]

    dir = 'ncm'

    conn = sqlite3.connect('music_storage_v2.sqlite3')
    cur = conn.cursor()
    cur.execute('SELECT songid,type from downloadtrack')

    rows = cur.fetchall()

    for row in rows:
        songid = row[0]
        # type = row[1]

        cur.execute("SELECT name from track where songid="+str(songid))
        nameRows = cur.fetchall()
        name = nameRows[0][0]

        # print(row[0])
        # dir = os.path.dirname(os.path.realpath(__file__))
        oldName =  dir + '/' + unicode(str(songid)+'.ncm',"utf-8")
        tName = name.replace("/", "_") #替换掉名字中存在的/
        if re.match('^\s*$', tName):
            return
        # newName =   dir + '/' + tName +  '.ncm'
        newName =   dir + '/' + tName + '__' + unicode(str(songid)+'.ncm',"utf-8")
        if os.path.exists(oldName) and os.path.isfile(oldName) :
            os.rename(oldName, newName)
            # shutil.copy(oldName, 'aaa__'+oldName)
            print('修改：' + oldName.encode('utf8') + ' 为 ' + newName.encode('utf8'))

    conn.close()

renameTingMp3()