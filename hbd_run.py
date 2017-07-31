import sqlite3, time

# Execute database query
def execQuery():
    try:
        conn = sqlite3.connect('dates.db')
        cursor = conn.cursor()
        now = time.strftime("%m/%d")
        t = (now,)
        cursor.execute("SELECT * FROM DATA WHERE strftime('%m/%d', birthday)=?", t)
        people = cursor.fetchall()
        conn.close()
        return people

    except:
        print ('DB error')

# Send a mail
def sendMail(user, pwd, recipient, subject, body_text, body_html):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gmail_user = user
    gmail_pwd = pwd

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = recipient
    
    part1 = MIMEText(body_text, 'plain')
    part2 = MIMEText(body_html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    # Prepare actual message

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(user, recipient, msg.as_string())
        server.close()
        # print ('successfully sent the mail')
    except (Exception,e): 
        print (str(e))
        # print ("failed to send mail")
        pass
    pass

# Send email to everybody
def sendAll(user, pwd, people=[]):
    import random
    # Building message for everbody
    for item in people:
        # Choose pic
        conn = sqlite3.connect('dates.db')
        cursor = conn.cursor()
        t = (item[4],)
        cursor.execute("SELECT url FROM IMGS WHERE gender=?", t)
        pics = cursor.fetchall()
        pic_url = random.choice(pics)[0]
        
        # Building body
        subject = "Happy Birthday {} {}".format(item[0], item[1])
        body_text = "{},\nMVC Research Group wishing you all the great things today".format(item[0])
        body_html = "<h2>{}</h2><p><i>MVC Research Group</i> wishing you all the great things today</p><p><img src={} width='100%%' /></p>".format(item[0],pic_url)
        sendMail(user,pwd, item[2], subject, body_text, body_html)
        pass
    pass

# Execute commands in order
def run(user, pwd):
    people = execQuery()
    if people:
        sendAll(user, pwd, people)
        pass
    pass

# Get parameters and start execution
if __name__ == '__main__':
    import sys
    args = sys.argv
    if (len(args) == 3):
        run(args[1], args[2])
    else:
        print ("Please check your parameters")
