import os
import json


def curl_set():
    for server_sn in sn_list:
        # dhcp_info_json = os.system("curl http://nginx.dcos/dcos_oob_dep_api -d '{\"system_id\":\"sid_dcos\","
        #                           "\"user\":\"dcos\",\"command\":\"query_outband_info\",\"data\":[\"server_sn\"]}'")
        dhcp_info_json = '{"data":[{"dhcp_ip":"1.1.1.1", "SN":2100000202002}],"version":1.0}'
        # 如果包含no_info，则需重新查询,否则记录下SN与IP地址，并从set中删除
        dhcp_info = json.loads(dhcp_info_json)
        # 查找是否包含no_info
        if dhcp_info["data"][0]["dhcp_ip"] == "NO_INFO":
            print("哎呀，我碰到no_info拉！！！！" + str(count))
            continue
        # 从dhcp_info中找到IP，存入字典
        # print(server_sn)
        # TODO
        # lan_ip = os.system("mysql ")
        oob_ip = dhcp_info["data"][0]["dhcp_ip"]
        result.update({server_sn: oob_ip})
        # 将成功查询后的数据存入结果字典，并从集合中删除
        sn_set.remove(server_sn)


if __name__ == '__main__':
    sn_list = ['2100000202002', '2100000202001']
    sn_set = set(sn_list)
    result = {}
    count = 0
    NOT_INFO = "NOT_INFO"

    while sn_set:
        count += 1
        sn_list = list(sn_set)
        if count <= 100:
            curl_set()
        else:
            exit(0)

    for sn, ip in result.items():
        print(sn + "\t" + ip)
