from telethon import TelegramClient, sync
from config import *
from generate_image import *
import datetime
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest


def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.datetime.now()) != prev_time

if __name__ == '__main__':
    client = TelegramClient('avatar', api_id, api_hash)
    client.start()

    dt = datetime.datetime.now()
    date = convert_time_to_string(dt)
    a = generate(date)

    prev_update_time = ""

    while True:
        if time_has_changed(prev_update_time):
            dt = datetime.datetime.now()
            date = convert_time_to_string(dt)
            a = generate(date)

            prev_update_time = convert_time_to_string(datetime.datetime.now())
            client(DeletePhotosRequest(client.get_profile_photos('me')))
            file = client.upload_file("123.png")
            client(UploadProfilePhotoRequest(file))

