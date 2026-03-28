import requests
print("START")
API_KEY = "YOUR API KEY"


class SteamAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_steam_id(self, username: str):
        url = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/"
        params = {
            "key": self.api_key,
            "vanityurl": username
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        if data["response"].get("success") != 1:
            return None

        return data["response"].get("steamid")

    def get_profile(self, steam_id: str):
        url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/"
        params = {
            "key": self.api_key,
            "steamids": steam_id
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        players = data.get("response", {}).get("players", [])
        if not players:
            return None

        player = players[0]

        return {
            "name": player.get("personaname"),
            "profile_url": player.get("profileurl"),
            "avatar": player.get("avatarfull")
        }

    def get_games(self, steam_id: str):
        url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
        params = {
            "key": self.api_key,
            "steamid": steam_id,
            "include_appinfo": True
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        if "response" not in data or "games" not in data["response"]:
            return {"error": "Games are private or unavailable"}

        games = data["response"]["games"]
        result = []

        for game in games:
            result.append({
                "name": game.get("name"),
                "playtime_hours": round(game.get("playtime_forever", 0) / 60, 1)
            })

        return result


if __name__ == "__main__":
    steam = SteamAPI(API_KEY)

    username = "Withyom"

    steam_id = steam.get_steam_id(username)
    if not steam_id:
        print("User not found")
        raise SystemExit

    print("STEAM ID:", steam_id)

    profile = steam.get_profile(steam_id)
    print("\nPROFILE:", profile)

    games = steam.get_games(steam_id)
    print("\nGAMES:", games[:5] if isinstance(games, list) else games)
