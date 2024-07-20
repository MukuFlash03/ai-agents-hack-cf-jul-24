import pyautogui
import time
import sys

def cursorPosition():
    # Find current cursor position
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def click_extension_button(button_x, button_y):
    pyautogui.moveTo(button_x, button_y, duration=0.5)
    pyautogui.click()
    print("Clicked the button in the extension popup")

def drag_multion_chat_extension(start_x, start_y, end_x, end_y):
    pyautogui.moveTo(start_x, start_y, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=1)
    time.sleep(0.2)
    pyautogui.mouseUp()
    print("Performed drag operation in the extension popup")

cursor_positions = {
    'brave': {
    "button_maximize": (96, 39),
    "button_autofill_1": (1221, 469),
    "button_autofill_2": (1221, 525),
    "popup_drag_start": (1221, 300),
    "popup_drag_end": (821, 300),
    "simplify_button_cross_onsubmit": (1055, 370),
    "empty_space": (602, 180),
    },
    'chrome': {
        "button_autofill_1": (1228, 418),
        "button_autofill_2": (1234, 477),
        "popup_drag_start": (1215, 355),
        "popup_drag_end": (865, 355),
        "simplify_button_cross_onsubmit": (1026, 379),
        "empty_space": (670, 95),
    }
}

def managePopups():
    # click_extension_button(cursor_positions['brave']['button_maximize'][0], cursor_positions['brave']['button_maximize'][1])
    # time.sleep(1.5)
    drag_multion_chat_extension(cursor_positions['chrome']['popup_drag_start'][0], cursor_positions['chrome']['popup_drag_start'][1], cursor_positions['chrome']['popup_drag_end'][0], cursor_positions['chrome']['popup_drag_end'][1])
    time.sleep(1.5)
    click_extension_button(cursor_positions['chrome']['button_autofill_1'][0], cursor_positions['chrome']['button_autofill_1'][1])
    time.sleep(1.5)
    click_extension_button(cursor_positions['chrome']['button_autofill_2'][0], cursor_positions['chrome']['button_autofill_2'][1])

if __name__ == "__main__":
    cursorPosition()

# Main loop
# try:
#     for key, value in cursor_positions.items():         
#         click_extension_button(value[0], value[1])
#         # Wait for 5 minutes before clicking again
#         time.sleep(5)
#     drag_multion_chat_extension()
# except KeyboardInterrupt:
#     print("Script stopped by user")
     
# click_extension_button(cursor_positions['button_maximize'][0], cursor_positions['button_maximize'][1])
# time.sleep(3)
# drag_multion_chat_extension(cursor_positions['popup_drag_start'][0], cursor_positions['popup_drag_start'][1], cursor_positions['popup_drag_end'][0], cursor_positions['popup_drag_end'][1])
# time.sleep(3)
# click_extension_button(cursor_positions['button_autofill'][0], cursor_positions['button_autofill'][1])
# time.sleep(3)
# click_extension_button(cursor_positions['simplify_button_cross_onsubmit'][0], cursor_positions['simplify_button_cross_onsubmit'][1])
# time.sleep(3)
# click_extension_button(cursor_positions['simplify_button_cross_onsubmit'][0], cursor_positions['simplify_button_cross_onsubmit'][1])