class TestSuite():
    def change_name(self, name):
        self.name=name

    def __init__(self, name="", details="", sub_suites=[], testcase_list=[]):
        self.name = name
        self.details = details
        if sub_suites:
            self.sub_suites = sub_suites
        else:
            self.sub_suites = []
        if testcase_list:
            self.testcase_list = testcase_list
        else:
            self.testcase_list = []

    # sub_suites = None
    # name = ""
    # details = ""
    # testcase_list = None

    def to_dict(self):
        me = {'name': self.name,
              'details': self.details,
              'testcase_list': [],
              'sub_suites': []}

        if self.sub_suites:
            for s in self.sub_suites:
                me['sub_suites'].append(s.to_dict())

        if self.testcase_list:
            for t in self.testcase_list:
                me['testcase_list'].append(t.to_dict())

        return me


class TestCase():
    name = ""
    summary = ""
    preconditions = ""
    importance = 2
    execution_type = 1
    steps = None

    def to_dict(self):
        me = {'name': self.name,
              'summary': self.summary,
              'preconditions': self.preconditions,
              'importance': self.importance or 2,
              'execution_type': self.execution_type,
              'steps': []}

        if self.steps:
            for s in self.steps:
                me['steps'].append(s.to_dict())

        return me


class TestStep():
    number = 1
    action = ""
    expected = ""
    execution_type = 1

    def to_dict(self):
        me = {'number': self.number,
              'action': self.action,
              'expected': self.expected,
              'execution_type': self.execution_type}
        return me


cache = {}
