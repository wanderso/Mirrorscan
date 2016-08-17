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
    print(html_soup)
    card_name = html_soup.find('img')['alt']
    print card_name

with open("soi.txt", "r") as f:
    text = f.read()
    soup = bs4.BeautifulSoup(text, 'html.parser')
    #print (soup.find('tr').find('tr'))

    main_tr = soup.find('tr')

    convert_data(main_tr.find('tr'))

#    for i in main_tr.find_all('tr'):
#        print (i)


#print(soup.find_all('tr'))
#http://gatherer.wizards.com/Pages/Search/Default.aspx?page=0&set=%5B%22Shadows%20over%20Innistrad%22%5D