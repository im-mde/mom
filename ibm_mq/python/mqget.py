#!/bin/python3

# author: Matthew E. (im-mde)
# date: August 24, 2021
# summary: retrieve 1st message from specified queue


import argparse
import pymqi


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # queue manager name
    parser.add_argument(
        '-qm', '--queuemanager', help='name of queue manager',
        default='SQM1', type=str
    )
    # queue name
    parser.add_argument(
        '-q', '--queue', help='name of queue',
        default='APP1.SAMPLE1.QUEUE1', type=str
    )
    # channel name
    parser.add_argument(
        '-c', '--channel', help='name of channel',
        default='SQM1.APP1.SVRCONN', type=str
    )
    # host name or ip addresss
    parser.add_argument(
        '-hn', '--hostname', help='host name or ip address',
        default='localhost', type=str
    )
    # port number of listener
    parser.add_argument(
        '-p', '--port', help='network port value',
        default=1414, type=int
    )

    args = parser.parse_args()

    qmgr = pymqi.connect(args.queuemanager, args.channel, args.hostname)
    queue = pymqi.Queue(qmgr, args.queue)
    
    print('Message from {}:'.format(args.queue))

    try:
        print(queue.get())
    except pymqi.MQMIError as e:
        if (e.comp == pymqi.CMQC.MQCC_FAILED and 
                e.reason == pymqi.CMQC.MQRC_NO_MSG_AVAILABLE):
            print('*** Queue is empty ***')
        else:
            raise

    queue.close()
    qmgr.disconnect()
