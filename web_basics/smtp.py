#!/usr/bin/env python
# coding:utf-8

import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr, formatdate

'''
Message
+- MIMEBase
   +- MIMEMultipart
   +- MIMENonMultipart
      +- MIMEMessage
      +- MIMEText
      +- MIMEImage
'''

# to create suitable format for the email
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def _add_attachment(msg, filepath, id):
    filename = filepath.split('/')[-1]
    filetype = filename.split('.')[-1]
    with open(filepath, 'rb') as f:
        mime = MIMEBase('image', filetype, filename=filename)
        # set MIME and file name, type
        mime.add_header('Content-Disposition', 'attachment', filename=filename)
        mime.add_header('Content-ID', '<%s>' % str(id))
        mime.add_header('X-Attachment-Id', str(id))
        # add header
        mime.set_payload(f.read())
        # read the attachment
        encoders.encode_base64(mime)
        # encode with base64
        msg.attach(mime)
        # add to message


# read information from a separate file
with open('smtp.txt', 'r') as f:
    from_addr = f.readline().strip()
    # email address for sender
    from_name = f.readline().strip() + '<%s>'
    # name displayed for sender
    passwd =  f.readline().strip()
    # password for sender
    to_addr = f.readline().strip()
    # email address for receiver
    to_name = f.readline().strip() + '<%s>'
    # name displayed for receiver
    smtp_server = f.readline().strip()
    # SMTP server
    smtp_port = f.readline().strip()
    # SMTP port
    # usually 25
    # Gmail 587
    # QQ 465, server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    hd = f.readline().strip()
    # header of the email

# read content of email
with open('smtp.html', 'r') as f:
    txt = ''.join(f.readlines())
    # read all the content of the html

msg = MIMEMultipart()
# create the email object
msg['From'] = _format_addr(from_name % from_addr)
# add from message
msg['To'] = _format_addr(to_name % to_addr)
# add to message
msg['Subject'] = Header(hd, 'utf-8').encode()
# add subject message
msg['Date'] = formatdate()
# add date message
msg.attach(MIMEText(txt, 'html', 'utf-8'))
# attach the email content
_add_attachment(msg, 'python1.png', 0)
_add_attachment(msg, 'python2.jpg', 1)
# add two attachments
# the first one will be put into the html content of email (see smtp.html)
# the second one is attachment

server = smtplib.SMTP(smtp_server, smtp_port)
# create the server
server.starttls()
# create safe connection
server.set_debuglevel(1)
# open debugger message
server.login(from_addr, passwd)
# server login
server.sendmail(from_addr, [to_addr], msg.as_string())
# send email
server.quit()
