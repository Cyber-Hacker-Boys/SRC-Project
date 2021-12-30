import asyncio
import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer


class WSConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        self.connected = True
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })

        await self.send({
            'type': 'websocket.send',
            'text': "000",
        })

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        self.connected = False
