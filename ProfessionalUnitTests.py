#Quick & lazy test.
import SteamAPI

def testForDisappointment(name, result):
    if result == "disappointment":
        print("Error in " + name + " debug it fool.")
    else:
        print(name + " test passed.")

#These need to be changed from XXXXXXXX.. to legit key/id before it will run.
apikey = "XXXXXXXXXXXXXXXXX"
steamid = "XXXXXXXXXXXXXXXXX"
appid = 440

testForDisappointment(SteamAPI.getAppList.__name__, SteamAPI.getAppList())
testForDisappointment(SteamAPI.getNewsForApp.__name__, SteamAPI.getNewsForApp(440, 6, 400))
testForDisappointment(SteamAPI.getGlobalAchievementPercentagesForApp.__name__, SteamAPI.getGlobalAchievementPercentagesForApp(appid))
testForDisappointment(SteamAPI.getPlayerSummaries.__name__, SteamAPI.getPlayerSummaries(apikey, steamid))
testForDisappointment(SteamAPI.getFriendsList.__name__, SteamAPI.getFriendsList(apikey, steamid, "all"))
testForDisappointment(SteamAPI.getPlayerAchievements.__name__, SteamAPI.getPlayerAchievements(apikey, steamid, appid))
testForDisappointment(SteamAPI.getOwnedGames.__name__, SteamAPI.getOwnedGames(apikey, steamid))
testForDisappointment(SteamAPI.getRecentlyPlayedGames.__name__, SteamAPI.getRecentlyPlayedGames(apikey, steamid))
testForDisappointment(SteamAPI.isPlayingSharedGame.__name__, SteamAPI.isPlayingSharedGame(apikey, steamid, appid))