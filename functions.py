#function to find all tweets of a certain twitter id (Like the one of KLM)
def user_id_to_list(datafr, user_id):
    id_list = []
    for i in range(0, len(datafr)):
        if datafr['user'][i]['id'] == user_id:
            id_list.append(datafr.loc[i])
    #return pandas.DataFrame(id_list)
    return id_list

#Function to find a tweet by its id (string id)
def tweet_id_finder(datafr, tweet_id):
    for i in range(0, len(datafr)):
        if datafr['id_str'][i] == tweet_id:
            return datafr.loc[i]
    return False

#function to find all tweets that replied on a tweet
def answer_tweets(datafr, tweet_id):
    answer_list = []
    for i in range(0, len(datafr)):
        if datafr['in_reply_to_status_id_str'][i] == tweet_id:
            answer_list.append(datafr.loc[i])
    return answer_list

#function to find all tweets that took part of a conversation of a certain tweet
def conversations(datafr, tweet, tweet_list = []):
    if tweet[13] == "NaN":
        tweet_list.append(tweet)
        return(tweet_list)
    else:
        replied_tweet = tweet_id_finder(datafr, tweet[13])
        print(tweet)
        if type(replied_tweet) == bool:
            return tweet_list.append(tweet)
        return conversations(datafr, replied_tweet, tweet_list)
    answer_list = answer_tweets(datafr, tweet[14])
    for tweets in answer_list:
        return conversations(datafr, tweets, tweet_list)