from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest
from info import REQ_CHANNEL1, REQ_CHANNEL2
from database.users_chats_db import db

if REQ_CHANNEL1 or REQ_CHANNEL2:
    channels_filter = None

    if REQ_CHANNEL1 and REQ_CHANNEL2:
        channels_filter = filters.chat(REQ_CHANNEL1) | filters.chat(REQ_CHANNEL2)
    elif REQ_CHANNEL1:
        channels_filter = filters.chat(REQ_CHANNEL1)
    elif REQ_CHANNEL2:
        channels_filter = filters.chat(REQ_CHANNEL2)

    @Client.on_chat_join_request(channels_filter)
    async def join_reqs(b, join_req: ChatJoinRequest):
        user_id = join_req.from_user.id
        try:
            if join_req.chat.id == REQ_CHANNEL1:
                if join_req.invite_link and join_req.invite_link.creator.id == b.me.id:
                    await db.add_req_one(user_id)
            elif join_req.chat.id == REQ_CHANNEL2:
                if join_req.invite_link and join_req.invite_link.creator.id == b.me.id:
                    await db.add_req_two(user_id)
        except Exception as e:
            print(f"Error adding join request: {e}")
