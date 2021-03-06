# -*- coding: utf-8 -*-

import sys
from netkit.contrib.tcp_client import TcpClient
from netkit.box import Box

import time

def handle(uid):
    # client = TcpClient(Box, '192.168.1.67', 29000, timeout=None)
    client = TcpClient(Box, '115.28.224.64', 29000, timeout=None)
    client.connect()

    box = Box()
    box.cmd = 1
    box.set_json(dict(
        uid=uid
    ))

    client.write(box)

    box = Box()
    box.cmd = 2

    box.set_json(dict(
        uid=uid
    ))

    client.write(box)

    t1 = time.time()

    while True:
        # 阻塞
        box = client.read()
        print 'time past: ', time.time() - t1
        print box
        if not box:
            print 'server closed'
            break


def main():
    if len(sys.argv) < 2:
        print "input uid please"
        return

    uid = int(sys.argv[1])

    handle(uid)

if __name__ == '__main__':
    main()
