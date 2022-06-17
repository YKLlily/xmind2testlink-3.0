def get_titles_params(suite_dict):
    # global titles
    # titles += suite_dict.get("title")
    # titles += "\n"
    # for line in suite_dict.get("topics"):
    #     titles += "\t"
    #     get_titles_params(line)
    # return
    if not suite_dict:
        return ""
    if isinstance(suite_dict,list):
        return "".join([get_titles_params(line) for line in suite_dict])
    return suite_dict.get("title")+get_titles_params(suite_dict.get("topics"))


"""
入参是列表，判断当前列表中是否有总结陈词之类的节点
如果有，返回True
否则，默认返回false，是需要解析的case节点
"""


def is_summary(suite):
    keywords = ["目的", "背景", "入口", "NOTE", "note", "Note","目标"]
    # for case in dict_list:
    #     if case.get("title") in keywords:
    #         return True
    # return False
    if suite.get("title") in keywords:
        return True
    else:
        return False


"""
入参是列表，判断当前列表中是否有前提之类的节点
如果有，返回True
否则，默认返回false，是需要解析的case节点
"""


def is_predict(step_list):
    keywords = ["前提"]
    for step in step_list:
        if step.get("title") in keywords:
            return True
    return False





test_case = {
    "title": "根0",
    "topics": [
        {"title": "suite1",
         "topics": [
             {"title": "case1",
              "topics": []},
             {"title": "case2",
              "topics": []
              }
         ]},
        {"title": "suite2",
         "topics": [
             {"title": "case10",
              "topics": []},
             {"title": "case20",
              "topics": []
              }
         ]}
    ]
}



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
if __name__ == '__main__':
    # main()
    test_case = {
        "title": "根0",
        "topics": [
            {"title": "suite1",
             "topics": [
                 {"title": "case1",
                  "topics": [
                      {
                          "title": "step1",
                          "topics":[
                              {
                                  "title":"result1",
                                  "topics":[]
                              }
                          ]
                      },
                      {
                          "title":"step2",
                          "topics":[{
                              "title":"result2",
                              "topics":[]
                          }]
                      }
                  ]},
                 {"title": "case2",
                  "topics": [
                      {
                          "title": "step2.1",
                          "topics": [
                              {
                                  "title": "result2.1",
                                  "topics": []
                              }
                          ]
                      },
                      {
                          "title": "step2.2",
                          "topics": [{
                              "title": "result2.2",
                              "topics": []
                          }]
                      }
                  ]
                  }
             ]},
            {"title": "suite2",
             "topics": [
                 {"title": "case10",
                  "topics": [
                      {
                          "title": "step10.1",
                          "topics": [
                              {
                                  "title": "result10.1",
                                  "topics": []
                              }
                          ]
                      },
                      {
                          "title": "step10.2",
                          "topics": [{
                              "title": "result10.2",
                              "topics": []
                          }]
                      }
                  ]},
                 {"title": "case20",
                  "topics": [
                      {
                          "title": "step20.1",
                          "topics": [
                              {
                                  "title": "result20.1",
                                  "topics": []
                              }
                          ]
                      },
                      {
                          "title": "step20.2",
                          "topics": [{
                              "title": "result20.2",
                              "topics": []
                          }]
                      }
                  ]
                  }
             ]}
        ]
    }
    global title
    titles = ""
    # print(get_titles_params(test_case))
   # get_titles_params(test_case)
    _is_v2_by_guess(test_case)
    print(title)
