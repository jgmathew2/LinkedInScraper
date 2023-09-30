from bs4 import BeautifulSoup
import requests
def linkFilter(url):

    keywords = ["Freshman", "freshman", "Sophomores", "sophomores", "2026", "2027"]
    techs = ["Java", "java", "JavaScript", "Javascript", "React", "react", "javascript", "Web", "web", "spring", "Spring"]
    turnOffs = ["2024", "2025", "junior", "senior", "Junior", "Senior"]

    url = url.get("href")
    if(url == None or "https://www.linkedin.com/jobs" not in url):
        return False
    else:
        doc = BeautifulSoup(requests.get(url).text, "html.parser")

        #print(doc.prettify())

        descript = doc.find_all("p")
        descript.extend(doc.find_all("script"))

        for para in descript:
            text = para.getText()

            if "intern" in text or "Intern" in text or "co-op" in text or "Co-op" in text:
                for keyword in keywords:
                    if(keyword in text):
                        return True

                for turnOff in turnOffs:
                    if(turnOff in text):
                        return False

                for tech in techs:
                    if(tech in text):
                        return True
        return False
def web_scrape(url, linkList, start):

    if len(linkList) > 3:
        return linkList

    result = requests.get((url + str(start)))

    doc = BeautifulSoup(result.text, "html.parser")

    listOfLinks = doc.find_all("link")

    listOfLinks.extend(doc.find_all("a"))

    filteredLinks = filter(linkFilter, listOfLinks)

    linkList.extend(filteredLinks)

    web_scrape(url, linkList, start + 25)

    return linkList
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    """
    result = requests.get("https://www.linkedin.com/jobs/view/2024-summer-internship-software-development-at-dv-trading-llc-3712686052?refId=rnzfNodRItbgn8G%2Fm08e4A%3D%3D&trackingId=%2Fb6Z4jZGV41yP1sB4Ns%2FyA%3D%3D&position=5&pageNum=0&trk=public_jobs_jserp-result_search-card")
    doc = BeautifulSoup(result.text, "html.parser")
    descript = doc.find_all("p")
    descript.extend(doc.find_all("script"))
    for text in descript:
        print(text.getText())
    """
    listoflinks = web_scrape("https://www.linkedin.com/jobs/search/?currentJobId=3711769308&geoId=103644278&keywords=software%20engineer%20intern&location=United%20States&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&start=", [], 0)

    # "https://www.linkedin.com/search/results/all/?keywords=software%20engineer%20intern&origin=HISTORY&sid=!0w"
   # given BeatifulSoup doc, recursively find 100 links
    for link in listoflinks:
       print(link.get("href"))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
