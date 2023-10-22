#!/usr/bin/env python
# coding:utf-8

import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def print_info(msg, indent=0):
    # indent is used to show the hierarchy
    if indent == 0:
        # no indent, the first time to run the function
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            # get the contents in 'From', 'To', 'Subject'
            if value:
                if header == 'Subject':
                    value = decode_str(value)
                    # decode the Subject
                else:
                    hdr, addr = parseaddr(value)
                    # read from the encoded content
                    name = decode_str(hdr)
                    # decode the name from the encoded content
                    value = u'%s <%s>' % (name, addr)
                    # save the value
            print('%s%s: %s' % ('  ' * indent, header, value))
    if msg.is_multipart():
        # the msg is MIMEMultipart
        parts = msg.get_payload()
        # get the objects inside
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
            # run this function recursively with one more indent
    else:
        # indent != 0 and msg is not MIMEMultipart
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            # get the content in the msg
            charset = guess_charset(msg)
            # get the charset of content
            if charset:
                content = content.decode(charset)
                # decode using the certain charset if exists
            print('%sText: %s' % ('  ' * indent, content))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))
            # print attachment info


def decode_str(s):
    value, charset = decode_header(s)[0]
    # get the first name and charset in the list
    # ignore the cc, bcc
    if charset:
        value = value.decode(charset)
        # decode using the certain charset
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    # try to get charset directly
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        # find the charset in the content type
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
            # get the charset
    return charset

with open('pop3.txt', 'r') as f:
    email = f.readline().strip()
    passwd = f.readline().strip()
    pop3_server = f.readline().strip()

server = poplib.POP3(pop3_server)
# connect to server
# QQ server = poplib.POP3_SSL(pop3_server, '995')
server.set_debuglevel(1)
# open debugger message
print(server.getwelcome().decode('utf-8'))
# print welcome message

server.user(email)
server.pass_(passwd)
# login

print('Messages: %s. Size: %s' % server.stat())
# print message number and size
resp, mails, octets = server.list()
# return all the numbering of emails
print(mails)
# print the list of numbering
# numbering starts at 1

index = len(mails)
# the number of emails
for i in range(1, index + 1):
    print('Reading the mail No. %s ...' % i)
    resp, lines, octets = server.retr(i)
    # get a new email
    # i starts at 1
    # lines save every line of the email
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # save the text
    msg = Parser().parsestr(msg_content)
    # get the mail content and save as a Message object
    # it might be a MIMEMultipart object with several MIMEBase objects inside
    print_info(msg, indent=0)

    # server.dele(i)
    # this can delete given mail using index

server.quit()
