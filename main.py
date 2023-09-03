import math
import os
import threading
import time

import keyboard
import pystray
import win32api
import win32con
import win32console
import win32gui
from PIL import Image, ImageDraw

import config

pxl_exit = os._exit


class ColorUtils:
    @staticmethod
    def get_pixel_color(x, y):
        dc = win32gui.GetDC(0)
        color = win32gui.GetPixel(dc, x, y)
        r = color & 0xFF
        g = (color >> 8) & 0xFF
        b = (color >> 16) & 0xFF
        win32gui.ReleaseDC(0, dc)
        return r, g, b

    @staticmethod
    def color_distance(color1, color2):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        return math.sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)


class TrayIcon:
    def __init__(self, name, title, menu):
        self.icon = pystray.Icon(name, self.create_image(), title, menu)

    def create_image(self):
        width = 64
        height = 64
        color1 = "black"
        color2 = "white"
        image = Image.new("RGB", (width, height), color1)
        dc = ImageDraw.Draw(image)
        dc.rectangle([(width // 2, 0), (width, height)], fill=color2)
        return image

    def run(self):
        self.icon.run()


class PixelClick:
    def __init__(self):
        self.exit_flag = False

    def get_active_window_title(self):
        window = win32gui.GetForegroundWindow()
        title = win32gui.GetWindowText(window)
        return title if title else ""

    def shoot(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    def on_key_press(self, event):
        if event.name == config.EXIT_KEY:
            self.exit_flag = True
            pxl_exit(0)

    def run(self):
        keyboard.on_press(self.on_key_press)
        while not self.exit_flag:
            active_title = self.get_active_window_title()
            if "FiveM" or "RedM" in active_title:
                if win32api.GetKeyState(win32con.VK_RBUTTON) < 0:
                    while win32api.GetKeyState(win32con.VK_RBUTTON) < 0:
                        color = ColorUtils.get_pixel_color(
                            win32api.GetSystemMetrics(0) // 2,
                            win32api.GetSystemMetrics(1) // 2,
                        )
                        if "FiveM" in active_title:
                            if ColorUtils.color_distance(color, (196, 79, 79)) < 205:
                                self.shoot()
                        elif (
                            "RedM" in active_title
                        ):  ## White: 225, 225, 225, Gray: 123, 123, 123, Red: 242, 16, 45, Dark Red: 140, 0, 0
                            if (
                                ColorUtils.color_distance(color, (242, 16, 45)) < 20
                                or ColorUtils.color_distance(color, (140, 0, 0)) < 20
                            ):
                                self.shoot()
                        time.sleep(0.03)
            else:
                time.sleep(1)


def exit_action(icon):
    icon.stop()
    pxl_exit(0)


def main():
    try:
        win32console.SetConsoleTitle("PixelClick")
        win32gui.ShowWindow(win32console.GetConsoleWindow(), win32con.SW_HIDE)
        print("PixelClick is running...")

        menu = (
            pystray.MenuItem("Exit", exit_action),
        )
        tray_icon = TrayIcon("PixelClick", "PixelClick", menu)
        icon_thread = threading.Thread(target=tray_icon.run)
        icon_thread.start()

        pixel_click = PixelClick()
        pixel_click.run()

    except KeyboardInterrupt:
        PixelClick.exit_flag = True
        pxl_exit(0)

    except Exception as e:
        print(e)
        PixelClick.exit_flag = True
        pxl_exit(0)


if __name__ == "__main__":
    try:
        main()
        try:
            input("Press Enter to exit...")
            pxl_exit(0)
        except EOFError:
            pxl_exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
