import requests
import zipfile
import shutil
from pathlib import Path

steam_id = '76561198362219694'
profile_id = '506898'


def download_rec(match, profile_id):
    matches_url = f'https://aoe.ms/replay/?gameId={match}&profileId={profile_id}'
    response2 = requests.get(matches_url)

    with open("response.zip", "wb") as f:
        f.write(response2.content)

    try:
        with zipfile.ZipFile('./response.zip', 'r') as zip_ref:
            zip_ref.extractall('./recs')
    except:
        print('non-zip')

# def extract_civ(match):
    #     for index in range(len(match[index]['players']))


def main():

    url = f'https://aoe2.net/api/player/matches?game=aoe2de&steam_id={steam_id}&count=10'
    response = requests.get(url)
    matches = response.json()
    print(matches)

    dirpath = Path('./recs')

    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree('./recs')

    for index in range(len(matches)):
        players = matches[index]['players']
        if len(players) <= 2:
            if matches[index]['map_type'] == 9:
                print('1v1 arabia found')
                for player in range(len(players)):
                    # if players[player]['steam_id']==f'{steam_id}' and players[player]['civ'] == 9 or players[player]['civ'] == 13:
                    if players[player]['steam_id'] == f'{steam_id}':
                        # print(players[player]['civ'])
                        print('downloading rec')
                        download_rec(matches[index]['match_id'], profile_id)
                    # else:
                    #     print('HOANG on non-standard civ')
            else:
                print('non-arabia map')
        else:
            print('teamgame')


if __name__ == "__main__":
    main()
