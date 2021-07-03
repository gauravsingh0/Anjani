from pyrogram.filters import Filter, create
from pyrogram.types import Message


def chat_action() -> Filter:

    async def func(_, __, chat: Message) -> bool:
        return bool(chat.new_chat_members or chat.left_chat_member)

    return create(func, "CustomChatActionFilter")