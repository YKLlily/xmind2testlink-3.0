"""
针对新版本的xmind，没法添加备注等情况（其实主要是个人编写习惯问题，不喜欢加图标，将前言什么的都是放在用例集里面的）
这里在获取suite或者case的时候进行标题的判断
如果标题是【目的", "背景", "入口", "NOTE", "note", "Note","目标】，将节点的所有数据放到summary/details中
如果标题是【前提】，将节点的所有数据放到precondition
"""

"""
获取当前节点下所有的数据，深度优先
入参：字典
"""


def get_titles_params(suite_dict):
    if not suite_dict:
        return ""
    if isinstance(suite_dict, list):
        return "".join([get_titles_params(line) for line in suite_dict])
    return suite_dict.get("title") + get_titles_params(suite_dict.get("topics"))


"""
入参是列表，判断当前列表中是否有总结陈词之类的节点
如果有，返回True
否则，默认返回false，是需要解析的case节点
入参：字典
"""


def is_summary(suite):
    keywords = ["目的", "背景", "入口", "NOTE", "note", "Note", "目标"]
    if suite.get("title") in keywords:
        return True
    else:
        return False


"""
判断当前节点是否是前置条件
入参：字典
"""


def is_predict(step_list):
    keywords = ["前提", "前言", "前置条件"]
    if step_list.get("title") in keywords:
        return True
    return False


"""
判断当前节点是否是suite
note：根据个人的填写习惯，有可能模块的数目是不能控制的，但是个人不太喜欢加图标
所以如果是模块，那么要求title是[module,模块]开头就行
入参是字典
"""


def is_self_suite(suite):
    suite_title = suite.get("title")
    if suite_title.startswith("module") or suite_title.startswith("模块") or suite_title.startswith(
            "Module") or suite_title.startswith("MODULE"):
        return True
    return False


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


def _is_v2_by_guess(d):
    """if any sub topic from testcase node mark with priority, this can be guessed as v2 xmind. """
    for suite_node in d['topics']:
        for testcase_node in suite_node['topics']:
            sub_topics = testcase_node['topics']
            while sub_topics:
                temp_topics = []
                for _ in sub_topics:
                    temp_topics.extend(_['topics'])
                    sub_topics = temp_topics


# print(get_titles(test_case))
# if __name__ == '__main__':
#     # main()
#     test_case = {
#         "title": "根0",
#         "topics": [
#             {"title": "suite1",
#              "topics": [
#                  {"title": "case1",
#                   "topics": [
#                       {
#                           "title": "step1",
#                           "topics": [
#                               {
#                                   "title": "result1",
#                                   "topics": []
#                               }
#                           ]
#                       },
#                       {
#                           "title": "step2",
#                           "topics": [{
#                               "title": "result2",
#                               "topics": []
#                           }]
#                       }
#                   ]},
#                  {"title": "case2",
#                   "topics": [
#                       {
#                           "title": "step2.1",
#                           "topics": [
#                               {
#                                   "title": "result2.1",
#                                   "topics": []
#                               }
#                           ]
#                       },
#                       {
#                           "title": "step2.2",
#                           "topics": [{
#                               "title": "result2.2",
#                               "topics": []
#                           }]
#                       }
#                   ]
#                   }
#              ]},
#             {"title": "suite2",
#              "topics": [
#                  {"title": "case10",
#                   "topics": [
#                       {
#                           "title": "step10.1",
#                           "topics": [
#                               {
#                                   "title": "result10.1",
#                                   "topics": []
#                               }
#                           ]
#                       },
#                       {
#                           "title": "step10.2",
#                           "topics": [{
#                               "title": "result10.2",
#                               "topics": []
#                           }]
#                       }
#                   ]},
#                  {"title": "case20",
#                   "topics": [
#                       {
#                           "title": "step20.1",
#                           "topics": [
#                               {
#                                   "title": "result20.1",
#                                   "topics": []
#                               }
#                           ]
#                       },
#                       {
#                           "title": "step20.2",
#                           "topics": [{
#                               "title": "result20.2",
#                               "topics": []
#                           }]
#                       }
#                   ]
#                   }
#              ]}
#         ]
#     }
#     global title
#     titles = ""
#     # print(get_titles_params(test_case))
#     # get_titles_params(test_case)
#     _is_v2_by_guess(test_case)
#     print(title)
