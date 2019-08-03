from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_{}'.format(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))







# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# import json
# class ChatConsumer(WebsocketConsumer):
#     """ This is a synchronous WebSocket consumer that accepts all connections,
#     receives messages from its client, and echos those messages back to the same client."""
#     def connect(self):
#         # Called on connection.
#
#         # Obtain 'room_name' param from URL route in chat/routing.py
#         # that opened the WebSocket connection to the consumer.
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_{}'.format(self.room_name)
#
#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#         # To accept the WebSocket connection call:
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Called when the socket closes
#
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     # Receive message from WebSocket
#     def receive(self, text_data):
#         # Called with either text_data or bytes_data for each frame
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#
#         # Send messages to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 # An event has a 'type' key corresponding to the name of
#                 # the method that should be invoked on consumers that receive the event.
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#
#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))

