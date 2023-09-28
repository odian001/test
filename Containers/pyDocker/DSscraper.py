#!/bin/python3

from bs4 import BeautifulSoup
import requests, re, sys, time, random, os, mysql.connector


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Cookie": """AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1694825441238; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1694825443000@firstcreate:1694825441238"; auth=MTAyOTYyMDE4HYCNxSBYqkAal5zOAPDMfenCszVFbM6o7Zp8M6sIN19cmU%2BqrsYuWG%2F8zJ24e5RnqvYENHxh0ukE96nqnGhfTaypjK26C2LOMD1euyhSkbp4rC%2FsszkbJ2Qyi13uShDD767wuZloTfhm7Wk2KcjyglM949MaUzwsNnQKx2EXSLmGMsG8n5fWbvOncU2okNIHFLDhptptmoHAvOutvOmOFe4wZbO5EZGRvpNwK5eNuSEUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHQ6egaTbnn%2B5aLzLId3jFWTuqrUJsALxry8w%2Fd8L7liRP04%2FN%2B9Xwnsdc%2B3Bseu%2FQ%2FO2%2BcFQw2GhuUWzEymR3uM%2BsLX7zodOUaA9aXXf%2FxAQhzyR1DL0aJzDQ9jCZEaevUjyrOXbKKhH072NS%2FW0j%2FU%3D; ACID=398c0464-2060-4ee5-93c9-c36eee6d091b; hasACID=true; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiI0Mzc4IiwiZGlzcGxheU5hbWUiOiJPbmxleSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiIyMzQxOCIsImFkZHJlc3NMaW5lMSI6IjI2MDM2IExhbmtmb3JkIEh3eSIsImNpdHkiOiJPbmxleSIsInN0YXRlIjoiVkEiLCJjb3VudHJ5IjoiVVMiLCJwb3N0YWxDb2RlOSI6IjIzNDE4LTMwMDUifSwiZ2VvUG9pbnQiOnsibGF0aXR1ZGUiOjM3LjY4NTU1MSwibG9uZ2l0dWRlIjotNzUuNzI0MDAzfSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiaHViTm9kZUlkIjoiNDM3OCIsInN0b3JlSHJzIjoiMDY6MDAtMjM6MDAiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfQkFLRVJZIiwiUElDS1VQX1NQRUNJQUxfRVZFTlQiLCJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfSU5TVE9SRSJdLCJzZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQifV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6MzcuNzc2MiwibG9uZ2l0dWRlIjotNzUuNjMzNiwicG9zdGFsQ29kZSI6IjIzNDIxIiwiY2l0eSI6IlBhcmtzbGV5Iiwic3RhdGUiOiJWQSIsImNvdW50cnlDb2RlIjoiVVNBIiwibG9jYXRpb25BY2N1cmFjeSI6ImxvdyIsImdpZnRBZGRyZXNzIjpmYWxzZSwidGltZVpvbmUiOiJBbWVyaWNhL05ld19Zb3JrIn0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiNDM3OCIsImRpc3BsYXlOYW1lIjoiT25sZXkgU3VwZXJjZW50ZXIiLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsInJlZnJlc2hBdCI6MTY5NDgyOTA0MTI5MiwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjM5OGMwNDY0LTIwNjAtNGVlNS05M2M5LWMzNmVlZTZkMDkxYiJ9; assortmentStoreId=4378; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjQzNzgiLCJ0aW1lc3RhbXAiOjE2OTQ4MjU0NDEyOTEsInNlbGVjdGlvblR5cGUiOiJMU19TRUxFQ1RFRCJ9LCJwb3N0YWxDb2RlIjp7InRpbWVzdGFtcCI6MTY5NDgyNTQ0MTI5MSwiYmFzZSI6IjIzNDIxIn0sIm1wIjpbXSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOjM5OGMwNDY0LTIwNjAtNGVlNS05M2M5LWMzNmVlZTZkMDkxYiJ9; userAppVersion=us-web-1.99.1-a8184c7-0914T0217; sod=torbit1694825441; abqme=true; vtc=Vk-zyXGKJU_7YS-PTXOmy0; bstc=Vk-zyXGKJU_7YS-PTXOmy0; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=5x_R7|7qUrE|BOL9E|BT_PI|BUIT2|BukPC|CRAHa|Cvn2u|IhmrE|KvYZX|L_UiE|PLRdE|QpMSg|SK3g0|UbLrn|XCdGw|Y4MKj|aL6h-|b-nxw|fxdZH|iwrL4|ixZdu|jVDwQ|jyp9o|kD964|koDA2|lEUOy|lKy7O|lw4nN|msfO8|pyVOq|ragfe|tkCQg|xGG9_|zZps3; xpm=0%2B1694825443%2BVk-zyXGKJU_7YS-PTXOmy0~%2B0; exp-ck=5x_R717qUrE1BOL9E1BT_PI1BUIT21BukPC1CRAHa1Cvn2u1KvYZX1L_UiE1QpMSg1SK3g01UbLrn1Y4MKj3aL6h-1b-nxw1ixZdu1jVDwQ1kD9643koDA21lEUOy1lKy7O1lw4nN1msfO84ragfe1tkCQg1xGG9_1zZps31; _pxhd=facd34cc13d6f2ea817863a7953ebcc2912defa4f0e36e4f041f8eb28d351e93:0f4c322d-542b-11ee-9f7c-85a3908c8299; xptwg=1640588826:1C54156C9835EF0:47C9FA0:29E030A9:5966C8B9:227E6DBE:; xptwj=qq:221b08a61ed13ca95bd3:nlE8A9Lw0/YX4DzsRgnRaNwssDJ1buymXNm54KFzTzoKkm0YbwxtNZo1EI6FPgVt7k9to2qMR9QffWXrSv7dq114N54PxUEKNlQqjT0d3C1rqwkD4I45CrNAnUVf8L/R5QnCi748oWz3t+PgHxe+WSnrWsQsGQ0BQ4HDT41r; TS012768cf=010715e2f7339fd8773f3215587c1f5d7a5b09ddbc27f05807f769f907463ee2304e171411c6f2254514e30718b97159d7dfe8be03; TS01a90220=010715e2f7339fd8773f3215587c1f5d7a5b09ddbc27f05807f769f907463ee2304e171411c6f2254514e30718b97159d7dfe8be03; TS2a5e0c5c027=08981fe414ab2000fa05d9f28120f1b917081c3e2a47d47db61f59b30e07618d6c3a1da213d17d0a08bc294bfe113000738c322be6fcf3e69e29bc0a4a58371aef704d09fedc0cb3d143d253b06c39b2f1f3c858b19da124632dd967d1eaab53; akavpau_p2=1694826043~id=6f1fa87935c94a37e75bdd4247b15ec3; ak_bmsc=856AF8323C7DB11D4748A571CDAD0AC8~000000000000000000000000000000~YAAQ1PAiF/hB6JqKAQAAdOl3mxXCQ9aRtO3/OKcwItcaNEhAfOw7t9R95tSF+iZkXDvQR1/i4PoxUj6CsuriArAmdnaQ99TjmvM8wo17JXllrR/La5FXs65J97OE4Yip3LKM+czgJcLN+MRRwhmquXkKUi3FWCbbq3TK9XGkzQd4/hevhfsuhv+C7Je8or2Jjsawwg2y0ioCKpNQGJ0tCXC1ET3Hole+AZ00fPajov7sg/UsDZ4hTRXbKr0ClEVFy9cj9MVvXxFVU+kB2M3BUKJor0IT8ESs8nbEe7oMhJge+p95f3PAmgwCqUVY92exJ109MATpmctscIdoCV+tx7vJuRhPtaprObBagTDEp7uSrgKtkOpq/aD0cytqTiMJJNA33IvMx5QJQjY=; TBV=7; _astc=4add7849a627169b7490d15e27f897d2; adblocked=true; xptc=assortmentStoreId%2B4378; bm_sv=1F07034EC200681603983BE521DC3B84~YAAQ1PAiF1BC6JqKAQAAEfF3mxVVevxsbOy86GAG97sYnNHioh9O4e6GulXMWgLsL2l0hTIN5dTB9OrWXwo9HJtQTKEktVFk9N/k2z6o+kjzfqq3mKbW+8mYhbQzVEwE3h2FgvbBOJFuZe0Np7eRurk0qXiAbPv6GbF3rEI40SBxxuSpGgPtqb1X30fIBDb6L16R/roodyfypDthC6LXyMLqf9vZ7AWaB4ZA/tV2puTlpg2aSI8t1OkB+GrxRwRBLA==~1; _m=9; pxcts=10268ac6-542b-11ee-86f9-e9323d6b2655; _pxvid=0f4c322d-542b-11ee-9f7c-85a3908c8299; _pxde=eb708548ea9d22982661d9e86820a5e286796dc5c2ac958d62593a3f26c31f86:eyJ0aW1lc3RhbXAiOjE2OTQ4MjU0OTc4MDJ9; _px3=93bc63042b6151f0d8b8345b67ac759aa953ba7cabaf9ca8d624e0f1ac20163e:YUr5uDpJDgjIT+t9n9w/5an0jTIA5AwjQZ3d8nHpJat63Zdh55aNFFHGQgmmtgfPw4zrHvxk0lTfxmr+60dCPA==:1000:M3RSjDjN1R+br+IKf3N7YM++/Klsk1uZGRqOAz1dLxI3bojqBjkxIvYFgmg60Y/vuvFUcg2Kr3BxjOSlMmWUigVfQIrwEkQiYiTGFdOmfTkE7C81s0vD2Z7E4v0K89QMHEanip5H/mrDfoRzFy8Ez3k87auQ/okWWkbQ09xbIRlmE5mPlKjZzh+/mTUf3stz5UMBdrpHbLLpeRLh2Cc2QQ=="""
}

