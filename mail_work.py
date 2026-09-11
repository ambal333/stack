from mail import Mail

if __name__ == '__main__':
    user_mail = Mail('mail.com','qwerty')
    user_mail.send_message()
    user_mail.recieve_message()
