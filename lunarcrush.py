import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




APIKEY = 'p1fsoddrkwf7fg4bifve'

coinnames = "ADA"


def search(cname):
    url = f"https://api.lunarcrush.com/v2?data=assets&key={APIKEY}&symbol={cname}&data_points=24&change=1w&interval=day"

    headers = None
    payload= None
    response = requests.request("GET", url, headers=headers, data=payload)

    jsoned = json.loads(response.text)

    endpoint_with_data = jsoned['data'][0]["timeSeries"]
    df = pd.DataFrame()
    time = []
    tweets = []

    for ix in range(0,len(endpoint_with_data)):
        time.append(datetime.utcfromtimestamp(endpoint_with_data[ix]["time"]).strftime('%Y-%m-%d'))
        tweets.append(endpoint_with_data[ix]["tweets"])

    df["Time"] = time
    df[f"Tweets"] = tweets

    # if len(df) > 2:
    #     df = df.merge(df,how="outer")

    

    plt.figure(figsize = (12,8))

    ax = sns.lineplot(x="Time",y = "Tweets",
                data=df)
    plt.xticks(rotation=45)
    plt.show()

    
search(coinnames)

# for coinname in coinnames:
#     df = search(coinname)
  

# plt.figure(figsize = (12,8))

# ax = sns.lineplot(x="Time",y = "Tweets"
#             data=df)
# plt.xticks(rotation=45)
# plt.show()
