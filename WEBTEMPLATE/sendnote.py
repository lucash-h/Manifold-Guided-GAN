import cgi
import smtplib

form = cgi.FieldStorage()

name = form.getvalue('name')
email = form.getvalue('email')
message = form.getvalue('message')

to = 'lhatelyhoneyman@gmail.com'
subject = 'New message from your website'
body = f"Name: {name}\nEmail: {email}\n\n{message}"

# Send email
try:
    smtp_server = 'your_smtp_server'
    smtp_port = 587
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(email, to, f'Subject: {subject}\n\n{body}')
    server.quit()
    print('Content-Type: text/plain')
    print()
    print('Message sent successfully!')
except Exception as e:
    print('Content-Type: text/plain')
    print()
    print('Error sending message:', e)