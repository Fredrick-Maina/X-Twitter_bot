import tweepy
from tkinter import *

consumer_key = 'your consumer key'
consumer_secret = 'your consumer secret'
access_token = 'your access token'
access_token_secret = 'your access token secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.get_user()
print(user.name)
"""
try:
    user = api.verify_credentials()
    print(f"Authenticated as {user.name}")
except tweepy.TweepyException as e:
    print(f"Error: {e}")
try:
    user_info = api.get_user()
    print(f"User ID: {user_info.id}, user Name: {user_info.name}")
except tweepy.TweepyException as e:
    print(f"Error: {e}")
"""
for follower in tweepy.Cursor(api.get_followers).items():
    follower.follow()
    print("Followed everyone that is following " + user.name)

root = Tk()
label1 = Label(root, text="Search")
E1 = Entry(root, bd=5)
label2 = Label(root, text="Number of Tweets")
E2 = Entry(root, bd=5)
label3 = Label(root, text="Response")
E3 = Entry(root, bd=5)
label4 = Label(root, text="Reply?")
E4 = Entry(root, bd=5)
label5 = Label(root, text="Retweet?")
E5 = Entry(root, bd=5)
label6 = Label(root, text="Favorite?")
E6 = Entry(root, bd=5)
label7 = Label(root, text="Follow?")
E7 = Entry(root, bd=5)


def gete1():
    return E1.get()


def gete2():
    return E2.get()


def gete3():
    return E3.get()


def gete4():
    return E4.get()


def gete5():
    return E5.get()


def gete6():
    return E6.get()


def gete7():
    return E7.get()


def main():
    search = gete1()

    numberOfTweets = int(gete2())

    phrase = gete3()

    reply = gete4()

    retweet = gete5()

    favorite = gete6()

    follow = gete7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search_tweets, search).items(numberOfTweets):
            try:
                tweet.favorite()
                print("\nTweet by: @" + tweet.user.screen_name)
                print("ID: @" + str(tweet.user.id))
                tweetId = tweet.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
                print("Replied with" + phrase)

            except tweepy.TweepyException as e:
                print(f"Error: {e}")

            except StopIteration:
                break

    if retweet == "yes":
        for tweet in tweepy.Cursor(api.search_tweets, search).items(numberOfTweets):
            try:
                tweet.favorite()
                print("Favorite the tweet")

            except tweepy.TweepyException as e:
                print(f"Error: {e}")

            except StopIteration:
                break

    if follow == "yes":
        for tweet in tweepy.Cursor(api.search_tweets, search).items(numberOfTweets):
            try:
                tweet.user.follow()
                print("Followed the user")

            except tweepy.tweepyerrors as e:
                print(e.reason)

            except StopIteration:
                break


submit = Button(root, text="Submit", command=main)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side=BOTTOM)

root.mainloop()
