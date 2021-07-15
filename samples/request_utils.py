# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 3:59 下午
# @Author  : Li
# @Email   : m15574933885@163.com
# @File    : request_utils.py
# @Software: PyCharm


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
            # print(self.temp_variables)  # 存入临时变量

        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_headers': response.headers,
            'response_body': response.text
        }
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
        if requests_type == "get":
            result = self.__get(step_info)
        elif requests_type == "post":
            result = self.__post(step_info)
        else:
            result = {'code': 3, "result": "请求方式不支持"}
        return result

    def request_by_step(self, step_infos):
        for step_info in step_infos:
            tmep_results = self.request(step_info)
            if tmep_results['response_code'] != 0:
                break

        return tmep_results


if __name__ == "__main__":
    # get_infos = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01',
    #              '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token',
    #              '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
    #              '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在',
    #              '期望结果': 'access_token,expires_in', '测试结果': ''}
    # post_infos = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口',
    #               '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}',
    #               '提交数据（post）': '{"tag":{"id":607}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对',
    #               '期望结果': '{"errcode":0,"errmsg":"ok"}', '测试结果': ''}
    # case_infos = [{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01',
    #                '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token',
    #                '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
    #                '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配',
    #                '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试结果': ''}, {'测试用例编号': 'case03',
    #                                                                                     '测试用例名称': '测试能否正确删除用户标签',
    #                                                                                     '用例执行': '是',
    #                                                                                     '测试用例步骤': 'step_02',
    #                                                                                     '接口名称': '删除标签接口',
    #                                                                                     '请求方式': 'post',
    #                                                                                     '请求地址': '/cgi-bin/tags/delete',
    #                                                                                     '请求参数(get)': '{"access_token":${token}}',
    #                                                                                     '提交数据（post）': '{"tag":{"id":408}}',
    #                                                                                     '取值方式': '无', '传值变量': '',
    #                                                                                     '取值代码': '', '期望结果类型': 'json键值对',
    #                                                                                     '期望结果': '{"errcode":0,"errmsg":"ok"}',
    #                                                                                     '测试结果': ''}]
    quzhi = {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口',
             '请求方式': 'get', '请求地址': '/cgi-bin/token',
             '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
             '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配',
             '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}', '测试结果': ''}
    # RequestUtils().request(get_infos)
    # RequestUtils().post(post_infos)
    # requestutils = RequestUtils()
    # for c in case_infos:
    #     requestutils.request(c)
    RequestUtils().request(quzhi)
