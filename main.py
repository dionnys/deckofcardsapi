import requests

if __name__ == '__man__':
    url = 'https://deckofcardsapi.com/api/deck/new/shuffle/'
    args = {'desk_count': '1'} 
    response = requests.get(url, params=args)

    
    print (response)
    print (response.url)
    
    if response.status_code == 200:
        print (response.content)
        content = response.content
"""
        file = open ('archivo.txt', 'wb')
        file.write(content)
        file.close()
"""        