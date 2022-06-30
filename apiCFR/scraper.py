import requests
from bs4 import BeautifulSoup


def get_type(table_soup: BeautifulSoup, journey_type: str, city_from: str):
    information = []
    for row in table_soup.find_all("li"):
        row = row.find("div", class_="row")
        time = row.find("div", class_="line-height-1-25").find_all("div")[1].text.strip()
        to = row.find("a").text.strip()
        number = row.select_one("div:nth-child(3)").text
        number = ' '.join(number.split()[1:])
        print(number)
        information.append({
            "tip": journey_type,
            "statie1": to,
            "statie2": city_from,
            "time": time,
            "number": number
        })
    return information


class CFRScraper:
    run = True
    headers = {"Host": "mersultrenurilor.infofer.ro",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
               "Accept": "*/*",
               "Accept-Language": "en-US,en;q=0.5",
               "Accept-Encoding": "gzip, deflate, br",
               "Referer": "https://mersultrenurilor.infofer.ro/ro-RO/Statie/Bucuresti-Nord?Date=15.06.2022",
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               "X-Requested-With": "XMLHttpRequest",
               "Content-Length": "282",
               "Origin": "https://mersultrenurilor.infofer.ro",
               "Connection": "keep-alive",
               "Sec-Fetch-Dest": "empty",
               "Sec-Fetch-Mode": "no-cors",
               "Sec-Fetch-Site": "same-origin",
               "TE": "trailers",
               "Pragma": "no-cache",
               "Cache-Control": "no-cache"}
    url = "https://mersultrenurilor.infofer.ro/ro-RO/Stations/StationsResult"

    @staticmethod
    def build_url(station: str, date: str):
        return f"https://mersultrenurilor.infofer.ro/ro-RO/Statie/{station}?Date={date}"

    def scrape(self, station: str, date: str):
        url = "https://mersultrenurilor.infofer.ro/ro-RO/Stations/StationsResult"
        if self.run:
            response = requests.post(
                url,
                headers=self.headers,
                data=f"Date={date}&StationName={station}&ReCaptcha=&ConfirmationKey=a&IsSearchWanted=True")
            content = response.content
        else:
            with open("output.html", "r", encoding='utf-8') as f:
                content = f.read()

        soup = BeautifulSoup(content, features='html.parser')
        try:
            plecari = soup.find_all("ul", class_="list-group")[0]
        except IndexError:
            return []
        data = get_type(plecari, "Pleaca", station)

        sosiri = soup.find_all("ul", class_="list-group")[1]
        data.extend(get_type(sosiri, "Sosire", station))
        return data


if __name__ == "__main__":
    data = CFRScraper().scrape("Bucuresti-Nord", "15.06.2022")
    print(data)
