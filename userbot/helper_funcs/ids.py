# TG-UserBot - A modular Telegram UserBot script for Python.
# Copyright (C) 2019  Kandarp <https://github.com/kandnub>
#
# TG-UserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-UserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-UserBot.  If not, see <https://www.gnu.org/licenses/>.


from typing import Union

from pyrogram import Message


async def get_user_from_msg(event: Message) -> Union[int, str, None]:
    """Get a peer from a message’s text or entities.

    Args:
        event (:obj:`Message <pyrogram.Message>`):
            Pyrogram’s Message object.

    Returns:
        ``int`` | ``str`` | ``None``:
            ID or username if successful, None otherwise.
    """
    user = None
    match = event.matches[0].group(1)

    if match == "this":
        match = str(event.chat.id)

    if event.entities:
        for entity in event.entities:
            if entity.type == "text_mention":
                return entity.user.id
            elif entity.type == "mention":
                offset = entity.offset
                length = entity.length
                maxlen = offset + length
                return event.text[offset:maxlen]
    if match:
        user = int(match) if match.isdigit() else match.strip()
    return user