"""
A tool to parse xmind file into testlink xml file, which will help
you generate a testlink recognized xml file, then you can import it
into testlink as test suites.

Usage:
 xmind2testlink2 [path_to_xmind_file] [-json]

Example:
 xmind2testlink2 C:\\tests\\testcase.xmind       => output xml
 xmind2testlink2 C:\\tests\\testcase.xmind -json => output json

"""

import json
import sys

# from xmind2testlink2.sharedparser import get_titles, get_titles_params
# from xmind2testlink2.testlink_parser import to_testlink_xml_file
# from xmind2testlink2.xmind_parser import xmind_to_suite, xmind_to_flat_dict
from testlink_parser import *
from xmind_parser import xmind_to_suite, xmind_to_flat_dict
from get_testcase_as_comments import is_summary, is_predict


def xmind_to_testlink(xmind):
    xml_out = xmind[:-5] + 'xml'
    suite = xmind_to_suite(xmind)
    to_testlink_xml_file(suite, xml_out)
    return xml_out


def xmind_to_json(xmind):
    json_out = xmind[:-5] + 'json'
    with open(json_out, 'w', encoding='utf8') as f:
        f.write(json.dumps(xmind_to_flat_dict(xmind), indent=2))

    return json_out

def xmind_to_excel(xmind):
    excel_out =xmind[:-5]+'.xlsx'
    with open(excel_out,'w',encoding='utf8') as f:
        f.write(xmind_to_excel(xmind))
    return excel_out


def main():
    if len(sys.argv) > 1 and sys.argv[1].endswith('.xmind'):
        xmind = sys.argv[1]

        if len(sys.argv) == 3 and sys.argv[2] == '-json':
            file_out = xmind_to_json(xmind)
        elif len(sys.argv) == 3 and sys.argv[2] == '-.xls':
            file_out = xmin_to_excel(xmind)
        else:
            file_out = xmind_to_testlink(xmind)

        print('Generated: "{}"'.format(file_out))
    else:
        print(__doc__)


if __name__ == '__main__':
    # main()
    xmind = "E:\个人\测试脚本文件.xmind"
    file_out = xmind_to_testlink(xmind)
    print("generated {}".format(file_out))
    # test_case = {
    #     "title": "根0",
    #     "topics": [
    #         {"title": "suite1",
    #          "topics": [
    #              {"title": "case1",
    #               "topics": []},
    #              {"title": "case2",
    #               "topics": []
    #               }
    #          ]},
    #         {"title": "suite2",
    #          "topics": [
    #              {"title": "case10",
    #               "topics": []},
    #              {"title": "case20",
    #               "topics": []
    #               }
    #          ]}
    #     ]
    # }
    # global title
    # title=""
#  print(get_titles_params(test_case))
