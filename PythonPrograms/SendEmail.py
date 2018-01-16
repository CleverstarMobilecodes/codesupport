#!/usr/bin/env python
from smtoplib import SMTP
from smtplib import SMTPException

EMAIL_SUBJECT = "Email from Python script"
EMAIL_FROM = "notification@code4reference.com"
EMAIL_RECEIVERS = ['receiverId@gmail.com']

def listToStr(lst):
    """This method makes comma separated list item string"""
    return ','.join(lst)

def send_email(msg):
    """This method sends an email""" 
  
    msg_header = "From: " + EMAIL_FROM + "\n" + \
                 "To: " + listToStr(EMAIL_RECEIVERS) + "\n" + \
                 "Subject: " + EMAIL_SUBJECT + "\n"
    msg_body =  msg_header + msg

    try:
      smtpObj = SMTP('localhost')
      smtpObj.sendmail(EMAIL_FROM, EMAIL_RECEIVERS, msg_body)
      smtpObj.quit()
    except SMTPException as error:
      print "Error: unable to send email :  {err}".format(err=error)

def main():
    """This is a simple main() function which demonstrate sending of email using smtplib."""
    send_email("Test email was generated by Python using smtplib and email libraries");

if __name__ == "__main__":
   """If this script is run as stand alone then call main() function."""
    main()
