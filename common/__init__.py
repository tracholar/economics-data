#coding:utf-8
import os
import json

from echart_fig import *

class Template():
    def __init__(self):
        self._template = open(os.path.dirname(__file__) + '/template.html').read()
        self._line = open(os.path.dirname(__file__) + '/plot.html').read()

    def set_title(self, title):
        self._title = title

    def add_section(self, section):
        if not hasattr(self, '_section'):
            self._section = []
        self._section.append(section)

    def _add_fig(self, option):
        if isinstance(option, EchartFig):
            option = option.get_options()

        if isinstance(option, dict):
            option = json.dumps(option)

        if not isinstance(option, str) and not isinstance(option, unicode):
            raise Exception(u'非法参数异常{}', option)

        self.add_section(self._line.replace('{option}', option))

    def add_fig(self, fig):
        assert isinstance(fig, EchartFig)
        self._add_fig(fig.get_options())

    def _body(self):
        body = ''
        if self._section is None:
            return body

        for s in self._section:
            body += '<section>{0}</section>'.format(s)

        return body

    def render(self):
        html = self._template.replace('{title}', self._title)
        html = html.replace('{body}', self._body())
        return html


def df_to_dict(df):
    data = df.to_dict()
    for k in data.keys():
        v = data[k]
        data[k] = sorted(v.items(), key=lambda x: x[0])
    return data