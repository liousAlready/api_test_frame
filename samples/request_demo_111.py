# -*- coding: utf-8 -*-
# @Time : 2021/12/1 10:43
# @Author : Limusen
# @File : request_demo_111
import ast
import json
import requests
from common.localconfig_utlis import local_config


class RequestDemo111():

    def __init__(self):
        self.hosts = local_config.URL
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
        }
        self.session = requests.session()

    def get(self, get_info):
        url = self.hosts + get_info['请求地址']
        # print(url)
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_info['请求参数(get)']),
                                    )
        response.encoding = response.apparent_encoding  # 查看响应结果类型
        print(response.text)
        result = {
            "code": 0,  # 请求是否成功的标志位
            "response_reason": response.reason,
            "response_code": response.status_code,
            "response_header": response.headers,
            "response_json": response.json()
        }
        return result

    def post(self, post_info):
        url = self.hosts + post_info['请求地址']
        print(post_info['提交数据（post）'])
        response = self.session.post(url=url,
                                     params={
                                         "access_token": "51_xvzgkcM-QXOsTuhsf-EZFKgLpB99EJLhbEzr9DGWYmH2XC8-u0kTpPBEvCTQcQhJGJFtjFIA_IWeYpjrtuS_loDohqgvKrZeeopugpP6EhEzXAkMfqgDJKFaGzZzMvcCVc7aksQ3BLWEtEkxTHUhAFABPC"},
                                     # data=post_info['提交数据（post）'],
                                     json=post_info['提交数据（post）'],
                                     headers=self.headers
                                     )
        response.encoding = response.apparent_encoding  # 查看响应结果类型
        # print(response.text)
        result = {
            "code": 0,  # 请求是否成功的标志位
            "response_reason": response.reason,
            "response_code": response.status_code,
            "response_header": response.headers,
            "response_json": response.json()
        }
        return result


if __name__ == '__main__':
    get_info = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01',
                '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token',
                '请求参数(get)': '{"grant_type": "client_credential","appid": "wxb637f897f0bf1f0d","secret": "501123d2d367b109a5cb9a9011d0f084"}',
                '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在',
                '期望结果': 'access_token,expires_in', '测试结果': ''}
    # 把字符串转为字典      eval转换成字典模式
    # get_para = {"grant_type": "client_credential","appid": "wxb637f897f0bf1f0d","secret": "501123d2d367b109a5cb9a9011d0f084"}
    # print(eval(get_info['请求参数(get)']))
    post_info = {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口',
                 '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}',
                 '提交数据（post）': '{"tag" : {"name" : "996855"}}', '取值方式': '无', '传值变量': '', '取值代码': '',
                 '期望结果类型': 'json键值对', '期望结果': '{"errcode":45157}', '测试结果': ''}

    # RequestDemo111().get(get_info)
    RequestDemo111().post(post_info)
