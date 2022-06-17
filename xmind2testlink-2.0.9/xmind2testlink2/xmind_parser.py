"""
Module to parse xmind file into test suite and test case objects.
"""

from xmind2testlink import sharedparser as __
from .datatype import TestSuite
from .test import is_summary
from .test import is_predict
from .test import get_titles_params


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


def xmind_to_suite_v1(xmind_file):
    print("v1")

    def parse_suite(suite_dict):
        suite = TestSuite()
        suite.name = suite_dict['title']
        suite.details = suite_dict['note']
        suite.testcase_list = []
        testcase_topics = suite_dict.get('topics', [])

        for _ in testcase_topics:
            t = __.parse_testcase(_)
            suite.testcase_list.append(t)

        return suite

    __.open_and_cache_xmind(xmind_file)
    root = __.cache['root']

    suite = TestSuite()
    suite.sub_suites = []

    for _ in root['topics']:
        suite.sub_suites.append(parse_suite(_))

    return suite


def xmind_to_suite_v2(xmind_file):
    print("v2")

    def parse_testcase_list(cases_dict, parent=None):

        if __.is_testcase_topic(cases_dict):
            yield __.parse_testcase(cases_dict, parent)

        else:
            if not parent:
                parent = []

            parent.append(cases_dict)
            topics = cases_dict['topics'] or []

            for child in topics:
                # # 判断当前节点是否有说明性文字的子节点
                # if is_predict(child):
                #     global title
                #     title=""
                #     predict = get_titles_params(child)

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

    for _ in root['topics']:
        if is_summary(_):
            global titles
            titles=""
            suite.details = get_titles_params(_)
        else:
            suite.sub_suites.append(parse_suite(_))

    return suite
