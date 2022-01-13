# AWS SDK for Python
# ドキュメントを読む癖をつける: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
import boto3
import botocore

import base64
import pprint

IMAGE_LOC = "./images/sample1.jpg"

# base64のバイナリに変換
with open(IMAGE_LOC, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    base64_binary = base64.decodebytes(encoded_string)

# AWS SDKでAPIを叩くお決まりのパターンなので覚えておく
client = boto3.client('rekognition')
# エラーハンドリングも癖にする: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html
try:
    # このAPIの引数などはドキュメント参照: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html?highlight=rekognition%20protective#Rekognition.Client.detect_protective_equipment
    response = client.detect_protective_equipment(
        Image = {
            'Bytes': base64_binary
        }
    )
    pprint.pprint(response)
except botocore.exceptions.ClientError as error:
    # エラーによるロジック実装（今回は省略）
    raise error
