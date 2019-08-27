#coding:utf-8
"""

"""
import codecs
import sys
from pyhanlp import *

segment = HanLP.newSegment().enableNameRecognize(True)


# HanLP命名实体识别
def recognizeNER(text, entity_type):
    global segment
    ner_li = []
    for term in segment.seg(text):
        if str(term.nature) == u'nr':
            if entity_type == u"all" or entity_type == u"nr":
                ner_li.append(u'%s/%s' % (str(term.word), str(term.nature)))
        elif str(term.nature) == u'ns':
            if entity_type == u"all" or entity_type == u"ns":
                ner_li.append(u'%s/%s' % (str(term.word), str(term.nature)))
        elif str(term.nature) == u'nt':
            if entity_type == u"all" or entity_type == u"nt":
                ner_li.append(u'%s/%s' % (str(term.word), str(term.nature)))
    return ner_li


def main():
    run_type = sys.argv[1]
    if run_type == "debug":
        HanLP.Config.enableDebug()
        while True:
            text = input("please input your text:\n")
            if text == 'q':
                break
            print("hanlp_nr", recognizeNER(text, u'nr'))
            # print("hanlp_ns", recognizeNER(text, u'ns'))
            # print("hanlp_nt", recognizeNER(text, u'nt'))
    else:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        outfile = open(output_file_name, 'wb')
        with codecs.open(input_file_name, 'rb', 'utf-8', 'ignore') as infile:
            for line in infile:
                line = line.strip()
                if line:
                    try:
                        text, ner_li_str = line.split(u'\t')
                    except:
                        text = line
                        ner_li_str = u''
                    ner_li = recognizeNER(text, "all")
                out_str = u'%s\t%s\t%s\n' % (text, ner_li_str, u','.join(ner_li))
                outfile.write(out_str.encode('utf-8', 'ignore'))
        outfile.close()


if __name__ == "__main__":
    main()
