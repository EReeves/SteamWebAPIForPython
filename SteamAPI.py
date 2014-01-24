#Steam Web API wrapper by Evan Reeves

import json

#Returns a list of dictionaries containing all Steam apps - ['appid': int, 'name', string]
def getAppList():
    r = _sendRequest("ISteamApps/GetAppList/v2")
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    jr = jr["applist"]
    jr = jr["apps"]
    return jr

#Returns a dictionary of news articles.
def getNewsForApp(appid, count, maxlength):
    r = _sendRequest("ISteamNews/GetNewsForApp/v0002/", {"appid": appid, "count": count, "maxlength": maxlength})
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    jr = jr["appnews"]
    return jr

#Returns a list of dictionaries containing an acheivement name and percentage. [{"name": string, "percent": float},]
def getGlobalAchievementPercentagesForApp(appid):
    r = _sendRequest("ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/", {"gameid": appid})
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    jr = jr["achievementpercentages"]
    return jr

#Gets a Steam user summary from a steamid, requires an API key.
#Supports multiple users at once, separate steam id's with commas.
def getPlayerSummaries(apikey, steamids):
    r = _sendRequest("ISteamUser/GetPlayerSummaries/v0002/", {"key": apikey, "steamids": steamids})
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    jr = jr["response"]
    return jr    

#Gets players listed on a public player profile. Requires API key.
def getFriendsList(apikey, steamid, relationship = all):
    r = _sendRequest("ISteamUser/GetFriendList/v0001/", {"key": apikey, "steamid": steamid, "relationship": relationship})
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    jr = jr["friendslist"]
    return jr    

#Gets a list of player achievements from a steamid and appid. Requires API key.
def getPlayerAchievements(apikey, steamid, appid):
    r = _sendRequest("ISteamUserStats/GetPlayerAchievements/v0001/", {"key": apikey, "steamid": steamid, "appid": appid})
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    return jr  

#Gets owned games from a steamid, check the Valve documentation for the optional arguments.
def getOwnedGames(apikey, steamid, appids_filter = "", include_appinfo = True, include_played_free_games = True):
    r = _sendRequest("IPlayerService/GetOwnedGames/v0001/", {"key": apikey, "steamid": steamid, "include_appinfo": include_appinfo, "include_played_free_games": include_played_free_games})
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    return jr  

#get recently played games from a steamid, optional count parameter limits number retrieved.
def getRecentlyPlayedGames(apikey, steamid, count = None):
    arguments = None
    if count == None:
            arguments = {"key": apikey, "steamid": steamid}
    else:
        arguments = {"key": apikey, "steamid": steamid, "count": count}
    r = _sendRequest("IPlayerService/GetRecentlyPlayedGames/v0001/", arguments)
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    return jr    

#Check Valve docs.
def isPlayingSharedGame(apikey, steamid, appid_playing):
    r = _sendRequest("IPlayerService/IsPlayingSharedGame/v0001/", {"key": apikey, "steamid": steamid, "appid_playing": appid_playing})
    if r == "disappointment":
        return
    r = r.read().decode("ascii", errors='ignore')
    jr = json.loads(r)
    return jr  

import urllib.request
import urllib.parse

def _sendRequest(get, post = {}):
    req = urllib.request.Request("https://63.228.223.110/" + get)
    outData = None
    if len(post) != 0:
        outData = urllib.parse.urlencode(post)
        req = urllib.request.Request("https://63.228.223.110/" + get + "?" + outData)
    #It's picky about the User Agent.
    req.add_header("User-Agent", "Steam 1291812 / iPhone")
    try:
        r = urllib.request.urlopen(req)   
        return r
    except:
        print("Error connecting to valve server.")
        return "disappointment."


    




