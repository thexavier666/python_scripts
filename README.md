# Some Useful Python Scripts

These are some scripts I developed which I needed to automate. Hopefully it might be useful for someone else.
But keep it in mind it might not work **perfectly** for you as these are tailored for my specific needs.

### `get_ip.py`
Prints only the IP in the console and nothing else

#### Prerequisites
None
#### Usage
`python get_ip`

### `list_downloader.py`
Downloads a given list of items in parallel. Works really well when you have a lot of bandwidth 
#### Prerequisites
None
#### Usage
`python list_downloader file_name`

### `ping_check.py`
This is useful when a particular host is down and you want to get alerted when the host comes back online

#### Prerequisites
* The host must be pingable
* `totem-audio-preview` - Standard with Gnome distribution
* One music file which will serve as the alert

#### Usage
`python ping_check host_ip`

### `mp3_downloader.py` 
It downloads a list of videos from youtube specified in a file and converts them to mp3

#### Prerequisites
* `youtube_dl` - Needs to be installed
* `ffmpeg` - Needs to be installed

#### Usage
`python mp3_downloads file_name`