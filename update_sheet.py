from datetime import datetime
import os
import json
import gspread
from google.oauth2.service_account import Credentials

# 讀取 Google Sheets API 憑證
creds_json = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
creds_dict = json.loads(creds_json)

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

# 連線 Google Sheets
gc = gspread.authorize(creds)

# 你的 Google Sheet ID（網址中的 ID）
SHEET_ID = "13APeNnhU8H-SkKCRhqBCG4grxpgR6Lmjg2ajxpeszAk"
worksheet = gc.open_by_key(SHEET_ID).sheet1

# 寫入目前時間到下一行
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
worksheet.append_row([now, "GitHub Actions 自動記錄"])

print(f"已寫入：{now}")
