from django.shortcuts import render_to_response
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json
from settings import MYNETA_STATES_NAMES

def home(request):
    """ Render to home page"""
    return render_to_response('index.html', {'MYNETA_STATES_NAMES': MYNETA_STATES_NAMES})


def get_html_from_url(url):
    """ 
    Method to retrieve html page from url and 
    converting it to beautiful soup object
    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    return soup


def mynetaapi(request):
    """ Method to fetch data from myneta.info """
    state = request.GET['state'] if 'state' in request.GET else 'delhi'
    year = request.GET['year'] if 'year' in request.GET else 2015

    try:
        url = """http://myneta.info/%s%s/index.php?action=show_winners&sort=default"""%(state, str(year))
        soup = get_html_from_url(url)
        winner_row = soup.find_all('table')
        if not len(winner_row):
            return HttpResponse(json.dumps({
                'status_code': 100,
                'status_msg': 'No Data Found',
                'data': []
            }))
        winner_row = winner_row[2].find('tbody').contents
        winner_data = []
        for winner in winner_row:
            try:
                wdata = winner.contents
                winner_data.append({
                    'name': wdata[3].text,
                    'constituency': wdata[4].text,
                    'party': wdata[6].text,
                    'criminal_case': wdata[8].text,
                    'education': wdata[10].text
                })
            except:
                continue 
        return HttpResponse(json.dumps({
            'status_code': 200,
            'status_msg': 'Success',
            'data': winner_data
        }))
    except Exception, e:
        return HttpResponse(json.dumps({
            'status_code': 400,
            'status_msg': 'Error: ' + str(e),
            'data': []
        }))
