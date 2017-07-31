import sqlite3, time

# Ejecutar consulta de la base de datos
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

# Enviar un email
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

# Enviar email a todas las personas que correspondan
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
        subject = "Feliz Cumpleaños {} {}".format(item[0], item[1])
        body_text = "{},\nEl Grupo de Investigación de Multimedia y Visión por Computador (MVC) te desea éxitos en este día tan especial".format(item[0])
        body_html = "<h2>{}</h2><p>El <i>Grupo de Investigación de Multimedia y Visión por Computador (MVC)</i> te desea éxitos en este día tan especial</p><p><img src={} width='100%%' /></p>".format(item[0],pic_url)
        sendMail(user,pwd, item[2], subject, body_text, body_html)
        pass
    pass

# Ejecutar ordenadamente las acciones
def run(user, pwd):
    people = execQuery()
    if people:
        sendAll(user, pwd, people)
        pass
    pass

# Captura de parametros y ejecución inicial
if __name__ == '__main__':
    import sys
    args = sys.argv
    if (len(args) == 3):
        run(args[1], args[2])
    else:
        print ("Por favor revisar los parámetros")
