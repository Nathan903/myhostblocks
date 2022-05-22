import urllib.request
from datetime import datetime

src = r"https://anti-ad.net/easylist.txt"
bannedinitials=r"@@"

now = datetime.now() 
result="!cleaned by nathan. Generated on "+now.strftime("%m/%d/%Y, %H:%M:%S")+"\n"
with urllib.request.urlopen(src) as data:
    for line in data:
        line=line.decode("utf-8")
        if bannedinitials in line:
            #print(line)
            pass
        else:
            result+=line
with open("anti-ad-easylist-cleaned.txt", "w", encoding="utf-8") as f:
    f.write(result)
    f.close()
