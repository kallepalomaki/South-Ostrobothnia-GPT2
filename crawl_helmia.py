import requests
from bs4 import BeautifulSoup

#main_page_link="http://pohopekka.blogspot.com/"
main_page_link="https://www.blogit.fi/tag/pakina"
#main_page_link=fi_wiki_link+"/wiki/Seitsem%C3%A4n_veljest%C3%A4"

page=requests.get(main_page_link)
soup = BeautifulSoup(page.content, 'html.parser')
links=soup.find_all("a")
with open("helmia.txt", "w") as f:
    for link in links:
        if "helmia" in link.get("href"):
            print(link.get("href"))
            page2 = requests.get(link.get("href"))
            soup2 = BeautifulSoup(page2.content, 'html.parser')
            data=soup2.find_all("div", {"class":"entry-content"})
            data1=data[0].find_all("p")
            for item in data1:
                #print(item.text)
                line_splitted=item.text.split(". ")
                for line in line_splitted:
                    line_text=line + ". "
                    line_text=line_text.replace("..",".")
                    if len(line_text) > 3:
                        f.write(line_text + "\n")
