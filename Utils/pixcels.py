from pexels_api import API

PEXELS_API_KEY = '563492ad6f917000010000014e15b808af134640bb351ac9a2b7ebc0'

def pixels(keyword,page,result):
  api = API(PEXELS_API_KEY)

  api.search(keyword, page=page, results_per_page=result)

  photos = api.get_entries()
  urls = []
  for photo in photos:
    # Print photographer
    # print('Photographer: ', photo.photographer)
    #  Print url
    # print('Photo url: ', photo.url)
    # Print original size url
    urls.append(photo.original)
    # print('Photo original size: ', photo.original)
  return urls

# print(pixels(keyword="apple",page=1,result=10))