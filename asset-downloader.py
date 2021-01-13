import urllib.request, urllib.error, json, os
from nested_lookup import nested_lookup

URL = 'https://venge.io/config.json'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

request = urllib.request.Request(URL, headers=HEADERS)

with urllib.request.urlopen(request) as url:
  # Retrieve the data from the Venge servers
  data = json.loads(url.read().decode())

  # Perform a nested key lookup and the
  # retrived JSON object
  # urls will store all the resource
  # locations
  urls = nested_lookup('url', data)

  url_count = len(urls)
  counter = 0

  # Iterate over the URLs
  for resource_temp in urls:
    counter += 1

    print('File ' + str(counter) + ' of ' + str(url_count))

    # Append download target folder
    file_loc = 'downloads/' + resource_temp

    # Append host to every url
    resource = 'https://venge.io/' + resource_temp

    # Auto create subfolders if needed
    os.makedirs(os.path.dirname(file_loc), exist_ok=True)

    req = urllib.request.Request(resource, headers=HEADERS)
    try:
      url = urllib.request.urlopen(req)
      with open(file_loc, 'b+w') as file:
        file.write(url.read())
    except urllib.error.HTTPError:
      print('Skipping file ' + str(counter) + ' due to an HTTP error. (File might possibly be 404)')