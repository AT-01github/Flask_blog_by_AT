Mail.send_message('New message from blog' + names,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" +phone)

