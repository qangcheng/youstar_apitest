# encoding: utf-8
# Author    : Davide<m13632721415@163.com >
# Datetime  : 2022/12/16 10:29
# User      : chenqang
# Product   : PyCharm
# Project   : yourstar_api_test
# File      : room_api.py
# explain   : 房间API相关接口

from api.login.login_api import iphone_login
import requests
from common.get_fields import get_filed
import time


class RoomApi(object):
    def __init__(self):
        super().__init__()
        self.url = None
        self.commonbody = get_filed("room.yml", "Creatingroom_body")
        self.commonprames = get_filed("room.yml", "common_prams")
        self.new_versioncode = "new_versioncode=" + self.commonprames['new_versioncode']
        self.debug = "debug=" + self.commonprames['debug']
        self.URL = "https://test.qmovies.tv"

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
        self.url = self.URL + "/java_room/create/?" + self.new_versioncode + '&' + self.debug
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

    def Mic_Up(self, room_id, index, token, uid):
        """
        房间上麦
        :param room_id:  上麦房间的ID
        :param index:    上麦位置
        :param token:    登录生成token
        :param uid:      登录生成uid
        :return:
        """
        self.url = self.URL + "/java_room/room_mic_up/?" + self.new_versioncode + '&' + self.debug
        body = {
            "room_id": room_id,
            "index": index,
            "token": token,
            "uid": uid
        }
        body.update(self.commonbody)
        print(body)
        r = requests.post(self.url, json=body)
        return r

    def Mic_Down(self, room_id, token, uid):
        """
        房间下麦
        :param room_id:  房间的ID，需要同一账户的上麦房间ID一致
        :param token:    登录生成token
        :param uid:      登录生成uid
        :return:
        """
        self.url = self.URL + "/java_room/room_mic_down/?" + self.new_versioncode + '&' + self.debug
        body = {
            "room_id": room_id,
            "token": token,
            "uid": uid
        }
        body.update(self.commonbody)
        r = requests.post(self.url, json=body)
        return r

    def Send_Roommsg(self, room_id, token, uid, msgType):
        """
        房间发送公屏消息
        :param room_id:  所在房间ID
        :param token:    登录生成token
        :param uid:      登录生成UID
        :param msgType:  //1:文字消息；2.图片消息
        :return:
        """
        self.url = self.URL + "/java_room/room_msg?" + self.new_versioncode + '&' + self.debug
        content = "这是一条测试消息:" + time.strftime(
            "%Y{}%m{}%d{} %H{}%M{}%S{}".format("年", "月", "日", "时", "分", "秒"))
        body = {
            "room_id": room_id,
            "token": token,
            "uid": uid,
            "content": content,
            "msgType": msgType
        }
        body.update(self.commonbody)
        r = requests.post(self.url, json=body)
        return r

    def Send_Roompicturemsg(self, room_id, token, uid, img, width, height):
        """
        公屏发送图片消息
        :param room_id: 所在房间ID
        :param token:   登录生成token
        :param uid:     登录生成UID
        :param img:     发送图片地址
        :param width:   发送图片的宽度
        :param height:  发送图片的长度
        :return:
        """
        self.url = self.URL + "/room/new/pic/send?" + self.new_versioncode + '&' + self.debug
        body = {
            "room_id": room_id,
            "token": token,
            "uid": uid,
            "img": img,
            "width": width,
            "height": height
        }
        body.update(self.commonbody)
        r = requests.post(self.url, json=body)
        return r


if __name__ == '__main__':
    rust = iphone_login("+8613632721415", "950720")
    token = rust.json()['data'].get('token')
    uid = rust.json()['data'].get('uid')
    roomid = rust.json()['data'].get('roomId')
    A = RoomApi()
    a = A.Creating_Room(token, uid, roomName="api_test_name", tagId="4", roomType="4")
    print(a.json())
    time.sleep(2)
    c = A.Mic_Up(room_id=roomid, index=0, token=token, uid=uid)
    print(c.json())
    time.sleep(5)
    v = A.Mic_Down(room_id=roomid, token=token, uid=uid)
    print(v.json())
    d = A.Send_Roommsg(room_id=roomid, token=token, uid=uid, msgType=1)
    print(d.json())
    n = A.Send_Roompicturemsg(room_id=roomid, token=token, uid=uid, img="room/1BC4C69F025349339912321E0FB90EA8.png",
                              width="1080", height="1920")
    print(n.json())
