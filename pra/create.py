import json
import configparser
from tcecloud.common import credential
from tcecloud.common.profile.client_profile import ClientProfile
from tcecloud.common.profile.http_profile import HttpProfile
from tcecloud.common.exception.tce_cloud_sdk_exception import TceCloudSDKException
from tcecloud.cvm.v20170312 import cvm_client, models


class TceCvmCreate(object):
    def __init__(self, SecretId, SecretKey):
        self.SecretId = SecretId
        self.SecretKey = SecretKey

    def create_cvm(self, params):
        try:
            cred = credential.Credential(self.SecretId, self.SecretKey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "cvm.api3.tce.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = cvm_client.CvmClient(cred, "chongqing", clientProfile)

            req = models.RunInstancesRequest()
            req.from_json_string(json.dumps(params))

            resp = client.RunInstances(req)
            print(resp.to_json_string())

        except TceCloudSDKException as err:
            print(err)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("setting.ini", encoding="utf-8")

    cvm = TceCvmCreate(config.get("defaults", "SecretId"), config.get("defaults", "SecretKey"))
    params = {
        "InstanceChargeType": "POSTPAID_BY_HOUR",
        "Placement": {
            "Zone": "cqaz1"
        },
        "InstanceType": "S3.MEDIUM4",
        "ImageId": "img-cphll0yv",
        "SystemDisk": {
            "DiskType": "CLOUD_SSD",
            "DiskSize": 50
        },
        "DataDisks": [
            {
                "DiskType": "CLOUD_SSD",
                "DiskSize": 100,
                "DeleteWithInstance": True
            }
        ],
        "VirtualPrivateCloud": {
            "VpcId": "vpc-gynsaui3",
            "SubnetId": "subnet-8r1n8f1s",
            "AsVpcGateway": False,
        },
        "InstanceCount": 1,
        "InstanceName": "test-liuzhx",
        "LoginSettings": {
            "Password": "Root123456789"
        },
        "SecurityGroupIds": ["sg-az6hnjl8"],
        "EnhancedService": {
            "SecurityService": {
                "Enabled": True
            },
            "MonitorService": {
                "Enabled": True
            }
        },
        "HostName": "liuzhx",
        "DryRun": False
    }

    cvm.create_cvm(params)
