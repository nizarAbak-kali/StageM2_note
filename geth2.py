from bs4 import BeautifulSoup


file  = open("Good patching practice.html", "r")

soup = BeautifulSoup(file)

for h2 in soup.find_all('h2'):
    print h2


file.close();
