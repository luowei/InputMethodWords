#!/usr/bin/python
# coding=utf-8

__author__ = 'luowei'

import sqlite3
import re
import codecs


conn = sqlite3.connect('test.db')
print "Opened database successfully"

conn.execute("DROP TABLE IF EXISTS wubi_words")
conn.execute('''CREATE TABLE wubi_words (id INTEGER PRIMARY KEY  NOT NULL ,
                code VARCHAR,words VARCHAR, count INTEGER DEFAULT 0,
                `num` VARCHAR(10)  DEFAULT NULL)''')

print "create table successfully"

rows = []
conn.text_factory = str

# 提示:用于检测文件编码的shell命令: file -i (linux) or file -I (osx)

# 读取txt文件
with codecs.open('wubi_words.txt', 'r','utf-16le') as f:
# with open('wubi_words.txt', 'r') as f:
    for line in f:
        # line = line.decode('utf-16le')
        line = line.strip()
        line = unicode(line).encode('utf-8')
        line = line.strip()
        if line:
            data = re.split(',|=',line)
            if len(data) == 3:
                data.extend([1])
                # print data
                # conn.execute("INSERT INTO wubi_words(count,code,words,`num`) VALUES (?,?,?,1)",data)
                rows.append(data)
            else:
                print '================:',data

# 批量插入数据集到数据库
conn.executemany("INSERT INTO wubi_words(count,code,words,`num`) VALUES (?,?,?,?)",rows)

conn.commit()
print "insert data successfully"

conn.close()