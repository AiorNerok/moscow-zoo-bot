from bs4 import BeautifulSoup
import json


db =[]

with open("Животные Московского зоопарка.html", 'r') as f:
    soup = BeautifulSoup(f.read())

    res = soup.find(class_="sp-block-list df_ajax_list")    
    links = res.find_all('a')
    
    for i in links:
        label = i.text.strip()
        src = str(i.find('img')['src']).replace("./Животные Московского зоопарка_files/","")
        link_to_more_info = i["href"]
        db.append({"name": label,"src":src,"link_to_more_info":link_to_more_info})


with open("db.json", "w") as out:
    json.dump(db, out, ensure_ascii=False)