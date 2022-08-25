# Scrapy to Google Sheets

## What does it do

Sends scrapy output to Google Sheet

## How to run
### Authentication

#### Enable API Access

1. Head to Google Developers Console and create a new project (or select the one you already have).
2. In the box labeled `Search for APIs and Services` search for `Google Drive API` and enable it.
3. In the box labeled `Search for APIs and Services`, search for `Google Sheets API` and enable it.

[Source](https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project)

#### Create Service Account
1. Enable API Access for a Project if you haven’t done it yet.
2. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
3. Fill out the form
4. Click “Create” and “Done”.
5. Press “Manage service accounts” above Service Accounts.
6. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new key”.
7. Select JSON key type and press “Create”.
8. Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google account. If you don’t do this, you’ll get a gspread.exceptions.SpreadsheetNotFound exception when trying to access this spreadsheet from your application or a script.
9. Move the downloaded file to `~/.config/gspread/service_account.json`. Windows users should put this file to `%APPDATA%\gspread\service_account.json`.
### The basics

- Install Python3
- Install the dependencies
```
pip install -r requirements.txt
```

### Key libraries
- Scrapy for scanning
- Pandas for massaging raw data
- Gspread for updating Google sheet

### Additional Configuration

- Create a Google API service account
- Share the sheet with this service account 
- set the following in `main.py` file
- 
```python
WORKSHEET_NAME = 'results'
GSHEET_URL = 'https://docs.google.com/spreadsheets/d/...'
CREDENTIALS_FILE = "xyz.json"
```

### cron settings

Set up crontab to run every Monday at 10 a.m. by using these lines:

```shell
0 10 * * mon sh /path/to/runner.sh
```