import os
from dotenv import load_dotenv
from pagespeed import SpreadsheetReporter
from pagespeed import PageSpeedv5 


load_dotenv(verbose=True)
SHEET_PAGE = 0
page = PageSpeedv5(
  os.getenv("API_KEY"),
  os.getenv("URL"),
  os.getenv("STRATEGY")
)
reporter = SpreadsheetReporter(os.getenv("AUTH_FILE"))

reporter.open(
  os.getenv("SHEET_ID"), 
  SHEET_PAGE
)
light_result = page.fetch_light_house()
reporter.set_daily_metrics(light_result)
