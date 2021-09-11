import configparser
from imgurpython import ImgurClient

config = configparser.ConfigParser()
config.read('auth.ini')

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')
client = ImgurClient(client_id, client_secret)

''' # Extracts the items (images) on the front page of imugur.
items = client.gallery()
for item in items:
    print(item.link)
    print(item.title)
    print(item.views)
'''
# Find the image on the front page that has the highest number of views
items = client.gallery()
maxitem = None
maxviews = 0

for item in items:
    if item.views > maxviews:
        maxitem = item
        maxviews = item.views
print(maxitem.title)
print(maxitem.views)
print(maxitem.link)
