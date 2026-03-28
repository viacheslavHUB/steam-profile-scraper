# Steam Profile Scraper

Python scraper for Steam profile data using the official Steam API.

## Features

- Resolve custom Steam profile URL to SteamID
- Get profile data:
  - profile name
  - profile URL
  - avatar
- Get owned games
- Get playtime in hours

## Tech Stack

- Python
- Requests
- Steam Web API

## Example Output

```bash
STEAM ID: 76561199230050669

PROFILE: {
  'name': 'Withyom',
  'profile_url': 'https://steamcommunity.com/id/Withyom/',
  'avatar': 'https://avatars.steamstatic.com/...jpg'
}

GAMES: [
  {'name': 'Half-Life 2', 'playtime_hours': 0.2},
  {'name': 'Portal', 'playtime_hours': 2.1},
  {'name': 'Left 4 Dead 2', 'playtime_hours': 5.0}
]
