from flask import request, render_template, jsonify
from . import e_policy
# from flask_login import login_required
from epolicy import ElePolicyOrder
from loguru import logger
# import pymysql.cursors
#from settings import Config


# 电子保单查询
@e_policy.route("/e_policy_query", methods=['GET', 'POST'])
# @login_required
def e_policy_query():
    if request.method == "GET":
        return render_template('epolicy/e_policy_query.html')
    elif request.method == "POST":
        env = request.form.get("env")
        channel = request.form.get("channel")
        policy_no = request.form.get("policyNo")
        policy_id = ElePolicyOrder.VieDb.get_id(env, policy_no)
        if policy_id == "未查询到该保单":
            msg = "未查询到该保单的电子保单信息"
            return render_template('epolicy/e_policy_query.html', msg=msg)
        else:
            aes_policy_id = ElePolicyOrder.get_aes_policy_id(policy_id)
            msg = ElePolicyOrder.ele_policy_order(env, aes_policy_id, channel)
            return render_template('epolicy/e_policy_query.html', msg=msg)










