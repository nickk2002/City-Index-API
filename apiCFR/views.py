from datetime import date

from django.http import JsonResponse, HttpResponse

from apiCFR.scraper import CFRScraper


def trains(request):
    if "city" in request.GET:
        city = request.GET["city"]
    else:
        return HttpResponse(
            "<h1>Sa pui city ca parametru</h1>"
            "https://cfr-scraper.herokuapp.com/?city=Bucuresti-Nord&date=15.06.2022 sau https://cfr-scraper.herokuapp.com/?city=Bucuresti-Nord pentru date=now")
    if "date" in request.GET:
        date_to_search = request.GET["date"]
    else:
        date_to_search = date.today().strftime("%d.%m.%y")
        print("Date not specified using now:", date_to_search)

    scraper = CFRScraper()
    json_data = scraper.scrape(city, date_to_search)
    if not json_data:
        return HttpResponse(f"Nu am gasit nimic pentru {city} si data {date_to_search}")
    return JsonResponse(json_data, safe=False)
