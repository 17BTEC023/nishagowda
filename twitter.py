import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        :"UcmHC4APh1rG2hXpMmdfTpQRh",
    "consumer_secret"     :"deOzINnS9IYESLpgred5KgApVwdv9JlvNfiwLvGPWiDweNV9Fa",
    "access_token"        :"969429438306725888-S8bNkdroVwfNy0TJ8DzdCbekdznq0Zj",
    "access_token_secret" :"QzPXtu7SGgBhCAs3SIiZriYbMk275YfLL3lnkBQQkeuX9"

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
