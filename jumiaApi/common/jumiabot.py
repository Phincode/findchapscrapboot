import requests
from bs4 import BeautifulSoup
import time
class headers:
    def __init__(self):
        self.header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'

        }
def scrapdatadeals(category,keyword):
    ss = requests.Session()
    head = headers()
    if category == '':
        category = 'catalog'
    header1 = head.header
    header1['Referer']='https://deals.jumia.ci/'+category+'?search-keyword='+keyword
    url = ss.get('https://deals.jumia.ci/'+category+'?search-keyword='+keyword,headers = header1,verify=False)
    soup = BeautifulSoup(url.text,'lxml')
    all_article = soup.findAll('article')
    all_data = []
    if all_article:
        for article in all_article:
            aa = 0
            try:
                aa = ss
                id = eval(article['data-event'])['id']
                Product_name = str(eval(article['data-event'])['title'])
                Product_price = eval(article['data-event'])['price']
                Product_address = article.find('span',{"class":'address'}).text.replace('\n','').replace(' ','')
                Product_time = article.find('time').text
                Product_details = Product_address + '|' + Product_time
                Product_image = article.find('img')['data-src']
                Product_url = 'https://deals.jumia.ci'+article.find('a')['href']
                product_open = aa.get(Product_url,headers = header1,verify=False)
                soup = BeautifulSoup(product_open.text,'lxml')
                try:
                    Vender_name = soup.find('dl').find('span',{'itemprop':"name"}).text
                    Vender_location = soup.find('dl').find('span',{'itemprop':"addressLocality"}).text
                    Vender_contact = soup.find('div',{'class':'phone-box show'}).find('a').text
                except:
                    Vender_name = ''
                    Vender_location = ''
                    Vender_contact = ''
                Site_name = 'deals.jumia.ci'
                all_data.append({
                    'Product_name':Product_name,
                    'Product_price':Product_price,
                    'Product_details':Product_details,
                    'Product_image':Product_image,
                    'Product_url':Product_url,
                    'Vender_name':Vender_name,
                    'Vender_location':Vender_location,
                    'Vender_contact':Vender_contact,
                    'Site_name':Site_name
                    })
                time.sleep(2)
            except Exception as e:
                print(str(e))
                pass
    return all_data
def scrapdatajumia(keyword):
    try:
        ss = requests.Session()
        frist_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.jumia.ci/?__cf_chl_captcha_tk__=2e4e42aabbd415dae890134268cc30d9e3b64b71-1590824165-0-AXZq-4aGJrz6svDTw46SqM7Z8jf4-4SHQkxf47XOgUlQkKah_sPeijXjG9rDFlQJvKZS1UNBM3V8ldjf75Zbm5UigIOolznwykXpwa0bu-YB2bsC4QvONLHW92HJGx4x4DAhTsV5_7QUfeYs4Wpn1ZcLBhxmye66xRUNm7w27ExX-rMM4q_eTL4QFJs6GBuszE0Cgv658VwtHktHi1A-ZzNdUtmPxO7BV8d5r1HjIzx2kU-vc5ZtfZIWN_vcvtoe75RibCZT8oXObIOlMiAsQmUwmaS16V8WdufoMz6QTatx4WX9cEhanPjPcKYiewWRelkt_vW6QlW747kgGSm_kWoIAl6LmtJ-kMO5TycEqKjzl0dte74Ic5cvKsjBDQVSxnsnFLC3e1be6ZbFjX9FJDjZI3PhdYh84O9Ksw9YNNJea3FVeDHZpeQKF6BAWPjf4nJRpw9PbnJgoFixjafX_YtK-Ng7zRxcXi5mGqcqYW2BGs21YdaTPBjpNcQrx9JpMpyBLPct3IqOTYBbMF-RS81NTAUxoeKUDO_TlKgpvmrz',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        
        url = ss.get('https://www.jumia.ci/catalog/?q='+keyword,headers = frist_headers,verify=False)
        soup = BeautifulSoup(url.text,'lxml')
        all_article = soup.findAll('article')
        all_data = []
        if all_article:
            for article in all_article:
                if article.find('img'):
                    try:
                        Product_name = article.find('div',{'class':'info'}).find('h3').text
                        Product_price = article.find('div',{'class':'info'}).find('div').text.split(' ')[0]
                        Product_details = article.find('div',{'class':'info'}).find('h3').text
                        Product_image = article.find('img')['data-src']
                        Product_url = 'https://www.jumia.ci'+article.find('a')['href']
                        Site_name = 'www.jumia.ci'
                        Vender_name = ''
                        Vender_location = ''
                        Vender_contact = ''
                        all_data.append({
                            'Product_name':Product_name,
                            'Product_price':Product_price,
                            'Product_details':Product_details,
                            'Product_image':Product_image,
                            'Product_url':Product_url,
                            'Vender_name':Vender_name,
                            'Vender_location':Vender_location,
                            'Vender_contact':Vender_contact,
                            'Site_name':Site_name
                        })
                    except:
                        pass
            return all_data
    except:
        all_data = []
        return all_data

