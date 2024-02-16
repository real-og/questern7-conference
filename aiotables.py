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


async def get_ids():
    sheet = await get_sheet()
    res = await sheet.col_values(1) 
    return res


async def get_all_scores():
    sheet = await get_sheet()
    column_values = await sheet.col_values(8)
    team_names = await sheet.col_values(1)
    return team_names[1:7], column_values[1:7]


async def get_score(name):
    sheet = await get_sheet()
    if name in ['1', '2', '3', '4', '5', '6']:
        row_number = int(name) + 1
    else:
        cell = await sheet.find(name)
        if cell is None:
            return None, None
        row_number = cell.row
    rooms_names = await sheet.row_values(1)
    values_in_row = await sheet.row_values(row_number)
    return values_in_row, rooms_names[1:8]

async def update_cell(id, cell_num, value):
    sheet = await get_sheet()
    cell = await sheet.find(str(id))
    if cell is None:
        return
    row_number = cell.row
    await sheet.update_cell(row_number, cell_num, str(value))



