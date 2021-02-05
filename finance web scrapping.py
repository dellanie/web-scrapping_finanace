## web scarpping the current finacial market positions of S&P 500, Crude Oil and other indices

import pandas as pd
import requests
from bs4 import BeautifulSoup

page= requests.get("https://finance.yahoo.com/") 
soup= BeautifulSoup(page.content, "html.parser")
finance =soup.find(id ='Lead-3-FinanceHeader-Proxy')

#print (finance)

items = (finance.find_all(class_=' D(ib) Bxz(bb) Bdc($seperatorColor)  Mend(10px)  BdEnd '))

title_name = [finance.find(class_='Fz(s) Ell Fw(600) C($linkColor)').get_text() for fin in finance]
volume = [finance.find(class_='Trsdu(0.3s) Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)').get_text() for fin in finance]
current_growth = [finance.find(class_='Mstart(2px)').get_text() for fin in finance]

#print(title_name)
#print(volume)
#print(current_growth)

fnance_analysis = pd.DataFrame(
    {
        'title': title_name,
        'vol': volume,
        'growth': current_growth

    })

print(fnance_analysis)


fnance_analysis.to_csv('finance.csv')
