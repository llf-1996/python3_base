import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr

my_sender = '2367746876@qq.com'  # 发件人邮箱账号
my_pass = 'yourpassword'  # 发件人邮箱密码,在qq邮箱中生成授权码作为密码
my_user = '15038712879@163.com'  # 收件人邮箱账号，我这边发送给自己


def send_mail(title, message, file_path):
    '''
    发送邮件，包括附件
    :param title: 邮件主题
    :param message: 邮件正文
    :return:
    '''
    try:
        # msg = MIMEText(message, 'plain', 'utf-8')  # 纯文本邮件
        msg = MIMEMultipart()  #
        msg['From'] = formataddr(["news_controller", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["llf", my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title                 # 邮件的主题，也可以说是标题

        # 构造文字内容
        text = message
        text_plain = MIMEText(text, 'plain', 'utf-8')
        msg.attach(text_plain)

        if file_path:
            # 构造附件
            f = open(file_path, 'rb')
            sendfile = f.read()
            f.close()
            text_att = MIMEText(sendfile, 'base64', 'utf-8')
            text_att["Content-Type"] = 'application/octet-stream'
            # 以下附件可以重命名成aaa.txt
            text_att["Content-Disposition"] = 'attachment; filename="warning_log.txt"'
            # 另一种实现方式
            # text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
            # 以下中文测试不ok
            # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
            msg.attach(text_att)

        # 发送邮件
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print('邮件发送成功！')
    except Exception as e:
        print(e)
        print('邮件发送失败！')


if __name__ == "__main__":
    file_path = './warning.log'
    f = open(file_path, 'rb')
    file_text = f.read()
    f.close()
    title = 'Send Email Test'
    if file_text.strip():
        message = '异常数据见附件。'
        file_path = './warning.log'
        send_mail(title, message, file_path)
        with open(file_path, 'w') as f:
            f.write('')
    else:
        message = '无异常数据！'
        file_path = ''
        send_mail(title, message, file_path)


