import requests

keyword = input("Please state the keyword: ")

request = "https://api.tvmaze.com/search/shows?q=" + keyword

response = requests.get(request).json()

try:   
    print("")
    print(response[0]["show"]["name"])
    print("")

    for x in (response[0]["show"]["genres"]):
        print(x)

    print("")

    summary = response[0]["show"]["summary"]

    summary = summary.replace("<p>","")
    summary = summary.replace("</p>","")
    
    summary = summary.replace("<b>","")
    summary = summary.replace("</b>","")

    print(summary)
except:
    print("Could not find the show. Sorry!")