from threading import Thread
import requests
import smtplib
import email
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self) -> None:
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/caohao/Downloads/' + filename, 'wb') as f:
            f.write(resp.content)


def download_pic():
    thread = DownloadHandler('https://img.iplaysoft.com/wp-content/uploads/2019/free-images/free_stock_photo.jpg')
    thread.start()
    thread.join()


def mail(message, from_str: str):
    ret = True
    try:
        # 定义SMTP邮件服务器地址
        smtp_server = 'smtp.qq.com'
        # 邮件发送人邮箱
        from_addr = '705083979@qq.com'  # 自己的邮想
        # 邮件发送人邮箱密码
        password = 'jvllheeanyxxbgab'  # 邮箱密码
        # 邮件接收人
        to_addr = '705083979@qq.com'  # 测试接收邮件地址邮箱

        # 创建SMTP连接
        conn = smtplib.SMTP_SSL(smtp_server, 465)
        # 设计调试级别
        conn.set_debuglevel(1)
        # 登录邮箱
        conn.login(from_addr, password)
        # 创建邮件内容对象
        msg = email.message.EmailMessage()
        # 设置邮件内容
        msg.set_content('{}'.format(message), 'plain', 'utf-8')
        msg['Subject'] = '今日的投资建议'
        msg['From'] = from_str
        msg['To'] = '不苦'
        # 发送邮件
        conn.sendmail(from_addr, [to_addr], msg.as_string())
        # 退出连接
        conn.quit()
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret = False
        ret = False
        print(e)
    return ret


if __name__ == '__main__':
    # download_pic()
    mail('lalala', 'hahaha')