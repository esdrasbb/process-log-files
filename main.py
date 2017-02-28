import file_process
import request_process

file_process.create_result('partial_log.txt', 'partial_log_result.txt')
request_list = file_process.getRequestDict('partial_log_result.txt')
not_subscribed = request_process.check_subscription(request_list)
error_not_subscribed = request_process.call_original_url(not_subscribed)
print(error_not_subscribed)
