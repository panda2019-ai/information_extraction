#coding:utf-8
"""
评测命名实体识别的准确率
"""

import codecs

outfile_nr = open('nr_w.txt', 'wb')
outfile_ns = open('ns_w.txt', 'wb')
outfile_nt = open('nt_w.txt', 'wb')
precision_dict = dict()
with codecs.open('result.txt', 'rb', 'utf-8', 'ignore') as infile:
    for line in infile:
        line = line.strip()
        if line:
            items_li = line.split(u'\t')
            if len(items_li) == 3:
                text, old_ner_li_str, predict_ner_li_str = items_li
                if not predict_ner_li_str:
                    continue
            elif len(items_li) == 2:
                continue
            else:
                continue
            predict_ner_li = predict_ner_li_str.split(u',')
            old_ner_set = set(old_ner_li_str.split(u','))
            for ner in predict_ner_li:
                word, ner_type = ner.split(u'/')
                precision_dict.setdefault(ner_type, [0, 0])
                precision_dict[ner_type][1] += 1
                if ner in old_ner_set:  # 正确预测的实体
                    precision_dict[ner_type][0] += 1
                else:  # 错误预测的实体
                    if ner_type == u'nr':
                        out_str = u'%s\n' % ner
                        outfile_nr.write(out_str.encode('utf-8', 'ignore'))
                    elif ner_type == u'ns':
                        out_str = u'%s\n' % ner
                        outfile_ns.write(out_str.encode('utf-8', 'ignore'))
                    elif ner_type == u'nt':
                        out_str = u'%s\n' % ner
                        outfile_nt.write(out_str.encode('utf-8', 'ignore'))
                    else:
                        print('error')
for ner_type, statistic_li in precision_dict.items():
    if statistic_li[1] > 0:
        print("%s 正确预测个数%d, 预测总数%d, precision = %.2f" % (ner_type, statistic_li[0], statistic_li[1], statistic_li[0]*100.0/statistic_li[1]))

outfile_nr.close()
outfile_ns.close()
outfile_nt.close()
