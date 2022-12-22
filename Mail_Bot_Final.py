import smtplib
import os.path
from email.message import EmailMessage

sender = "jiteshece@gmail.com"
user_pass = "kdhrzpxxcdrcftp"

sent_from = "Jitesh Kumar"
sent_to_bcc = "vinishbhaskar321@gmail.com"
sent_to_cc = "mefisat690@lubde.com"
sent_to = ["jiteshece@gmail.com", "jitesbharti@gmail.com"]


Company_Name = "MicroSoft"
subject = f"Interest in applying for a Software Developer position at {Company_Name}"

msg_body = f"""
{Company_Name}

I am writing to express my interest in applying for a Software Developer position at {Company_Name}. I recently graduated from  Government Engineering College, Vaishali with a degree in B.Tech ECE (2022 Batch) with a CGPA of 8.3.


I am particularly interested in working for{Company_Name} because I need Job. I have experience developing software in a variety of languages, including [Programming Languages]. I am a hard worker and a quick learner, and I am confident that I can contribute to the success of your team.

Attached, please find my resume for your review. Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to the success of {Company_Name}.


Thanks & Regards
Jitesh Kumar
"""


resume = "D:/Automation Project/Email_BOT/Script/Jitesh_Kumar_Resumee_Aug.pdf"
path = "D:/ResultBOT/Email_BOT/msg_body.txt"
file_name = os.path.isfile(path)
file_name = os.path.isfile(resume)


# writing Resume file
with open(resume, "rb") as fp:
    # Create a text/plain message
    msg = EmailMessage()
    file_type = fp.read()
    file_name = "Jitesh_Resume.pdf"


msg = EmailMessage()
msg.set_content(msg_body)
# msg.add_alternative(msg_body1)
msg.add_attachment(file_type, maintype="pdf", subtype="file_type", filename=file_name)

msg["Subject"] = subject
msg["From"] = sent_from
msg["To"] = ",".join(sent_to)
msg["Cc"] = sent_to_cc
msg["Bcc"] = sent_to_bcc

try:
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.ehlo()
    smtp_server.login(sender, user_pass)
    smtp_server.send_message(msg)
    smtp_server.close()
except Exception as e:
    print("Error found", e)

print("Script executed successfuly")


# send msg from  atext file
# with open(path, 'r') as fp:
#     # Create a text/plain message
#     msg = EmailMessage()
#     msg.set_content(fp.read())
