#coding:utf-8
"""
将json格式的训练文件，转换为CRF格式的训练文件
"""

import codecs
import json

outfile = open('../data/train/train_file', 'wb')
with codecs.open('../data/train/subtask1_training_afterrevise.txt', 'rb', 'utf-8', 'ignore') as infile:
    for line in infile:
        line = line.strip()
        if line:
            json_data = json.loads(line)
            originalText = json_data["originalText"]
            entity_li = json_data["entities"]
            old_start_pos = 0
            old_end_pos = len(originalText)
            out_li = []
            for entity in entity_li:
                if entity["label_type"] == u"疾病和诊断":
                    start_pos = entity["start_pos"]
                    old_end_pos = start_pos
                    out_li.extend([u'\t'.join(w) for w in zip(originalText[old_start_pos: old_end_pos],
                                                                 'O'*(old_end_pos - old_start_pos))])
                    end_pos = entity["end_pos"]
                    out_li.append(u'%s\t%s' % (originalText[start_pos], 'B-DISEASE'))
                    out_li.extend([u'\t'.join(w) for w in zip(originalText[start_pos+1: end_pos],
                                                                 ['I-DISEASE'] * (end_pos - start_pos -1))])
                    old_start_pos = end_pos
                elif entity["label_type"] == u"药物":
                    start_pos = entity["start_pos"]
                    old_end_pos = start_pos
                    out_li.extend([u'\t'.join(w) for w in zip(originalText[old_start_pos: old_end_pos],
                                                              'O' * (old_end_pos - old_start_pos))])
                    end_pos = entity["end_pos"]
                    out_li.append(u'%s\t%s' % (originalText[start_pos], 'B-DRUG'))
                    out_li.extend([u'\t'.join(w) for w in zip(originalText[start_pos + 1: end_pos],
                                                              ['I-DRUG'] * (end_pos - start_pos - 1))])
                    old_start_pos = end_pos
                else:
                    pass
            if old_end_pos < len(originalText):
                old_end_pos = len(originalText)
                out_li.extend([u'\t'.join(w) for w in zip(originalText[old_start_pos: old_end_pos],
                                                             'O' * (old_end_pos - old_start_pos))])
            out_str = u'%s\n' % (u'\n'.join(out_li))
            outfile.write(out_str.encode('utf-8', 'ignore'))
outfile.close()
