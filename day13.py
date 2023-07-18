import time
import multiprocessing
import random
import os
import threading
import tkinter
import tkinter.messagebox


class DownloadTask(threading.Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        download_task(self._filename)


def download_task(file_name):
    print('启动下载进程，进程号[%d].' % os.getpid())
    print('开始下载%s...' % file_name)
    time_to_download = random.randint(5, 10)
    time.sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (file_name, time_to_download))


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            time.sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(threading.Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def download_graph():

    class DownloadTaskHandler(threading.Thread):

        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    start = time.time()

    # 多进程
    # p1 = multiprocessing.Process(target=download_task, args=('1.pdf',))
    # p1.start()
    # p2 = multiprocessing.Process(target=download_task, args=('2.pdf',))
    # p2.start()
    # p1.join()  # 等待p1执行完成
    # p2.join()  # 等待p2执行完成
    # end = time.time()
    # print('总共耗费了%.2f秒.' % (end - start))

    # 多线程
    # t1 = threading.Thread(target=download_task, args=('1.pdf',))
    # t2 = threading.Thread(target=download_task, args=('2.pdf',))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # end = time.time()
    # print('总共耗费了%.2f秒.' % (end - start))

    # t1 = DownloadTask('1.pdf')
    # t2 = DownloadTask('2.pdf')
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # end = time.time()
    # print('总共耗费了%.2f秒.' % (end - start))

    # account = Account()
    # threads = []
    # for _ in range(100):
    #     t = AddMoneyThread(account, 1)
    #     threads.append(t)
    #     t.start()
    # for t in threads:
    #     t.join()
    # print('账户余额为: ￥%d元' % account.balance)

    download_graph()
