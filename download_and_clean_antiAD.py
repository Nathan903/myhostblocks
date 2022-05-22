import urllib.request
src = r"https://anti-ad.net/easylist.txt"
bannedinitials=r"@@"


result="!cleaned by nathan\n\n"
with urllib.request.urlopen(src) as data:
    for line in data:
        line=line.decode("utf-8")
        if bannedinitials in line:
            print(line)
        else:
            result+=line
with open("anti-ad-easylist-cleaned.txt", "w", encoding="utf-8") as f:
    f.write(result)
    f.close()
