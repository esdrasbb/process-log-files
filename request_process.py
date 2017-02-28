import requests
import time
from xml.dom import minidom

URL_CHECK = 'http://SBS_URL_AND_PORT/subscription/check/?&phone=%(phone)s&applicationId=%(applicationId)s'
CHECK_DELAY_TIME = 0.05
SUBSCRIPTION_DELAY_TIME = 0.05


def make_url_call(url_value, tag_name):
    resp = requests.get(url_value, timeout=5.000)
    return validate_url_call(resp, tag_name)


def validate_url_call(resp, tag_name):
    return_value = False
    if resp.status_code == 200:
        xml_doc = minidom.parseString(resp.content)
        if xml_doc.getElementsByTagName(tag_name)[0].firstChild.nodeValue == 'true':
            return_value = True
    return return_value


def check_subscription(request_list):
    start_time = time.time()
    request_not_subscribed = list()
    for param in request_list:
        time.sleep(CHECK_DELAY_TIME)
        if make_url_call(URL_CHECK % param, 'exists') is not True:
            request_not_subscribed.append(request_list[0])
    print('Elapsed Time check_subscription -->' + str(time.time() - start_time))
    return request_not_subscribed


def call_original_url(request_subscription_list):
    start_time = time.time()
    request_subscription_error = list()
    for param in request_subscription_list:
        time.sleep(SUBSCRIPTION_DELAY_TIME)
        if make_url_call(param['originalUrl'], 'error') is True:
            request_subscription_error.append(param)
    print('Elapsed Time call_subscription -->' + str(time.time() - start_time))
