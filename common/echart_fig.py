#coding:utf-8
"""echarts fig class"""

class EchartFig(object):
    def get_options(self):
        """
        所有子类必须实现的接口，用于生成echart的options对象
        :return: dict
        """
        raise NotImplementedError()


class Line(EchartFig):

    def __init__(self, data, xlabel='x', ylabel='y',
                 xtype='category', title=None,
                 zoom_start=90, zoom_end=100):
        line = {
            "xAxis" : {
                "name" : xlabel,
                "type": xtype
            },
            "yAxis": {
                "name": ylabel,
                "type": 'value'
            },
            "series": [
            ],
            "legend": {
                "data": []
            },
            "tooltip": {
                "trigger": 'axis'
            },
            "dataZoom":[{
                "type": 'slider',
                "start": zoom_start,
                "end" : zoom_end
            }]
        }

        if isinstance(data, dict):
            for name, value in data.items():
                line['legend']["data"].append(name)
                line['series'].append({"name": name, "data" : value, "type" : "line", "showSymbol" : False})
            if title is not None:
                line['title'] = {"text": title}
            self._options = line

        else:
            raise Exception(u"data type must be dict, {}", data)

    def ylim(self, min, max):
        self._options['yAxis']['min'] = min
        self._options['yAxis']['max'] = max

    def get_options(self):
        return self._options