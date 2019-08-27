#coding:utf-8
"""
badcase自动分析脚本1
"""

import codecs
import sys

file_path = r'C:\ProgramData\Anaconda3\Lib\site-packages\pyhanlp\static\data\dictionary'
files_li = [r'person\nr.txt',
            r'person\nrf.txt',
            r'person\nrj.txt',
            r'custom\CustomDictionary.txt',
            r'custom\人名词典.txt',
            r'CoreNatureDictionary.txt']

original_text_name = r'C:\Users\yufei\git_code\information_extraction\data\命名实体识别评测语料.txt'


# 查找原文
def query_original_file(original_text_name, query_word):
    out_li = []
    with codecs.open(original_text_name, 'rb', 'utf-8', 'ignore') as infile:
        for line in infile:
            line = line.strip()
            if line:
                try:
                    text = line.split(u'\t')[0]
                except:
                    text = line
                if query_word in text:
                    out_li.append(u'%s' % text)
    out_str = u'|||'.join(out_li)
    return out_str


# 查找词典
def query_dictionary_file(file_path, files_li, query_word):
    out_li = []
    for file_name in files_li:
        with codecs.open(r'%s\%s' % (file_path, file_name), 'rb', 'utf-8', 'ignore') as infile:
            for line in infile:
                line = line.strip()
                if line:
                    items_li = line.split()
                    word = items_li[0]
                    if query_word == word:
                        out_li.append(u'%s' % file_name)
    out_str = u'|||'.join(out_li)
    return out_str


def main():
    run_type = sys.argv[1]
    if run_type == 'debug':
        while True:
            query_word = input("输入待查词语\n")
            if query_word == "q":
                break

            # 查找原文
            with codecs.open(original_text_name, 'rb', 'utf-8', 'ignore') as infile:
                for line in infile:
                    if query_word in line:
                        print(line)

            # 查找词典
            for file_name in files_li:
                with codecs.open(r'%s\%s' % (file_path, file_name), 'rb', 'utf-8', 'ignore') as infile:
                    for line in infile:
                        line = line.strip()
                        if query_word in line:
                            print(file_name, line, query_word)
    else:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        outfile = open(output_file_name, 'wb')
        with codecs.open(input_file_name, 'rb', 'utf-8', 'ignore') as infile:
            for line in infile:
                line = line.strip()
                if line:
                    out_li = []
                    print(line)
                    query_word, pos = line.split(u'/')
                    # 添加查询项
                    out_li.append(u'%s' % line)
                    # 查找原文
                    out_li.append(query_original_file(original_text_name, query_word))
                    # 查找词典
                    out_li.append(query_dictionary_file(file_path, files_li, query_word))
                    # 输出
                    out_str = u'%s\n' % (u'\t'.join(out_li))
                    outfile.write(out_str.encode('utf-8', 'ignore'))
        outfile.close()


if __name__ == '__main__':
    main()
