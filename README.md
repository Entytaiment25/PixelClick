# PixelClick
Pixel Detection for the Grand Theft Auto V (FiveM) and Red Dead Redemption 2 (RedM) Crosshair when it turns red, it shoots.

# Requirements
Python 3.11.X (for 3.12.X see FAQ)

# Install
pip install -r requirements.txt

# Keybinds
Press **+** to exit the app. You can change that in the config.toml

# Known Issues
- Not Reshade Compatible (technicolor,...)
- Could have problems with NVE and other Shaders

# FAQ

### I got a package installation error
- try to run cmd.exe with Administrator permisson

### Is the Code harmful?
- No. Its Open Source and you can see the code.

### It isn't working :/
- I will have problems with Reshade -> Technicolor, Technicolor2 Settings open a Issue and provide the #hex or rgb color and I'll add it

## I have Python 3.12.X why isn't it working?
- there seems to be some kind of package error with the 'keyboard' package.
- Do the following to fix it:
```bash
py -m venv NAME

NAME\Scripts\activate

pip install -r requirements.txt

py main.py
```

# This was only made for education.
