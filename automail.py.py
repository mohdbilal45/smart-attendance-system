import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("SENDER_EMAIL_ADDRESS", "PASSWORD")

# sent the mail
yag.send(
    to= "RECEIVER_EMAIL_ADDRESS",
    subject= "ATTENDANCE REPORT", # email subject
    contents="Today's attendance report",  # email body
    attachments= filename  # file attached
)
print("Email Sent!")
