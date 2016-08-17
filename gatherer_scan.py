import requests
import bs4


def scrape_soi():

    r = requests.get(\
        'http://gatherer.wizards.com/Pages/Search/Default.aspx?page=0&set=%5B%22Shadows%20over%20Innistrad%22%5D')

    with open("soi.txt", "w") as f:
        f.write(r.text.encode('utf-8'))

    r = requests.get(\
        'http://gatherer.wizards.com/Pages/Search/Default.aspx?page=1&set=%5B%22Shadows%20over%20Innistrad%22%5D')

    with open("soi.txt", "a") as f:
        f.write(r.text.encode('utf-8'))

    r = requests.get(\
        'http://gatherer.wizards.com/Pages/Search/Default.aspx?page=2&set=%5B%22Shadows%20over%20Innistrad%22%5D')

    with open("soi.txt", "a") as f:
        f.write(r.text.encode('utf-8'))

    r = requests.get(\
        'http://gatherer.wizards.com/Pages/Search/Default.aspx?page=3&set=%5B%22Shadows%20over%20Innistrad%22%5D')

    with open("soi.txt", "a") as f:
        f.write(r.text.encode('utf-8'))

    #print (r.text)

#scrape_soi()


def convert_data(html_soup):
    #print(html_soup)

    print ""
    card_name = html_soup.find('img')['alt']
    print card_name

    type_line = html_soup.find('span','typeLine').text
    card_types = " ".join(type_line.split())
    print card_types

    mana_line = html_soup.find('span','manaCost')
    #print mana_cost
    mana_cost = ""
    for entry in mana_line.find_all('img'):
        mana_cost = mana_cost + " " + entry['alt']
    mana_cost = mana_cost.strip()
    print mana_cost

    rules_div = html_soup.find('div','rulesText')
#    print rules_div
    for entry in rules_div.find_all('p'):
        print entry.text

    set_line = ""
    for entry in html_soup.find_all('img'):
#        print entry['src']
        if "rarity=" in entry['src']:
            set_line = entry
    print set_line['alt']
    print ""



with open("soi.txt", "r") as f:
    text = f.read()
    soup = bs4.BeautifulSoup(text, 'html.parser')
    #print (soup.find('tr').find('tr'))

    main_tr = soup.find('tr')

    print(main_tr.find('tr'))

    for i in main_tr.find_all('tr'):
        convert_data(i)



#print(soup.find_all('tr'))
#http://gatherer.wizards.com/Pages/Search/Default.aspx?page=0&set=%5B%22Shadows%20over%20Innistrad%22%5D