import os
import json
import requests


def get_parameter():
    env = os.environ
    param_env = env.get('DLKIT_PARAM')
    return json.loads(s=param_env)


def report_final_result(data):
    env = os.environ
    report_url = env.get('REPORT_URL') + 'final'
    trial_id = env.get('TRIAL_ID')
    exp_id = env.get('EXP_ID')
    sequence = env.get('SEQUENCE')
    req = {'metric_data': data, 'exp_id': exp_id, 'trial_id': trial_id, 'sequence':int(sequence)}
    headers = {'Content-Type': 'application/json'}
    requests.post(report_url, headers=headers, data=json.dumps(req))

def report_loss(data):
    env = os.environ
    report_url = env.get('REPORT_URL') + 'loss'
    trial_id = env.get('TRIAL_ID')
    exp_id = env.get('EXP_ID')
    req = {'loss':data, 'exp_id':exp_id, 'trial_id': trial_id}
    headers = {'Content-Type': 'application/json'}
    requests.post(report_url, headers=headers, data=json.dumps(req))

def report_intermediate_result(data):
    env = os.environ
    report_url = env.get('REPORT_URL') + 'intermediate'
    trial_id = env.get('TRIAL_ID')
    exp_id = env.get('EXP_ID')
    req = {'result':data, 'exp_id':exp_id, 'trial_id': trial_id}
    headers = {'Content-Type': 'application/json'}
    requests.post(report_url, headers=headers, data=json.dumps(req))