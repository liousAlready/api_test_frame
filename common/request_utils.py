# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 3:59 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : request_utils.py
# @Software: PyCharm

import re
import requests
from common.localconfig_utlis import local_config
import ast
import jsonpath


class RequestUtils():

    def __init__(self):
        self.hosts = local_config.URL
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
        }
        self.session = requests.Session()
        self.temp_variables = {}  # 临时变量

    def __get(self, get_info):
        url = self.hosts + get_info['请求地址']
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_info["请求参数(get)"])
                                    )
        response.encoding = response.apparent_encoding  # 默认匹配最佳格式
        if get_info["取值方式"] == "json取值":
            value = jsonpath.jsonpath(response.json(), get_info["取值代码"])[0]
            self.temp_variables[get_info['传值变量']] = value
        elif get_info['取值方式'] == "正则取值":
            value = re.findall(get_info['取值代码'], response.text)[0]
            self.temp_variables[get_info['传值变量']] = value

        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        print(result['response_body'])
        return result

    def __post(self, post_info):
        url = self.hosts + post_info['请求地址']
        response = self.session.post(url=url,
                                     headers=self.headers,
                                     params=ast.literal_eval(post_info["请求参数(get)"]),
                                     json=ast.literal_eval(post_info['提交数据（post）'])
                                     )
        response.encoding = response.apparent_encoding  # 默认匹配最佳格式
        if post_info["取值方式"] == "json取值":
            value = jsonpath.jsonpath(response.json(), post_info["取值代码"])[0]
            self.temp_variables[post_info['传值变量']] = value
        elif post_info['取值方式'] == "正则取值":
            value = re.findall(post_info['取值代码'], response.text)[0]
            self.temp_variables[post_info['传值变量']] = value

        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
        return result

    def request(self, step_info):
        requests_type = step_info["请求方式"]
        param_variable_list = re.findall('\\${\w+}', step_info["请求参数(get)"])
        if param_variable_list:
            for param_variable in param_variable_list:
                step_info["请求参数(get)"] = step_info["请求参数(get)"].replace(param_variable,
                                                                        '"%s"' % self.temp_variables.get(
                                                                            param_variable[2:-1])
                                                                        )
        if requests_type == "get":
            result = self.__get(step_info)
        elif requests_type == "post":
            data_variable_list = re.findall('\\${\w+}', step_info["提交数据（post）"])
            if data_variable_list:
                for param_variable in data_variable_list:
                    step_info["提交数据（post）"] = step_info["提交数据（post）"].replace(param_variable,
                                                                              '"%s"' % self.temp_variables.get(
                                                                                  param_variable[2:-1])
                                                                              )
            result = self.__post(step_info)
        else:
            result = {'code': 3, "result": "请求方式不支持"}
        return result

    def request_by_step(self, step_infos):
        self.temp_variables = {}  # 临时变量
        for step_info in step_infos:
            temp_results = self.request(step_info)
            if temp_results['code'] != 0:
                break
        return temp_results


if __name__ == "__main__":
    case_info = [
        {'请求方式': 'get', '请求地址': '/cgi-bin/token',
         '请求参数(get)': '{"grant_type":"client_credential","appid":"wxb637f897f0bf1f0d","secret":"501123d2d367b109a5cb9a9011d0f084"}',
         '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配'},
        {'请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}',
         '提交数据（post）': '{"tag" : {"name" : "zxc"}}', '取值方式': '无', '传值变量': '', '取值代码': ''}
    ]
    RequestUtils().request_by_step(case_info)

