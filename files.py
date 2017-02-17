import re


def read(path):
    return open(path)


logger = open('log-processed.txt', 'w')
for line in read('log.txt'):
    if line.find('[ERROR]') > 0:
        logger.write(re.search('\[(.*?)\]', line).group(1) + '\n')
