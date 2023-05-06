from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = "https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule"
# Request in case 404 Forbidden error
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

print(soup.title.text)

myclasses = ['MW 2:30 p.m.', 'MW 4:00 p.m.',
             'TR 9:30 a.m.', 'TR 11:00 a.m.', 'TR 2:00 p.m.']


finals_rows = soup.findAll("tr")


for row in finals_rows:
    final = row.findAll('td')
    if final:
        myclass = final[0].text
        if myclass in myclasses:
            print(
                f'For class: {myclass} the final is scheduled for {final[1].text} at {final[2].text}')

            # look at powerpoints, look at in class work, part 2 is webscraping (will give first few lines), part 1 is MC and fill in blank
            # similar to the MOVIES EXAMPLE and PROJECT
            # gives you list comprehension and know what to do with it (multiple choice)
            # high level questions on SQL
