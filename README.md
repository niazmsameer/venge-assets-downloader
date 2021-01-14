# Venge Assets Downloader

Venge assets downloader is a python script that fetches the latest config.json file from the Venge servers and looks up all the assets and it's locations on the server. Then, it will download all the resources and place them in the appropiate folders. This can be useful if you're building clients for Venge.io.

## Usage (Simple)

You will need a version of Python 3 installed on your computer.

You will also need one dependency which is 'nested-lookup'. It's responsible for looking up the urls in the configuration JSON object. To install it, you will need to use Pip. (A python package manager)

Installing with Pip:
`pip install nested-lookup`

If you have Python 2 and Python 3 installed on your computer:
`pip3 install nested-lookup`

If you're not sure which command to use, try running `python --version`. If it returns `2.x.x`, use `pip3`, otherwise use `pip`.

After installation is complete, you can now execute the script.

Open a command prompt/terminal session and `cd` your way into the folder containing the `asset-downloader.py` script. Then execute the following command:

`python asset-downloader.py`

If you used the `pip3` to install the dependency, then you will need to run:
`python3 asset-downloader.py`.

Once you run the command, the console will start printing out status updates like `File x of x`.

If you go to the folder containing the script, you will notice that there is a new `downloads` folder. That folder will contain all the downloaded assets. The speed of the download process will depend on your internet speed.

## Usage (With Pipenv)

If you'd like to use Pipenv to seperate dependencies according to projects.

_TODO: To be written_

## Support

Contact me on Discord: Syn7ax#4537