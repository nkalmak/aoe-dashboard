import requests
import zipfile
import shutil
from pathlib import Path

def download_rec(match):
    matches_url = f'https://aoe.ms/replay/?gameId={match}&profileId={profile_id}'
    response2 = requests.get(matches_url)

    with open("response.zip", "wb") as f:
        f.write(response2.content)

    try:
        with zipfile.ZipFile('./response.zip', 'r') as zip_ref:  
            zip_ref.extractall('./recs')
    except:
        print('non-zip')

if __name__ == "__main__":

    steam_id = '76561198449406083'
    profile_id = '199325'
        
    url = f'https://aoe2.net/api/player/matches?game=aoe2de&steam_id={steam_id}&count=14'
    response = requests.get(url)
    matches = response.json()

    dirpath = Path('./recs')

    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree('./recs')

    for index in range(len(matches)):
        players = matches[index]['players']
        if len(players) <= 2:
            if matches[index]['map_type']==9:
                for player in range(len(players)):
                    # if players[player]['steam_id']==f'{steam_id}' and players[player]['civ'] == 9 or players[player]['civ'] == 13:
                    if players[player]['steam_id']==f'{steam_id}':
                        print('downloading rec')
                        download_rec(matches[index]['match_id'])
                    else:
                        print('HOANG on non-standard civ')
            else:
                print('non-arabia map')
        else:
            print('teamgame')

    # def extract_civ(match):
    #     for index in range(len(match[index]['players']))