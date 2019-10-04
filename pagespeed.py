# -*- coding: utf-8 -*-

try:
  import datetime
  import gspread ## put in another folder
  import requests
  from oauth2client.service_account import ServiceAccountCredentials # put in another folder
  import json
except Exception as e:
  raise e

## CONSTANTS
API_BASE = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
SCOPES = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']


## class PageSpeedv5
class PageSpeedv5():
  def __init__(self, api_key, url, strategy):
    self.params = {
      'url': url,
      'key': api_key,
      'strategy': strategy
    }

  def _requestor(self):
    return requests.get(API_BASE, params=self.params).json()

  def fetch_all(self):
    try:
      return self._requestor()
    except Exception as e:
      raise e

  def fetch_light_house(self):
    try:
      return self._requestor()['lighthouseResult']['audits']
    except Exception as e:
      raise e


## class SpreadsheetReporter
class SpreadsheetReporter():
  def __init__(self, file_data):
    self.data = json.loads(file_data)
    self.credentials = ServiceAccountCredentials.from_json_keyfile_dict(self.data, scopes=SCOPES)

  def _authorize(self):
    try:
      return gspread.authorize(self.credentials)
    except Exception as e:
      raise e

  def open(self, doc_id, sheet_page):
    try:
      auth = self._authorize()
      sheets = auth.open_by_key(doc_id)
      self.working_sheet = sheets.get_worksheet(sheet_page)
    except Exception as e:
      raise e

  def set_daily_metrics(self, light_house_result):
    current_time = datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S.%f")
    self.values = [
      current_time,
      light_house_result['first-contentful-paint']['displayValue'],
      light_house_result['speed-index']['displayValue'],
      light_house_result['first-meaningful-paint']['displayValue'],
      light_house_result['first-cpu-idle']['displayValue'],
      light_house_result['max-potential-fid']['displayValue']
    ]
    self.working_sheet.append_row(self.values)
