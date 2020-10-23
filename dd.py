
# YouTube Video: https://www.youtube.com/watch?v=mP_Ln-Z9-XY
import smtplib

EMAIL_ADDRESS = 'yabous.xman@gmail.com'
PASSWORD = 'hrasveswuoqkgorj'

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS,PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"

from pytrends.request import TrendReq

# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['tshirt'],timeframe='now 7-d',geo='US')


# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
D=related_queries_dict['tshirt']['rising']


send_email(subject, D)
