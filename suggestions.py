import requests
import html
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

# GOOGLE SUGGESTIONS
def get_google_suggestions(text):
    url = "http://suggestqueries.google.com/complete/search"

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
def get_ddgo_suggestions(text):
    url = "https://duckduckgo.com/ac/?q="+text+"&kl=wt-wt"

    r = requests.get(url)

    if(r.status_code == 200):
        ddg_list = []
        for x in r.json():
            ddg_list.append(x["phrase"])
        
        return ddg_list
    else:
        return []        



# BING SUGGESTIONS
# def get_bing_suggestions(text):
#     url = "https://www.bing.com/AS/Suggestions?mkt=en-gb&qry="+text+"&cvid=D5B30824B0E840299C765CB9CA9E6511"

#     r = requests.get(url)

#     if(r.status_code == 200):
#         text_soup = BeautifulSoup(urlopen(url).read()) #read in

#         titles = text_soup.findAll('span', {'class': 'sa_tm_text'})
#         for title in titles:
#             print(td.text)

#         return []
#     else:
#         return []  




# print(get_google_suggestions("glasgow"))
# print(get_ddgo_suggestions("glasgow"))

# print(get_bing_suggestions("glasgow"))