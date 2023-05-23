RButton::
    WinGetTitle, activeTitle, A
    If (InStr(activeTitle, "FiveM") > 0)
    {
        while (GetKeyState("RButton", "P")) ; While right mouse button is held down
        {
            PixelGetColor, color, % A_ScreenWidth / 2, A_ScreenHeight / 2 ; Get the color of the pixel at the center of the screen
            if (ColorDistance(color, 0xC14F4F) < 205) ; Adjust the color distance threshold as needed
            {
                SendInput, {LButton Down} ; Press and hold left mouse button to shoot
                Sleep 20 ; Adjust the delay between shots as needed
                SendInput, {LButton Up} ; Release left mouse button
            }
            Sleep 10 ; Adjust the loop delay as needed
            
            if (GetKeyState("+", "P")) ; Check if "+" key is pressed
            {
                return ; Exit the RButton hotkey loop
            }
        }
    }
return

ColorDistance(color1, color2) ; Function to calculate color distance
{
    r1 := (color1 & 0xFF0000) >> 16
    g1 := (color1 & 0x00FF00) >> 8
    b1 := color1 & 0x0000FF

    r2 := (color2 & 0xFF0000) >> 16
    g2 := (color2 & 0x00FF00) >> 8
    b2 := color2 & 0x0000FF

    return sqrt((r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2)
}

+::
    ExitApp ; Exit the script if "+" key is pressed
