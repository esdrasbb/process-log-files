import re
import time

pattern_http_error = re.compile('\" [4-5][0-9][0-9] ', re.I)
pattern_create = re.compile('/create/', re.I)


# create result file with lines after regexp
def create_result(file_name, file_name_result):
    start_time = time.time()
    logger = open(file_name_result, 'w')
    for line in open(file_name):
        if re.search(pattern_http_error, line) and re.search(pattern_create, line):
            logger.write(line)
    print('Elapsed Time create_result -->' + str(time.time() - start_time))


# get all values from request and put in a dict
def getRequestDict(file_name):
    start_time = time.time()
    request_list = []
    for line in open(file_name):
        request_dict = {'originalUrl': line.split(' ')[7]}
        for pair in line.split('?')[1].split(' ')[0].split('&'):
            if pair.find('=') > 0:
                k, v = pair.split('=')
                request_dict[k] = v
        request_list.append(request_dict)
    print('Elapsed Time getRequestDict -->' + str(time.time() - start_time))
    return request_list
