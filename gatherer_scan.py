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

    soup = bs4.BeautifulSoup(r.text, 'html.parser')


#print(soup.find_all('tr'))
#http://gatherer.wizards.com/Pages/Search/Default.aspx?page=0&set=%5B%22Shadows%20over%20Innistrad%22%5D