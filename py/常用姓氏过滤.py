#coding:utf-8
"""
根据常用姓氏表过滤HanLP的nr.txt
"""

import codecs
import re

# 读入常用姓氏表
common_surnames_set = set()
with codecs.open('../data/dictionary/常见姓氏表.txt', 'rb', 'utf-8', 'ignore') as infile:
    for line in infile:
        line = line.strip()
        if line:
            common_surnames_set.add(line)

# 过滤nr.txt
outfile = open('nr_f.txt', 'wb')
with codecs.open(r'C:\Users\yufei\Desktop\nr.txt',
                 'rb', 'utf-8', 'ignore') as infile:
    for line in infile:
        line = line.rstrip()
        if line:
            if re.search(u'^\w .*B.*', line):
                items_li = line.split(u' ')
                if items_li[0] not in common_surnames_set:  # 不是常用姓氏，则去掉B角色
                    line_erase_b = u' '.join(re.split(u' ?B \d+ ?', line))  # 去掉角色标注
                    if len(line_erase_b.split(u' ')) >= 2:
                        out_str = u'%s\n' % line_erase_b
                        outfile.write(out_str.encode('utf-8', 'ignore'))
                else:  # 是常用姓氏
                    out_str = u'%s\n' % line
                    outfile.write(out_str.encode('utf-8', 'ignore'))
            else:
                out_str = u'%s\n' % line
                outfile.write(out_str.encode('utf-8', 'ignore'))

outfile.close()
