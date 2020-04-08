from os import mkdir, chdir, listdir
from requests import get
from re import findall
from sys import argv

def main():

	file = open("wordlist.txt", "r")
	links = file.readlines()
	file.close()

	if "screenshots" in listdir():
		chdir("screenshots")
	else:
		mkdir("screenshots")
		chdir("screenshots")

	if len(argv) > 1:
		ch = int(argv[1])
	else:
		ch = 0

	for link in links[ch:]:

		try:
			URL = "https://prnt.sc/" + link[:-1]
			print("[%i] Trying %s..." % (ch, URL), end = "")
			res = get(URL, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'})
		
			if res.status_code == 200:
				pic_link = findall('"(https://.*?)"', res.text)[0]
			
				if pic_link == URL:
					print("nothing.")
			
				else:
					file = open(pic_link.split("/")[-1], "wb")
					file.write(get(pic_link).content)
					file.close()
					print("screenshot found and saved.")

			else:
				input("WARNING %i" % (res.status_code))

			ch += 1
		except KeyboardInterrupt:
			if input("\nPaused. Press Enter for continue, or 'E' for exiting: ") == "c".lower():
				exit(0)
			else:
				continue

main()