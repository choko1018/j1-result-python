import requests
from bs4 import BeautifulSoup
from image import match
match_url = "https://data.j-league.or.jp/SFMS01/search?competition_years=2024&competition_frame_ids=1&competition_ids=589&team_ids=11&home_away_select=0&tv_relay_station_name="

#HTMLを取得して変数に格納する
match_html = requests.get(match_url).text

match_soup = BeautifulSoup(match_html, 'html.parser')
all_result = match_soup.find_all("tr")
matches=[]
for result in all_result:
    contents=result.find_all("td")
    if len(contents) != 11: continue
    result=match(
        date=contents[3].get_text(strip=True),
        category=contents[2].get_text(strip=True),
        victory="",
        hometeam=contents[5].get_text(strip=True),
        awayteam=contents[7].get_text(strip=True),
        scoreDetail=contents[6].get_text(strip=True),
        venue=contents[8].get_text(strip=True)
    )
    matches.append(result)
print(matches)
for result in matches:
    result.make_image()