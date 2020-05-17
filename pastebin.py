import json
import requests, os, sys
def main():
	os.system("clear")
	print """
 ____           _       _     _
|  _ \ __ _ ___| |_ ___| |__ (_)_ __
| |_) / _` / __| __/ _ \ '_ \| | '_ \

|  __/ (_| \__ \ ||  __/ |_) | | | | |
|_|   \__,_|___/\__\___|_.__/|_|_| |_|

Author	: \033[91mWibuCode\033[97m
Github	: \033[91mhttps://github.com/wibucode\033[97m
------------------------------------------
masukkan nama_file.ext (inifile.py)
jika file ada di sdcard (/sdcard/file.ext)
"""

	url = "https://pastebin.com/api/api_post.php"
	nama_file = raw_input("\033[93mNama File	: \033[97m")
	name = raw_input("\033[93mNama Kamu	: \033[97m")
	file = open(nama_file, "rb")
	files = file.read()
	payload = {
		'api_dev_key':'6b3ba093ef789e580f505f7a9eee2993',
		'api_option':'paste',
		'api_paste_name':name,
		'api_paste_code':files
	}
	r = requests.post(url, payload)
	print "link =>		: \033[91m"+r.content+"\033[97m \n"
	ask = raw_input("Ingin menggunakannya lagi y/n	: ").lower()
	if ask == "y":
		main()
	elif ask == "n":
		sys.exit()
	else:
		print "\033[91mPilih y/n ?\033[97m"
try:
	main()
except KeyboardInterrupt:
	print "Ctrl + C (exit)"
