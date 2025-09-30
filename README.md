# 👾 Pwnagotchi: Fallout Vaul Boy Theme

This repository is a fork of [JD-2006/pwnagotchi-fallout-faces-mod](https://github.com/JD-2006/pwnagotchi-fallout-faces-mod/tree/main) with modifications for use on the 2.13in Waveshare e-ink displays.

### Changes and Improvements
- All images resized to 75×75 pixels.  
- Added solid white backgrounds to replace transparency, to properly display on 2.13in Waveshare e-ink displays.   

## ⚙️ Setup Instructions

### 1. Replace Default Faces

Open your Pwnagotchi configuration file:

```bash
sudo nano /etc/pwnagotchi/config.toml
```

Find and **replace the entire block** that looks like this:

```toml
ui.faces.look_r = "( ⚆_⚆)"
ui.faces.look_l = "(☉_☉ )"
ui.faces.look_r_happy = "( ◕‿◕)"
ui.faces.look_l_happy = "(◕‿◕ )"
ui.faces.sleep = "(⇀‿‿↼)"
ui.faces.sleep2 = "(≖‿‿≖)"
ui.faces.awake = "(◕‿‿◕)"
ui.faces.bored = "(-__-)"
ui.faces.intense = "(°▃▃°)"
ui.faces.cool = "(⌐■_■)"
ui.faces.happy = "(•‿‿•)"
ui.faces.excited = "(ᵔ◡◡ᵔ)"
ui.faces.grateful = "(^‿‿^)"
ui.faces.motivated = "(☼‿‿☼)"
ui.faces.demotivated = "(≖__≖)"
ui.faces.smart = "(✜‿‿✜)"
ui.faces.lonely = "(ب__ب)"
ui.faces.sad = "(╥☁╥ )"
ui.faces.angry = "(-_-')"
ui.faces.friend = "(♥‿‿♥)"
ui.faces.broken = "(☓‿‿☓)"
ui.faces.debug = "(#__#)"
ui.faces.upload = "(1__0)"
ui.faces.upload1 = "(1__1)"
ui.faces.upload2 = "(0__1)"
ui.faces.png = false
ui.faces.position_x = 0
ui.faces.position_y = 34
```

**With this version:**

```toml
ui.faces.look_r = "/custom-faces/LOOK_R.png"
ui.faces.look_l = "/custom-faces/LOOK_L.png"
ui.faces.look_r_happy = "/custom-faces/LOOK_R_HAPPY.png"
ui.faces.look_l_happy = "/custom-faces/LOOK_L_HAPPY.png"
ui.faces.sleep = "/custom-faces/SLEEP.png"
ui.faces.sleep2 = "/custom-faces/SLEEP2.png"
ui.faces.awake = "/custom-faces/AWAKE.png"
ui.faces.bored = "/custom-faces/BORED.png"
ui.faces.intense = "/custom-faces/INTENSE.png"
ui.faces.cool = "/custom-faces/COOL.png"
ui.faces.happy = "/custom-faces/HAPPY.png"
ui.faces.excited = "/custom-faces/EXCITED.png"
ui.faces.grateful = "/custom-faces/GRATEFUL.png"
ui.faces.motivated = "/custom-faces/MOTIVATED.png"
ui.faces.demotivated = "/custom-faces/DEMOTIVATED.png"
ui.faces.smart = "/custom-faces/SMART.png"
ui.faces.lonely = "/custom-faces/LONELY.png"
ui.faces.sad = "/custom-faces/SAD.png"
ui.faces.angry = "/custom-faces/ANGRY.png"
ui.faces.friend = "/custom-faces/FRIEND.png"
ui.faces.broken = "/custom-faces/BROKEN.png"
ui.faces.debug = "/custom-faces/DEBUG.png"
ui.faces.upload = "/custom-faces/UPLOAD.png"
ui.faces.upload1 = "/custom-faces/UPLOAD1.png"
ui.faces.upload2 = "/custom-faces/UPLOAD2.png"
ui.faces.png = true
ui.faces.position_x = 2
ui.faces.position_y = 33
```

🚨 Place the `custom-faces` file into the `root` of your Pwnagotchi.
Hint: If you already have a `custom-faces` folder in the `root` directory of your Pwnagotchi, replace it with the `custom-faces` folder from this repo.


### 2. Replace `voice.py` for Fallout Vault Boy Theme's version
These instructions are specifically for jayofelony's Pwnagotchi 2.9.5.3 release. If you are using a different Pwnagotchi release, the directory for your `voice.py` may be different.

🚨 This voice file refers to the Pwnagotchi as the Wanderer Companion and causes it to display messages themed to make the user feel like it is a gadget straight out of the Fallout: New Vegas video game. (The word "handshake" has been replaced with "stimpack") 

Download the `voice.py` file from this repo and move it to your desktop.

Open a terminal on your computer. Then, copy the new `voice.py` from your computer to your Pwnagotchi:

```Bash
scp ~/Desktop/voice.py pi@10.0.0.2:/home/pi/
```

SSH into your Pwnagotchi:

```Bash
ssh pi@10.0.0.2
```

Move the new `voice.py` into the proper directory:

```Bash
sudo mv /home/pi/voice.py /home/pi/.pwn/lib/python3.11/site-packages/pwnagotchi/voice.py
```

Restart Pwnagotchi to apply changes:

```Bash
sudo systemctl restart pwnagotchi
```

## Attribution
Original Fallout Vault Boy faces by JD-2006, from [pwnagotchi-fallout-faces-mod](https://github.com/JD-2006/pwnagotchi-fallout-faces-mod). This fork applies modifications for display optimization only.