def my_tag_selector(tag):
        return tag.name == "span" and tag.has_attr("itemprop") and tag.get("itemprop") == "price"

def bot_check(tag):
        return tag.name == "div" and tag.has_attr("id") and tag.get("id") == "px-captcha"

db_config = {
     "host": "doughsaverdb",  # Use the name of the MariaDB container
     "user": "root",
     "password": "1qaz!QAZ",
     "database": "DoughSaverDB",
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()
query = "Select IngredientID, UpdateTimestamp, CurrentPrice, Link, StoreID from PriceData where IsPaused is not TRUE order by UpdateTimestamp asc fetch first 12 rows only"
cursor.execute(query)
for row in cursor.fetchall():
    x = random.uniform(3.6,20.1)
    time.sleep(x)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    mysqlTime = str(time.strftime("%Y-%m-%d %H:%M:%S"))
    response = requests.get(row[3], headers=headers)
    if response.status_code != 200:
        with open("/output_data/errors.txt", "a") as file:
            file.write(timestr+' Error fetching page '+row[3]+'\n')
        continue
    with open("/output_data/responsefiles/"+str(row[0])+"-"+timestr+".txt", "w") as file:
            file.write(str(response.content))
    soup = BeautifulSoup(response.content, 'html.parser')
    botcheck =str(soup.find_all(bot_check))
    if botcheck != "[]":
        with open("/output_data/botchecks.txt", "a") as file:
            file.write(timestr+' Ive been detected. Bot check at page '+row[3]+'\n')
        continue
    output = str(soup.find_all(my_tag_selector))
    price = re.sub('.*>.*\$', '', output)
    price = re.sub('<.*', '', price)
    UpdateTimestamp = str(row[1].strftime("%Y-%m-%d %H:%M:%S"))
    StoreID=str(row[4])
    IngredientID=str(row[0])
    HistoricalPrice=str(row[2])	
    if HistoricalPrice == price:
        query = "UPDATE PriceData SET UpdateTimestamp = %s WHERE IngredientID = %s AND StoreID = %s"
        values = (mysqlTime, IngredientID, StoreID)
        cursor.execute(query, values)
    elif price == "[]":
         print("[]")
         time.sleep(.01)
    else:
        # Update UpdateTimestamp in PriceData
        query = "UPDATE PriceData SET UpdateTimestamp = %s WHERE IngredientID = %s AND StoreID = %s"
        values = (mysqlTime, IngredientID, StoreID)
        cursor.execute(query, values)
        # Update CurrentPrice in PriceData
        query = f"UPDATE PriceData SET CurrentPrice = %s WHERE IngredientID = %s AND StoreID = %s"
        values = (price, IngredientID, StoreID)        
        cursor.execute(query, values)
        # Insert into PriceHistory 
        query = "insert into PriceHistory (StoreID, IngredientID, UpdateTimestamp, HistoricalPrice) Values(%s, %s, %s, %s)"
        values = (StoreID, IngredientID, UpdateTimestamp, HistoricalPrice)
        cursor.execute(query, values)
        
connection.commit()