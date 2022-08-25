import datetime
import time

import gspread
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from google_sheet_sender.spiders.books import BooksSpider

WORKSHEET_NAME = 'latest_run'
GSHEET_URL = 'https://docs.google.com/spreadsheets/.....'
CREDENTIALS_FILE = "./config/credentials.json"


def run_spider(spider_to_run):
    start_time = time.time()
    settings = get_project_settings()
    settings['FEEDS'] = {
        csv_name: {
            'format': 'csv',
            'overwrite': True
        },
    }
    process = CrawlerProcess(settings)
    process.crawl(spider_to_run)
    process.start()
    print("\n\n{:.2f} Seconds".format(time.time() - start_time))


def update_gsheet():
    df = pd.read_csv(csv_name, na_filter=False)
    df['Last_Updated'] = timestamp

    gc = gspread.service_account(filename=CREDENTIALS_FILE)
    workbook = gc.open_by_url(GSHEET_URL)

    try:
        ws = workbook.worksheet(f'{timestamp}-docs')

    except gspread.exceptions.WorksheetNotFound:
        ws = workbook.add_worksheet(title=f'{timestamp}-docs',
                                         rows=df.shape[0] + 100,
                                         cols=df.shape[1] + 10)  # Creating New Sheet

    ws.clear()  # clear existing data
    ws.update([df.columns.values.tolist()] + df.values.tolist())


if __name__ == '__main__':
    spider = BooksSpider
    timestamp = datetime.datetime.now().strftime('%d-%b-%y')
    csv_name = f'{spider.name}_{timestamp}.csv'
    run_spider(spider)
    # update_gsheet()
    print('Done!')
