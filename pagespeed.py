# -*- coding: utf-8 -*-
import datetime
import gspread
import requests

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)

gc = gspread.authorize(credentials)

sh = gc.open_by_key('xxxxx')

for idx, sheet in enumerate(sh.worksheets()):
    if sheet.spreadsheet.title == "xxxx":
        worksheet = sh.get_worksheet(idx-1)


api_key = 'xxxxx'
url = 'xxxx'
strategy = 'desktop'

params = {
    'url': url,
    'strategy': strategy,
    'key': api_key
}
endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

def request(params):
    response = requests.get(endpoint, params=params)
    return response.json()

all = request(params)
light = all['lighthouseResult']
light['audits']['first-contentful-paint']['displayValue']
light['audits']['first-meaningful-paint']['displayValue']
light['audits']['speed-index']['displayValue']
light['audits']['first-cpu-idle']['displayValue']
light['audits']['max-potential-fid']['displayValue']


# review these 

light['audits']['diagnostics']
# light['first-contentful-paint']['displayValue'].replace(u'\xa0', u' ')


current_time = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")
# worksheet.update_acell('A3', current_time)
