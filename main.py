import pandas as pd
from bs4 import BeautifulSoup
import requests
import time



file = [
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_4&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_27&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_19&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_24&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_21&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_30&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_8&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_26&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_13&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_gamma_2&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_15&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_20&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_3&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_6&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_7&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_12&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_2&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_22&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_25&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_31&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_32&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_10&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_29&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_9&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_23&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_28&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_16&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_18&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_5&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_11&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_1&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730"
]
file2 = [
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_28&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_16&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_18&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_5&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_11&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730",
"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=tag_set_community_1&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730"

]
data= pd.DataFrame({"Name":[],"Qty":[],"Price_$":[]})

try:
    for i in file:
        page = requests.get(i)
        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find("div", class_="market_listing_row market_recent_listing_row market_listing_searchresult")
        resultName = result.find("span",class_="market_listing_item_name").string
        resultQty = result.find("span",class_="market_listing_num_listings_qty").string
        resultPrice = result.find("span",class_="normal_price").contents[3].string
        resultQty = resultQty.replace(",","")
        data.loc[len(data.index)] = [resultName, int(resultQty), resultPrice]

        #time.sleep(1)
        print("Name: "+ resultName+" Quantity: "+ resultQty +" Price_$: "+ resultPrice)

except:
    data.to_excel("data/data.xlsx",engine='xlsxwriter')
finally:
    data.to_excel("data/data.xlsx", engine='xlsxwriter')
