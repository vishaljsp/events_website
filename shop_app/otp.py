from twilio.rest import Client
# import random
#     OTP=random.randint(0,1000000)

def smssender(num,otp):
    account_sid ='AC36b2de897309518e9c95738493630436'
    auth_token ='1b2bc2ca9a5fd1cfadd216d1634d41d7'
    client = Client(account_sid, auth_token)
    client.messages.create(
            body=otp,
            from_='+15592967279',
            to=num
        )
        
    

    print("mesej done all")