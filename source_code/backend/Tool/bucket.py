import re
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
from properties import *


# oss的控制类，需要能创建存储，初始化存储，上传，下载，删除，同时要有审核功能
class Bucket:
    proxies = {
        'http': '127.0.0.1:80',
        'https': '127.0.0.1:443'
    }

    def __init__(self, secret_id, secret_key, bucket_name, region, token=None):
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.region = region
        self.token = token
        self.scheme = 'https'
        self.config = CosConfig(Region=self.region, Token=self.token, SecretId=self.secret_id,
                                SecretKey=self.secret_key, Scheme=self.scheme)
        self.client = CosS3Client(self.config)

    # 文件操作类
    def upload_file(self, local_file, key_name):
        try:
            self.client.upload_file(
                Bucket=self.bucket_name,
                LocalFilePath=local_file,
                Key=key_name,
            )
        except Exception as e:
            print('err: ' + str(e))
            return -1
        else:
            return 1

    def download_file(self, key_name, dest_file_path):
        try:
            self.client.download_file(
                Bucket=self.bucket_name,
                Key=key_name,
                DestFilePath=dest_file_path,
            )
        except Exception:
            return -1
        else:
            return 1

    def delete_file(self, key_name):
        try:
            self.client.delete_object(
                Bucket=self.bucket_name,
                Key=key_name,
            )
        except Exception:
            return -1
        else:
            return 1

    def list_file(self, prefix):
        try:
            resp = self.client.list_objects(Bucket=self.bucket_name, Prefix=prefix)
            return resp.get('Contents')[0].get('Key')
        except Exception as e:
            return 'err'

    # 文件审核类
    def image_audit(self, bucket_name, key_name):
        if re.match(r'^*\.(png|jpg|jpeg|bmp|gif|webp)$', key_name) is not None:
            try:
                resp = self.client.get_object_sensitive_content_recognition(
                    Bucket=self.bucket_name,
                    Key=key_name,
                )
            except Exception:
                pass
            else:
                score = int(resp.get('Score'))
                if score < 80:
                    result = 0
                else:
                    result = 1
                return {'result': result, 'label': resp.get('Label')}
        return {'result': -1, 'label': None}

    def audio_audit_submit(self, key_name, song_id):
        if re.fullmatch(r'^.+\.(mp3|wav|aac|flac|amr|3gp|m4a|wma|ogg|ape)$', key_name) is not None:
            try:
                resp = self.client.ci_auditing_audio_submit(
                    Bucket=self.bucket_name,
                    Key=key_name,
                    Callback=BUCKET_CALLBACK_ADDRESS,
                    CallbackVersion='Simple',
                    DataId=song_id,
                )
            except Exception:
                pass
            else:
                return {'result': 1, 'job_id': str(resp)}
        return {'result': -1, 'job_id': None}

    def audio_audit_res(self, job_id):
        try:
            resp = self.client.ci_auditing_audio_query(
                Bucket=self.bucket_name,
                JobID=job_id,
            )
            return str(resp)
        except Exception as e:
            return 'query failed'


    @staticmethod
    def audio_audit_query(resp):
        if resp.get('code') == 0:
            return {
                'result': resp.get('JobsDetail').get('Result'),
                'label': resp.get('JobsDetail').get('Label'),
                'job_id': resp.get('JobsDetail').get('JobId'),
            }
        else:
            return {
                'result': -1,
                'label': None,
                'job_id': resp.get('JobsDetail').get('JobId'),
            }

bucket = Bucket(BUCKET_SECRET_ID, BUCKET_SECRET_KEY, BUCKET_NAME, BUCKET_REGION)


