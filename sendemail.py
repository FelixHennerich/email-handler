import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP-Einstellungen
smtp_server = 'localhost'
smtp_port = 587
smtp_username = 'hashHQ23@gmail.com'
smtp_password = '7UKtaP7EKdocbE'

# Absender- und Empfängeradresse
sender_email = 'hashHQ23@gmail.com'
receiver_email = 'fehennerich@outlook.de'

# Nachricht erstellen
subject = 'Test-E-Mail'
message = 'Hallo,\nDies ist eine Test-E-Mail von Python.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Verbindung zum SMTP-Server herstellen und E-Mail senden
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Die E-Mail wurde erfolgreich gesendet.')

except Exception as e:
    print('Fehler beim Senden der E-Mail:', str(e))

finally:
    server.quit()
