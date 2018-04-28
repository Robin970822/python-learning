import threading
import time


def thread_job_1():
    print 'T1 start\n'
    for i in range(10):
        time.sleep(0.1)
    print 'T1 finish\n'


def thread_job_2():
    print 'T2 start\n'
    print 'T1 start\n'


def main():
    added_thread = threading.Thread(target=thread_job_1, name='T1')
    thread = threading.Thread(target=thread_job_2, name='T2')
    added_thread.start()
    thread.start()
    thread.join()
    added_thread.join()

    print 'All done\n'


if __name__ == '__main__':
    main()