def categorise(dataframe):
    complain = ['complain']
    luggage = ['luggage', 'suitcase', 'luggage']
    delay = ['delay', 'miss', 'on time', 'late']
    cancelling = ['cancel']
    promotion = ['offer', 'promotion']
    staff = ['staff', 'strike', 'steward', 'service']
    money = ['$', 'cost', '£', 'refund', '€']

    complain_tweets = dataframe[dataframe['text'].str.contains('|'.join(complain))]
    luggage_tweets = dataframe[dataframe['text'].str.contains('|'.join(luggage))]
    delay_tweets = dataframe[dataframe['text'].str.contains('|'.join(delay))]
    cancelling_tweets = dataframe[dataframe['text'].str.contains('|'.join(cancelling))]
    promotion_tweets = dataframe[dataframe['text'].str.contains('|'.join(promotion))]
    staff_tweets = dataframe[dataframe['text'].str.contains('|'.join(staff))]
    money_tweets = dataframe[dataframe['text'].str.contains('|'.join(money))]

    category_dict = {
        'complain': complain_tweets,
        'luggage': luggage_tweets,
        'delay': delay_tweets,
        'cancelling': cancelling_tweets,
        'promotion': promotion_tweets,
        'staff': staff_tweets,
        'money': money_tweets
    }
    return category_dict