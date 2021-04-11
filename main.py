import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import io
import sys

# pc버전 api
# url = f"https://new.land.naver.com/api/articles/clusters?cortarNo=1141011700&zoom=15&markerId&markerType&selectedComplexNo&selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3AOPST%3AABYG%3AOBYG%3AGM%3AOR%3AVL%3ADDDGG%3AJWJT%3ASGJT%3AHOJT&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3ASMALLSPCRENT%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&leftLon=126.8992045&rightLon=126.9317987&topLat=37.5879848&bottomLat=37.576930950000005"

# 명지대학교 인문캠퍼스 위치가 중심인 지도.
center_lat = 37.5785302
center_lon = 126.9234694
btm_lat = 37.5625943
left_lon = 126.8822707
top_lat = 37.5944627
right_lon = 126.9646681

url = f"https://m.land.naver.com/cluster/clusterList?view=atcl&rletTpCd=OR&tradTpCd=A1%3AB1%3AB2%3AB3&z=15&lat={center_lat}&lon={center_lon}&btm={btm_lat}&lft={left_lon}&top={top_lat}&rgt={right_lon}&pCortarNo="


sys.stdout.reconfigure(encoding='utf-8')
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(
    executable_path=".\\chromedriver.exe", options=chrome_options)

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html)
site_json = json.loads(soup.find("body").text)

print(site_json)

# bs4 만 쓸 경우 - Selenium 미 사용 시(단, Response 307 뜸)
# html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(html, "html.parser")
# site_json = json.loads(soup.text)
# result = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# soup = BeautifulSoup(result.text, "html.parser")
# for i in site_json:
#     print(i)
