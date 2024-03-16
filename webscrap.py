import requests
from bs4 import BeautifulSoup
import time

url = "https://www.moneycontrol.com/stocksmarketsindia/"
print(url)

response=requests.get(url)
if response.status_code==200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup)
    # Find all the elements with the class "gs-c-promo-heading"
    # headlines = soup.find_all(class_="bs-image image-crop")
    headlines = soup.find_all(class_="title_24px CTR title_botline")
    #print(headlines)

    for headline in headlines:
        title = headline.get_text(strip=True)
        print(title)

    #mctable1
        
    table=soup.find("table", class_='mctable1')

    if table:
        rows=table.find_all("tr")

         # Iterate over the rows
        cells=[] 
        for row in rows:
            cells=(row.find_all("td"))

            
            row_data=[cell.get_text(strip=True) for cell in cells]

            print("table data", row_data)


    else:
         print("table data")










    # if headlines:
    #     div_text=headlines.get_text(strip=True)
    #     print("Text of the div element",div_text)
    # else:
    #     print("Div element not found")    
    # trtaglist=headlines.find_all('tr')
    # print(trtaglist)


    
    # Iterate over the headlines and extract the title and link
    # for headline in headlines:
    #     # Extract the title text
    #     title = headline.find("a").get_text(strip=True)
        
    #     # Extract the link URL
    #     link = headline.find("a")["href"]
        
    #     # Print the title and link
    #     print("Title:", title)
    #     print("Link:", link)
    #     print()
else:
    print("Failed to retrieve the webpage.")
