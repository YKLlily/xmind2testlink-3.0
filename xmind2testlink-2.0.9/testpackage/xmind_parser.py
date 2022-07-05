"""
Module to parse xmind file into test suite and test case objects.
"""

import sharedparser as __
from datatype import TestSuite
from get_comments import is_summary
from get_comments import *
from get_comments import get_titles_params


def xmind_to_flat_dict(xmind_file):
    s = xmind_to_suite(xmind_file)
    return __.flat_suite(s)


def xmind_to_suite(xmind_file):
    """Auto detect and parser xmind to test suite object."""
    __.cache.clear()
    __.open_and_cache_xmind(xmind_file)

    if __.is_v2_format(__.cache['root']):
        print("v2")
        return xmind_to_suite_v2(xmind_file)
    else:
        print("v1")
        return xmind_to_suite_v1(xmind_file)


"""
在V1版本中修改，支持随意的添加module
支持输入概要以及前提内容
支持预期结果多个并且在xmind中是多条的展示
"""


def xmind_to_suite_v1(xmind_file):
    print("v1")

    # 解析子节点，且入参是字典类型
    def parse_suite(suite_dict):
        suite = TestSuite()
        suite.name = suite_dict['title']
        suite.details = suite_dict['note']
        suite.sub_suites = []
        suite.testcase_list = []
        testcase_topics = suite_dict.get('topics', [])

        for _ in testcase_topics:
            # 如果子节点有说明性节点，则放入当前节点的details中
            if is_summary(_):
                suite.details = get_titles_params(_)
            # 如果子节点是自定义的模块，那就是需要再增加suite
            elif is_self_suite(_):
                # s = parse_suite(_)
                suite.sub_suites.append(parse_suite(_))
            # 正常解析测试用例，并且将用例加到当前节点的测试用例中
            else:
                t = __.parse_testcase(_)
                suite.testcase_list.append(t)

        return suite

    __.open_and_cache_xmind(xmind_file)
    root = __.cache['root']

    suite = TestSuite()
    suite.sub_suites = []
    suite.name = root.get('title')

    for _ in root['topics']:
        # 判断当前节点是否是说明性节点,若是，则加到根目录的说明性文件中，如果否，则加到子节点中
        if is_summary(_):
            suite.details = get_titles_params(_)
        else:
            suite.sub_suites.append(parse_suite(_))

    return suite


# def xmind_to_suite_v(xmind_file):
#     #多层嵌套module的情况
#     def parse_suite_list(suite_dict,parent=None):
#         if is_summary(suite_dict):




def xmind_to_suite_v2(xmind_file):
    def parse_testcase_list(cases_dict, parent=None):

        if __.is_testcase_topic(cases_dict):
            yield __.parse_testcase(cases_dict, parent)

        else:
            if not parent:
                parent = []

            parent.append(cases_dict)
            topics = cases_dict['topics'] or []

            for child in topics:
                for _ in parse_testcase_list(child, parent):
                    yield _

            parent.pop()

    def parse_suite(suite_dict):
        suite = TestSuite()
        suite.name = suite_dict['title']
        suite.details = suite_dict['note']
        suite.testcase_list = []
        testcase_topics = suite_dict.get('topics', [])

        for node in testcase_topics:
            # 判断节点的子节点是否是备注性质的节点
            if is_summary(node):
                global titles
                titles = ""
                suite.details = get_titles_params(node)
            else:
                for t in parse_testcase_list(node):
                    suite.testcase_list.append(t)

        return suite

    __.open_and_cache_xmind(xmind_file)
    root = __.cache['root']

    suite = TestSuite()
    suite.sub_suites = []
    suite.name = root.get('title')

    for _ in root['topics']:
        if is_summary(_):
            # global title
            # title=""
            suite.details = get_titles_params(_)
        else:
            suite.sub_suites.append(parse_suite(_))

    return suite
