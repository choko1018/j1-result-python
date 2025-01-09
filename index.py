import requests
from bs4 import BeautifulSoup
from image import make_image,match
match_url = "https://data.j-league.or.jp/SFMS01/search?competition_years=2024&competition_frame_ids=1&competition_ids=589&team_ids=11&home_away_select=0&tv_relay_station_name="

#HTMLを取得して変数に格納する
match_html = requests.get(match_url).text

match_soup = BeautifulSoup(match_html, 'html.parser')
dates = match_soup.find_all("td", class_="sc-tableGame__data--date")

categories = match_soup.find_all("td",class_="sc-tableGame__data--category")

victories = match_soup.find_all("td",class_="sc-tableGame__data--victory")

teams = match_soup.find_all("td",class_="sc-tableGame__data--team")

scoreDetails = match_soup.find_all("p",class_="sc-tableGame__scoreDetail")
newDetails=[]
for scoreDetail in scoreDetails:
    if (scoreDetail.get_text(strip=True).find("合計") == -1):
        newDetails.append(scoreDetail)

venues = match_soup.find_all("td",class_="sc-tableGame__data--venue")

matches=[]

for i in range(1,len(dates)+1):
    date=dates[i-1].get_text(strip=True)
    category=categories[i-1].get_text(strip=True)
    victory=victories[i-1].get_text(strip=True)
    hometeam=teams[(i-1)*2].get_text(strip=True)
    awayteam=teams[(i-1)*2+1].get_text(strip=True)
    scoreDetail=newDetails[i-1].get_text(strip=True)
    venue=venues[i-1].get_text(strip=True)

    result=match(
        date,category,victory,hometeam,awayteam,scoreDetail,venue
    )
    matches.append(result)
    
for result in matches:
    make_image(result)