import gspread
from oauth2client.service_account import ServiceAccountCredentials

def create_and_populate_sheet(emails):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    creds_json = 'instagram-clone-e619a-c47e29a43538.json'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
    gc = gspread.authorize(credentials)

    sh = gc.create('Emails Spreadsheet')

    sh.share(None, perm_type='anyone', role='writer', with_link=True)

    worksheet = sh.get_worksheet(0)

    cell_list = worksheet.range('A1:A{}'.format(len(emails)))

    for i, cell in enumerate(cell_list):
        cell.value = emails[i]

    worksheet.update_cells(cell_list)

    return sh.url

emails = ['email1@example.com', 'email2@example.com', 'infect3dlab@gmail.com', 'email4@example.com', 'email5@example.com', 'email6@example.com']
spreadsheet_url = create_and_populate_sheet(emails)
print(f'New spreadsheet created and is publicly accessible: {spreadsheet_url}')
