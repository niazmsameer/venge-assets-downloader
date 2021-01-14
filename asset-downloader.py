import urllib.request, urllib.error, json, os
from nested_lookup import nested_lookup

# Gotta plug my socials y'know
print('Venge Assets Downloader')
print('-----------------------')
print('Git Repository: https://github.com/niazmsameer/venge-assets-downloader')
print('Instagram: @syn7ax.error | Discord: Syn7ax#4537')
print('-----------------------')

# Script Config
URL = 'https://venge.io/config.json'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# The request responsible for getting the config
config_request = urllib.request.Request(URL, headers=HEADERS)

# Retrieve the data from the Venge servers
with urllib.request.urlopen(config_request) as url:
  print('Retrieving config JSON file...')

  # Decode raw data into a Dictionary
  config_json = json.loads(url.read().decode())

  print('Looking up URLs...')

  # Lookup Dict for urls
  resources = nested_lookup('url', config_json)

  file_count = len(resources)
  progress_counter = 0

  print('Found ' + str(file_count) + ' URLs, starting download loop')

  # Iterate over the URLs
  for resource in resources:
    # Increment counter
    progress_counter += 1

    # Print status update
    print('File ' + str(progress_counter) + ' of ' + str(file_count))

    # Append download target folder
    file_loc = 'downloads/' + resource

    # Append host to every url
    resource_loc = 'https://venge.io/' + resource

    # Auto create subfolders if needed
    os.makedirs(os.path.dirname(file_loc), exist_ok=True)

    # Perform request
    resource_request = urllib.request.Request(resource_loc, headers=HEADERS)
    try:
      url = urllib.request.urlopen(resource_request)
      with open(file_loc, 'b+w') as file:
        # Write stream to file
        file.write(url.read())
    except urllib.error.HTTPError:
      # Handle HTTP errors
      print('Skipping file ' + str(progress_counter) + ' due to an HTTP error. (File might possibly be 404)')
