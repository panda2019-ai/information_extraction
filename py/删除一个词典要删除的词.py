#coding:utf-8
"""

"""

import codecs

file_path = r'C:\ProgramData\Anaconda3\Lib\site-packages\pyhanlp\static\data\dictionary'
dictionary_file_name = r'custom\人名词典.txt'
outfile_name = r'人名词典.txt'

deleted_word_set = set()
with codecs.open('nr_w_ana.txt', 'rb', 'utf-8', 'ignore') as infile:
    for line in infile:
        line = line.strip()
        if line:
            items_li = line.split(u'\t')
            if len(items_li) == 3:
                ner, text, file_name_li_str = items_li
                ner = ner.split(u'/')[0].strip()
                file_name_set = set(file_name_li_str.split(u'|||'))
                if dictionary_file_name in file_name_set:
                    deleted_word_set.add(ner)
print(deleted_word_set)
input()
outfile = open(outfile_name, 'wb')
with codecs.open(r'%s\%s' % (file_path, dictionary_file_name), 'rb', 'utf-8', 'ignore') as infile:
    for line in infile:
        if line:
            items_li = line.split()
            word = items_li[0]
            if word in deleted_word_set:
                print("delete ", word)
                continue
            else:
                out_str = u'%s' % line
                outfile.write(out_str.encode('utf-8', 'ignore'))
outfile.close()
