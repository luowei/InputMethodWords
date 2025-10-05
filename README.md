# InputMethodWords

输入法词库数据及相关处理脚本程序

## 项目简介

这是一个中文输入法词库资源集合项目，包含了多种输入法词库数据（拼音、五笔、英文等）以及词库处理和转换的 Python 脚本工具。项目整合了超过 120 万条搜狗细胞词库数据，为输入法开发和研究提供了丰富的数据资源。

## 技术栈

- **编程语言**: Python 2.x/3.x
- **数据库**: SQLite3
- **数据格式**: JSON, Plist, CSV, SQLite
- **主要库**: sqlite3, codecs, re

## 功能特性

1. **多种词库支持**
   - 拼音词库（基于 ibus-pinyin）
   - 五笔词库
   - 英文词库
   - 火星文词库
   - 表情符号词库（Emoji）
   - 简繁体转换词库

2. **地址数据库**
   - 全国省市区镇四级地理位置数据
   - 支持 JSON 和 SQLite 格式

3. **数据处理工具**
   - 五笔词库转 SQLite 数据库
   - 音频文件批量重命名工具
   - 支持网易云音乐、虾米音乐数据库处理

## 项目结构

```
InputMethodWords/
├── data/                          # 数据文件目录
│   ├── address_province.json      # 省级地址数据
│   ├── address_city.json          # 市级地址数据
│   ├── address_area.json          # 区级地址数据
│   ├── address_town.json          # 镇级地址数据
│   ├── address.sqlite             # 地址 SQLite 数据库
│   ├── Emoji_New.plist            # Emoji 表情数据
│   ├── EmojiImage_New.plist       # Emoji 图片数据
│   ├── EmojiString_New.plist      # Emoji 字符串数据
│   ├── emoji.ini                  # Emoji 配置文件
│   ├── emoticon.ini               # 表情符号配置
│   └── Symbol.plist               # 符号数据
├── ibus-pinyin_db/                # ibus 拼音输入法数据库
│   ├── android/                   # Android 平台相关
│   ├── open-phrase                # 开源短语库
│   ├── create_index.sql           # 创建索引 SQL
│   └── Makefile.am/in             # 编译配置文件
├── AudioFile_Rename/              # 音频文件重命名工具
│   ├── 网易云音乐_renameBySqlite.py   # 网易云音乐重命名脚本
│   ├── xmla_renameBySqlite.py         # 虾米音乐重命名脚本
│   ├── xmla_导出媒体文件列表.py        # 导出媒体列表脚本
│   ├── music_storage_v2.sqlite3       # 网易云音乐数据库
│   └── ting.sqlite                    # 虾米音乐数据库
├── 其他/                          # 其他资源文件
├── bihua_data.json                # 笔画数据
├── dict_mars.txt                  # 火星文词典
├── dict_simplify2traditional.plist # 简体转繁体词典
├── dict_traditional2smplify.plist  # 繁体转简体词典
├── en_word.plist                  # 英文单词词库
├── en_wordlist                    # 英文单词列表
├── pinyin_number.plist            # 拼音数字映射
├── pinyin-database.db.zip         # 拼音数据库压缩包
├── unicode_to_hanyu_pinyin.txt    # Unicode 到汉语拼音映射
├── wubi_words.txt                 # 五笔词库原始数据
├── wubi_words2sqlite.py           # 五笔词库转 SQLite 脚本
├── LICENSE                        # 许可证文件
└── README.md                      # 项目说明文档
```

## 依赖要求

- **Python**: 2.7+ 或 3.x
- **SQLite3**: 内置于 Python
- **必需的 Python 库**:
  - sqlite3 (标准库)
  - codecs (标准库)
  - re (标准库)

## 安装和使用

### 1. 克隆项目

```bash
git clone <repository-url>
cd InputMethodWords
```

### 2. 解压词库数据

```bash
# 解压拼音数据库
unzip pinyin-database.db.zip
```

### 3. 运行词库转换脚本

#### 五笔词库转 SQLite

