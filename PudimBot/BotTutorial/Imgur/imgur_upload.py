from auth import authenticate
from datetime import datetime

album = None
image_path = '07133250949243.jpg'

def upload_image(client):
    """
    Uploads an image to imgur
    """

    config = {
        'album': album,
        'name': 'Jacaré',
        'title': 'psiquiatra',
        'description': 'when meu jacarezinho got upload: {0}' .format(datetime.now())
    }

    print('Uploading image...')
    image = client.upload_from_path(image_path, config=config, anon=False)
    print('Done')
    print()

    return image

if __name__ == "__main__":
    client = authenticate()
    image = upload_image(client)

    print('Image was posted!')
    print(f'You can find the image here: {image["link"]}')
