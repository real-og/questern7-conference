import gspread_asyncio
from google.oauth2.service_account import Credentials
from loader import SHEET_LINK

link = SHEET_LINK
def get_creds():
    creds = Credentials.from_service_account_file("key.json")
    scoped = creds.with_scopes([
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    return scoped


agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
async def get_sheet(agcm=agcm):
    agc = await agcm.authorize()
    ss = await agc.open_by_url(link)
    zero_ws = await ss.get_worksheet(0)
    return zero_ws

async def append_user(id: str, username: str, team_name):
        sheet = await get_sheet()
        cell = await sheet.find(str(id))
        if cell is None:
            await sheet.append_row([id, username, team_name])
        else:
            await sheet.update_cell(cell.row, 3, team_name)


green = {'red': 0.44, 'green': 1, 'blue': 0.79}
yellow = {'red': 1, 'green': 1, 'blue': 0.67}

async def mark_cell(id, level, value):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    row_number = cell.row
    if value == 'д':
         color = green
    else:
         color = yellow
    # await sheet.update_cell(row_number, level + 3, value)

    range = f'{chr(level + 67)}{row_number}:{chr(level + 67)}{row_number}'
    format = {'backgroundColor': color}

    await sheet.format(range, format)

async def get_ids():
    sheet = await get_sheet()
    res = await sheet.col_values(1) 
    return res

async def update_cell(id, cell_num, value):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, cell_num, str(value))



