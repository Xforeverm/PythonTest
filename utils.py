import datetime
from const import *
import smtplib
from email.mime.text import MIMEText


def send_email(error_detail, program_name='起初系统', error_name='起初爬虫脚本'):
    """
    发送异常邮件
    """
    subject = "【程序异常提醒】{name}-{date}".format(name=program_name, date=datetime.datetime.now())  # 邮件的标题
    content = '''<div class="emailcontent" style="width:100%;max-width:720px;text-align:left;margin:0 auto;padding-top:80px;padding-bottom:20px">
            <div class="emailtitle">
                <h1 style="color:#fff;background:#51a0e3;line-height:70px;font-size:24px;font-weight:400;padding-left:40px;margin:0">程序运行异常通知</h1>
                <div class="emailtext" style="background:#fff;padding:20px 32px 20px">
                    <p style="color:#6e6e6e;font-size:13px;line-height:24px">程序：<span style="color:red;">【{program_name}】</span>运行过程中出现异常错误，下面是具体的异常信息，请及时核查处理！</p>
                    <table cellpadding="0" cellspacing="0" border="0" style="width:100%;border-top:1px solid #eee;border-left:1px solid #eee;color:#6e6e6e;font-size:16px;font-weight:normal">
                        <thead>
                            <tr>
                                <th colspan="2" style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center;background:#f8f8f8">程序异常详细信息</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center;width:100px">异常简述</td>
                                <td style="padding:10px 20px 10px 30px;border-right:1px solid #eee;border-bottom:1px solid #eee;line-height:30px">{error_name}</td>
                            </tr>
                            <tr>
                                <td style="padding:10px 0;border-right:1px solid #eee;border-bottom:1px solid #eee;text-align:center">异常详情</td>
                                <td style="padding:10px 20px 10px 30px;border-right:1px solid #eee;border-bottom:1px solid #eee;line-height:30px">{error_detail}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
            '''.format(program_name=program_name, error_name=error_name, error_detail=error_detail)  # 邮件的正文部分
    message = MIMEText(content, 'html', 'utf-8')
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receivers[0]
    try:
        smtp = smtplib.SMTP_SSL(smtp_host)
        smtp.login(email_username, email_password)
        smtp.sendmail(sender, receivers[0], message.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print(e)

