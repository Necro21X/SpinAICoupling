from typing import Any


class ChatMessageRequest:
    def __init__(self, msg: str, file):
        self.msg = msg
        self.file = file
        

msg = ChatMessageRequest("test", None)
