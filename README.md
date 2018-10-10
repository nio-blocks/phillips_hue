PhillipsHue
===========
This block will control the color of Phillips Hue lights through a hub on the same network, using the Phillips Hue API.

Properties
----------
- **bri**: Brightness of the bulb.
- **hub_ip**: IP Address of the Hub, must be on the same network.
- **hue**: The hue value is a wrapping value between 0 and 65535. Both 0 and 65535 are red, 25500 is green and 46920 is blue.
- **light_number**: Which light connected to the hub to control.
- **on_state**: Turn the bulb on or off.
- **sat**: Saturation of the bulb, with 0 being white and 254 being most color.
- **user_id**: The user id assigned by the hub.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: 

Dependencies
------------
requests

Commands
--------
None

