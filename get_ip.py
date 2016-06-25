import os

x = os.popen('ifconfig | grep "inet addr:19"')
y = x.read()
print y.strip().split(' ')[1].split(':')[1]
