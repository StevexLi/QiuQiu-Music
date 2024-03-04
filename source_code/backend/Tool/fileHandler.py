import os
import uuid

from Tool.bucket import bucket


def save_file(file, uuid, suffix):
    filepath = './media/' + str(uuid) + suffix
    with open(filepath, 'wb') as f:
        for _ in file.chunks():
            f.write(_)
    return filepath


def upload_cover(cover, prefix_type, id):
    try:
        temp_uuid = uuid.uuid1()
        prefix = prefix_type + str(id)
        key_name = bucket.list_file(prefix)
        if key_name != 'err':
            bucket.delete_file(key_name)
        suffix = os.path.splitext(cover.name)[-1]
        key_name = prefix_type + str(id) + suffix
        cover_path = save_file(cover, temp_uuid, suffix)
        bucket.upload_file(cover_path, key_name)
        os.remove(cover_path)
    except Exception as e:
        raise e
