import aiohttp
import json
from typing import Dict, Any
from loguru import logger

async def send_message(url: str, data: Dict[str, Any], headers:Dict[str, str] = None) -> Dict[str, Any]:
    """
    发消息的通用方法
    """
    if headers is None:
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
        }
        data = json.dumps(data)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as response:
           if response.headers['Content-Type'] == 'application/json':
                return await response.json()
           else:
                return await response.text()
            
            

class SendApi(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    async def send_webhook(url, msg):
        """
        webhook
        """
        data = {
            "content": msg
        }
        return await send_message(url, data)

    @staticmethod
    async def send_wecom(url, msg):
        """
        企业微信
        """
        data = {
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }
        return await send_message(url, data)

    @staticmethod
    async def send_dingtalk(url: str, msg: str) -> Dict[str, Any]:
        """
        钉钉
        """
        data = {
            "msgtype": "text",
            "text": {
                "content": msg
            }
        }
        return await send_message(url, data)

    @staticmethod
    async def send_feishu(url: str, msg: str) -> Dict[str, Any]:
        """
        飞书
        """
        data = {
            "msg_type": "text",
            "content": {
                "text": msg
            }
        }
        return await send_message(url, data)
    @staticmethod
    async def send_pushme(url: str, msg: str) -> Dict[str, Any]:
        """
        发送到pushme
        """
        from config import pushme_key
        data = {
            "push_key": pushme_key,
            "title": "京东CK更新结果",
            "type": "text",
            "content": msg
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        return await send_message(url, data, headers)
