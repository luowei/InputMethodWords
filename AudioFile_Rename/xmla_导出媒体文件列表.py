#!/usr/bin/python
# coding=utf-8

__author__ = 'luowei'

import sqlite3
import re
import codecs
import os.path
import os
import re

import unicodedata
import string

validFilenameChars = "-_.() %s%s" % (string.ascii_letters, string.digits)

def removeDisallowedFilenameChars(filename):
    cleanedFilename = unicodedata.normalize('NFKD', filename).encode('ASCII', 'ignore')
    return ''.join(c for c in cleanedFilename if c in validFilenameChars)

def xstr(s):
    if s is None:
        return ''
    return s

# 获取当前目录
# cwd = os.getcwd()
# dir_path = os.path.dirname(os.path.realpath(__file__))
# dir = dir_path+'/aaa'

dir = raw_input("请输入文件夹名: ")
ting = raw_input("请输入喜玛拉雅下载目录的sqlite文件名(直接回车，默认为'ting.sqlite')：")

# def whatisthis(s):
#     if isinstance(s, str):
#         print "ordinary string"
#     elif isinstance(s, unicode):
#         print "unicode string"
#     else:
#         print "not a string"

def isUnicode(s):
    if isinstance(s, unicode):
        return True
    else:
        return False


def renameTingMp3(dirString, tingString):
    dir = unicode(dirString, "utf-8")
    ting = unicode(tingString, "utf-8")
    # pattern = re.compile("\s")
    # pattern.match(ting)
    if re.match('^\s*$',ting):
        ting = 'ting.sqlite'

    conn = sqlite3.connect(dir + '/' + ting)
    # print "Opened database successfully"

    # 输出数据库中所有的表
    # res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # for name in res:
    #     print name[0]

    cur = conn.cursor()
    cur.execute('SELECT title,filePath,artist,coverSmall,playUrl32 FROM download_table')

    rows = cur.fetchall()

    itemText = ''
    for row in rows:
        name = row[0]
        md5Name = row[1]
        artist = row[2]
        coverSmall = row[3]
        playUrl32 = row[4]

        # print(row[0])
        # namePath = dir + '/' + removeDisallowedFilenameChars(name) + '.mp3'
        # md5Path = dir + '/' + md5Name + '.mp3'
        # if os.path.exists(md5Path):
        #     os.rename(md5Path, namePath)
        #     print('修改：' + md5Path.encode('utf8') + ' 为 ' + namePath.encode('utf8'))

        name = xstr(name).replace("\"", "")
        artist = xstr(artist).replace("\"", "")
        coverSmall = xstr(coverSmall).replace("\"", "")
        playUrl32 = xstr(playUrl32).replace("\"", "")

        itemText = itemText + '''
    {
      "title": "%s",
      "artist": "%s",
      "poster": "%s",
      "mp3": "%s"
    }
        ''' % (name,artist,coverSmall,playUrl32)

        if row != rows[-1]:
            itemText = itemText + ','


    text = '''
    {
      "playlist": [
        %s
      ]
    }
        ''' % (itemText)

    with open(dir + '/' +"Output.txt", "w") as text_file:
        text_file.write(text.encode('utf8'))

    conn.close()

renameTingMp3(dir,ting)
