import OS
import time
import tweepy
consumer_key='UcmHC4APh1rG2hXpMmdfTpQRh'
consumer_secret='deOzINnS9IYESLpgred5KgApVwdv9JlvNfiwLvGPWiDweNV9Fa'
access_token='969429438306725888-S8bNkdroVwfNy0TJ8DzdCbekdznq0Zj'
access_token_secret='QzPXtu7SGgBhCAs3SIiZriYbMk275YfLL3lnkBQQkeuX9'


auth=tweepy.0AuthHandler(consumer_key,consumer_secret)
auth.set_access_token_(access_token,access_token_secret)
api=tweepy.API(auth)
a=0
b=1
while(a<2):
    img="/home/user/rip/img"+str(b)+".jpg"
    cmd="ffswebcam-F 3 --fps 20 - 1200*800 "+img
    OS.system(cmd)
    print("selfiy taken")
    file = open(img,'rb')
    data = file.read()
    api.update_with_media(img,status="pic of the day")
    print("wait for 5 seconds selfiy!!")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
