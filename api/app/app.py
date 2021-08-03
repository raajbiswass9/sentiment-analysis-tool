
# import requests
# import html
# from urllib import urlopen
# from BeautifulSoup import BeautifulSoup

from flask import Flask
app = Flask(__name__)



@app.route("/")
def home():
    return "Welcome"





@app.route("/filter_google")
def filter_google_suggestions():
    url = "http://suggestqueries.google.com/complete/search"

    text = "Glasgow"
    params = {
        "client": "firefox",
        "q": text,
        "hl": "en"
    }

    r = requests.get(url, params = params)

    if(r.status_code == 200):
        return (r.json()[1])
    else:
        return []



# DUCK DUCK GO SUGGESTIONS
@app.route("/filter_ddgo")
def filter_ddgo_suggestions():
    text = "Glasgow"
    url = "https://duckduckgo.com/ac/?q="+text+"&kl=wt-wt"

    r = requests.get(url)

    if(r.status_code == 200):
        ddg_list = []
        for x in r.json():
            ddg_list.append(x["phrase"])
        
        return ddg_list
    else:
        return [] 