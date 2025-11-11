import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from companies.models import *

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = f"room_{self.scope['url_route']['kwargs']['id']}"
        await self.channel_layer.group_add(self.id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.id, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        
        event = {
            'type': 'send_message',
            'message': message
        }
        
        await self.channel_layer.group_send(self.id, event)
    
    async def send_message(self, event):
        data = event['message']
        await self.create_message(data=data)
        response_data = {
            'message': data['message'],
            'id': data['id']
        }
        
        await self.send(text_data=json.dumps({'message': response_data}))
    
    @database_sync_to_async
    def create_message(self, data):
        room = Room.objects.get(id=data['id'])
        if not Message.objects.filter(message=data['message']).exists():
            new_message = Message(room=room, message=data['message'])
            new_message.save()