```python
# 将五笔词库 txt 文件转换为 SQLite 数据库
python wubi_words2sqlite.py
```

这个脚本会：
- 读取 `wubi_words.txt` 文件（UTF-16LE 编码）
- 创建 SQLite 数据库 `test.db`
- 创建 `wubi_words` 表
- 将词库数据导入数据库

#### 音频文件重命名工具

```python
# 网易云音乐文件重命名
cd AudioFile_Rename
python 网易云音乐_renameBySqlite.py

# 虾米音乐文件重命名
python xmla_renameBySqlite.py

# 导出媒体文件列表
python xmla_导出媒体文件列表.py
```

## 数据说明

### 1. 拼音词库
- 来源：ibus-pinyin 输入法
- 格式：SQLite 数据库
- 内容：包含超过 120 万条搜狗细胞词库

### 2. 五笔词库
- 文件：wubi_words.txt
- 编码：UTF-16LE
- 格式：CSV (逗号或等号分隔)
- 字段：词频,编码,词组,数字标识

### 3. 地址数据
- 四级行政区划：省、市、区、镇
- 格式：JSON 和 SQLite
- 用途：地址输入提示、自动补全

### 4. 表情符号
- Emoji 新版数据
- 包含图片、字符串、词汇映射
- Plist 格式存储

### 5. 简繁转换
- 简体转繁体词典
- 繁体转简体词典
- Apple Plist 二进制格式

## 主要脚本说明

### wubi_words2sqlite.py

五笔词库转换脚本，主要功能：

```python
# 功能说明
1. 连接/创建 SQLite 数据库
2. 创建 wubi_words 表结构
3. 读取 UTF-16LE 编码的文本文件
4. 解析词库数据（支持逗号和等号分隔符）
5. 批量插入数据到数据库
6. 提交事务并关闭连接
```

**表结构**:
```sql
CREATE TABLE wubi_words (
    id INTEGER PRIMARY KEY NOT NULL,
    code VARCHAR,           -- 五笔编码
    words VARCHAR,          -- 词组
    count INTEGER DEFAULT 0, -- 词频
    num VARCHAR(10) DEFAULT NULL  -- 数字标识
)
```

### 音频重命名脚本

基于音乐应用的 SQLite 数据库，批量重命名本地音频文件：

- 读取音乐数据库中的歌曲元信息
- 匹配本地音频文件
- 按照 "歌手 - 歌名" 格式重命名

## 数据来源

- **搜狗细胞词库**: 120 余万词条
  - 来源：http://forum.ubuntu.org.cn/viewtopic.php?t=252407

- **hslinuxextra 项目**:
  - 来源：https://code.google.com/p/hslinuxextra/

## 应用场景

1. **输入法开发**
   - 作为词库数据源
   - 词频统计和优化
   - 智能提示和纠错

2. **中文分词**
   - 词库资源
   - 分词算法训练数据

3. **地址自动补全**
   - 地址输入提示
   - 地理位置搜索

4. **简繁转换**
   - 文本简繁体互转
   - 跨地区内容适配

5. **音乐文件管理**
   - 批量重命名
   - 音乐库整理

## 文件编码说明

处理文本文件时请注意编码格式：

```bash
# Linux 检测文件编码
file -i filename

# macOS 检测文件编码
file -I filename
```

已知编码：
- wubi_words.txt: UTF-16LE
- dict_mars.txt: UTF-8
- unicode_to_hanyu_pinyin.txt: ASCII

## 许可证

详见 [LICENSE](LICENSE) 文件

## 相关资源

- ibus-pinyin 输入法: https://github.com/ibus/ibus-pinyin
- 搜狗词库下载: https://pinyin.sogou.com/dict/
- Unicode 拼音数据: http://www.unicode.org/

## 注意事项

1. 运行脚本前请备份原始数据
2. 音频重命名工具需要确保数据库文件路径正确
3. 某些词库数据可能需要特定字符编码支持
4. SQLite 数据库文件较大，注意磁盘空间

## 贡献

欢迎提交词库数据、改进脚本或修复 Bug。
