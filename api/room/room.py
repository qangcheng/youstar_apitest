# encoding: utf-8
# Author    : Davide<m13632721415@163.com >
# Datetime  : 2022/12/16 10:29
# User      : chenqang
# Product   : PyCharm
# Project   : yourstar_api_test
# File      : room.py
# explain   : 房间API相关接口

from api.login.login_api import LoginApi
import requests
from common.get_fields import get_filed
import time


class RoomApi(LoginApi):
    def __init__(self):
        super().__init__()
        self.commonbody = get_filed("room.yml", "Creatingroom_body")
        self.commonprames = get_filed("room.yml", "common_prams")
        self.new_versioncode = "new_versioncode=" + self.commonprames['new_versioncode']
        self.debug = "debug=" + self.commonprames['debug']
        self.url = "https://test.qmovies.tv/java_room/create/?" + self.new_versioncode + '&' + self.debug

    def Creating_Room(self, token, uid, roomName, tagId, roomType):
        """
        创建房间
        :param token:     登录生成
        :param uid:       登录生成
        :param roomName:  房间名称
        :param tagId:     房间标签
        :param roomType:  房间内型：1=直播房；4=语音房
        :return: 返回值
        """
        requestTime = round(time.time()) * 1000  # 16位时间戳
        body = {
            "roomName": roomName,
            "tagId": tagId,
            "roomType": roomType,
            "token": token,
            "uid": uid,
            "requestTime": requestTime
        }
        body.update(self.commonbody)
        # print(body)
        r = requests.post(self.url, json=body)
        return r

    def Grazing_Wheat(self):
        pass


if __name__ == '__main__':
    login = LoginApi()
    rust = login.iphone_login("+8613632721415", "950720")
    token = rust[0]
    uid = rust[1]
    A = RoomApi()
    a = A.Creating_Room(token, uid, roomName="api_test_name", tagId="4", roomType="4")
    print(a.json())
