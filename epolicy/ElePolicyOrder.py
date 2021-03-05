import hashlib
import requests
from epolicy.AesCrypt import AES_Crypt
import pymysql.cursors


class VieDb:

    # def __init__(self, host, port, user, password, db_name):
    #     self.host = host
    #     self.port = port
    #     self.user = user
    #     self.password = password
    #     self.db_name = db_name
    #     self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password,
    #                          db=self.db_name, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor)
    #     self.db_cursor = self.db.cursor()

    @staticmethod
    def get_id(env, policy_no):
        '''
        param: env 数据库环境
               policy_no 保单号
        '''

        # _DB = VieDb(host="rm-bp159yy3va9am66e0.mysql.rds.aliyuncs.com",
        #             port=3306,
        #             user="guobanglu",
        #             password="guobanglu_a2dd97",
        #             db_name="vie_biz") if env == "test" else \
        #             VieDb(host="rm-bp159yy3va9am66e0.mysql.rds.aliyuncs.com",
        #             port=3306,
        #             user="guobanglu",
        #             password="guobanglu_a2dd97",
        #             db_name="vie_biz")
        #
        # with _DB.db_cursor as db:
        #     sql = f"select id from t_policy where policy_no='{policy_no}'"
        #     db.execute(sql)
        #     result = db.fetchone()
        #     if result is None:
        #         return f"未查询到该保单"
        #     else:
        #         return result["id"]
        if env == "test":
            url = "https://api-test.iyb.tm/policy/findByPolicyNo.json"
        elif env == "uat":
            url = "https://api-uat.iyb.tm/policy/findByPolicyNo.json"
        elif env == "prd":
            url = "https://api.iyb.tm/policy/findByPolicyNo.json"
        else:
            url_error = "请选中正确的环境"
            return url_error
        body = {
            "method": "post",
            "url": url,
            "json": {
                "policyNo": f"{policy_no}"
            }
        }
        result = get_req(body).json()["content"]
        if result:
            return result["id"]
        else:
            error_message = f"未查询到该保单"
            return error_message




# 加密保单id
def get_aes_policy_id(policy_id):
    key = "VRv8M+e23Q=="
    content = str(policy_id)
    _key = AES_Crypt.get_sha1prng_key(key)
    AES_Cryptor = AES_Crypt(_key, padding=AES_Crypt.PADDING_PKCS7)
    real_encrypt_res = AES_Cryptor.ECB_encrypt_to_base64(content)
    aes_policy_id = real_encrypt_res.rstrip("==")
    return aes_policy_id


def get_req(body, headers=None, **kwargs):
    if headers is None:
        headers = {
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Content-Type": "application/json"
        }
        res = requests.request(**body, headers=headers, **kwargs)
        return res


def ele_policy_order(env, aes_policy_id, channel):
    if env == "test":
        url = "https://api-test.iyb.tm/policy/electronicPolicyUrl.json"
    elif env == "uat":
        url = "https://api-test.iyb.tm/policy/electronicPolicyUrl.json"
    elif env == "prd":
        url = "https://api.iyb.tm/policy/electronicPolicyUrl.json"
    else:
        url_error = "请选中正确的环境"
        return url_error
    body = {
        "method": "post",
        "url": url,
        "json": {
            "id": aes_policy_id,
            "searchSource": channel
        }
    }
    response = get_req(body).json()["content"]
    if response["code"] == "0":
        return response["url"]
    else:
        return response["message"]


if __name__ == "__main__":
    # print(VieDb.get_id("test", "1s23"))
    id = get_aes_policy_id("229727414")
    print(ele_policy_order("uat", id, "app"))