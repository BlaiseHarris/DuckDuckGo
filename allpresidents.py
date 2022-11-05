import requests

def get_all_presidents():
    query = "presidents of the united states"
    resp = requests.get("https://api.duckduckgo.com",
                     params={
                         "q": query,
                         "format": "json"
                     })

    data = resp.json()
    amount = len(data["RelatedTopics"])
    i = 0
    finalData = ""

    while i != amount:
        if i != 0:
            finalData = finalData + ", " + data["RelatedTopics"][i]["Text"]
        else:
            finalData = data["RelatedTopics"][i]["Text"]
        i = i + 1

    return finalData