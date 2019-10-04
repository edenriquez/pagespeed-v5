# pagespeed-v5

![Action Status](https://action-badges.now.sh/edenriquez/pagespeed-v5?workflow=metrics)



Python wrapper over [Google Page Speed v5](https://developers.google.com/speed/docs/insights/v5/get-started)and optional integration over [Google SpreadSheet](https://developers.google.com/sheets/api) to bulk common metrics  information.

- First Contentful Paint	
- Speed Index	
- First Meaningful Paint	
- First CPU Idle	
- Max Potential First Input Delay

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt.
```

## pagespeed Usage

```python
from pagespeed import PageSpeedv5 

page = PageSpeedv5(
  os.getenv("API_KEY"), # pagespeed console api key
  os.getenv("URL"),     # https://example.com
  os.getenv("STRATEGY") # desktop or mobile
)
# get light_house_result object
light_result = page.fetch_light_house()

# or get entire object
light_result = page.fetch_all()

```

## (optional ) spreadsheet Usage

```python
from pagespeed import SpreadsheetReporter

SHEET_PAGE = 0

# AUTH_FILE json account service private key 
# https://console.developers.google.com/apis/credentials
reporter = SpreadsheetReporter(os.getenv("AUTH_FILE"))

reporter.open(
  os.getenv("SHEET_ID"), 
  SHEET_PAGE
)

# where light_result could be for instance 
# light_result = page.fetch_light_house()

reporter.set_daily_metrics(light_result)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
