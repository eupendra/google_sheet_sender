# Scrapy to Google Sheets
<!-- TOC -->
* [What does it do](#what-does-it-do)
* [How to run](#how-to-run)
  * [Authentication](#authentication)
    * [Enable API access](#enable-api-access)
    * [Create a service account](#create-a-service-account)
  * [The basics](#the-basics)
  * [Key libraries](#key-libraries)
  * [Additional configuration](#additional-configuration)
  * [cron settings](#cron-settings)
<!-- TOC -->
## What does it do

Sends scrapy output to Google Sheet

## How to run

### Authentication

#### Enable API access

1. Head to [Google Developers Console](https://console.cloud.google.com/) and create a new project (or select the one
   you already have).
2. In the box labeled `Search for APIs and Services` search for `Google Drive API` and enable it.
3. In the box labeled `Search for APIs and Services`, search for `Google Sheets API` and enable it.

*[Gspread Documentation](https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project)*

#### Create a service account

1. Enable API Access for a Project if you haven’t done it yet.
2. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
3. Fill out the form
4. Click “Create” and “Done”.
5. Press “Manage service accounts” above Service Accounts.
6. Press on ⋮ near recently created service account and select “Manage keys” and then click on “ADD KEY > Create new
   key”.
7. Select JSON key type and press “Create”.
8. Go to your spreadsheet and share it with a client_email from the step above. Just like you do with any other Google
   account. If you don’t do this, you’ll get a gspread.exceptions.SpreadsheetNotFound exception when trying to access
   this spreadsheet from your application or a script.
9. Move the downloaded file to `~/.config/gspread/service_account.json`. Windows users should put this file
   to `%APPDATA%\gspread\service_account.json`.

### The basics

- Install Python3
- Install the dependencies

```
pip install -r requirements.txt
```

### Key libraries

- Scrapy for scraping
- Pandas for cleaning up raw data
- Gspread for updating Google sheet

### Additional configuration

Set the following in [main.py](./google_sheet_sender/main.py) file

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