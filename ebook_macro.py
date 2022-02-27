import pyautogui
import pyperclip
import win32gui
import time


def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))


def bring_top_window(window_name):
    retsult = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)

    for i in top_windows:
        if window_name.lower() in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            break


start_page = 1
end_page = int(520)


bring_top_window('SM-P200')
time.sleep(1.)

for page in range(start_page, end_page + 1):

    pyperclip.copy(str(page).zfill(10))

    pyautogui.click(800, 98) # 캡처하기 버튼 위치
    time.sleep(.5)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(.5)

    pyautogui.press('enter')
    time.sleep(0.5)

    pyautogui.click(1208, 827)  # 다음페이지 누르기 위치
    time.sleep(1.0)
