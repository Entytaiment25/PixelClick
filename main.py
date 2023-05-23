import math
import time

import keyboard
import win32api
import win32con
import win32gui


def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    return title if title else ""


def get_pixel_color(x, y):
    dc = win32gui.GetDC(0)
    color = win32gui.GetPixel(dc, x, y)
    r = color & 0xFF
    g = (color >> 8) & 0xFF
    b = (color >> 16) & 0xFF
    win32gui.ReleaseDC(0, dc)
    return r, g, b


def color_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)


def shoot():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.02)  # Adjust the delay between shots as needed
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def main():
    exit_flag = False

    def on_key_press(event):
        nonlocal exit_flag
        if event.name == "+":
            exit_flag = True

    keyboard.on_press(on_key_press)  # Register the key press event handler

    while not exit_flag:
        if win32api.GetKeyState(win32con.VK_RBUTTON) < 0:
            active_title = get_active_window_title()
            if "FiveM" in active_title:
                while win32api.GetKeyState(win32con.VK_RBUTTON) < 0:
                    color = get_pixel_color(
                        win32api.GetSystemMetrics(0) // 2,
                        win32api.GetSystemMetrics(1) // 2,
                    )
                    if (
                        color_distance(color, (196, 79, 79)) < 205
                    ):  # Adjust the color distance threshold as needed
                        shoot()
                    time.sleep(0.01)  # Adjust the loop delay as needed


if __name__ == "__main__":
    main()
