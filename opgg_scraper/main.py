from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from champion_template import champ_lst
import json
def wr_lst_to_dict(lst):
    new_dict = {}
    for x in range(1, len(lst), 2):
        lst[x] = lst[x][:5]
    for x in range(0, len(lst), 2):
        key = lst[x].replace(" ", "")
        key = key.replace("'", "")
        key = key.replace(".", "")
        if key == "Wukong":
            key = "MonkeyKing"
        if key == "Nunu&Willump":
            key = "Nunu"
        value = lst[x+1]
        new_dict[key] = value
    return new_dict

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Here

driver =  webdriver.Chrome(options=options)
#nothing defaults to emerald+
TIER = ""
ROLE = ""
CHAMP = ""
empty_check = False
roles = ["top", "jungle", "mid", "adc", "support"]
url = 'https://www.op.gg/champions/'
champ_dict = {}
f = open("champ_data.json", "w")
for champ in champ_lst:
    champ_dict[champ] = {}
    for role in roles:
        new = "%s/counters/%s" % (champ, role)
        new_url = url + new
        driver.get(new_url)
        time.sleep(1)
        tbody = driver.find_element(By.CLASS_NAME, "table-container")
        if len(tbody.text) < 30:
            empty_check = True
            continue
        new_text = tbody.text.splitlines()
        new_text.pop(0)
        role_dict = {role: wr_lst_to_dict(new_text)}    
        champ_dict[champ].update(role_dict)
    print(champ_dict)
    json.dump(champ_dict, f)
    f.write("\n")
    

driver.quit()



