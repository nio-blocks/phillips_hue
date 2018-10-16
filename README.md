PhillipsHue
===========
This block will control the color of Phillips Hue lights through a hub on the same network, using the Phillips Hue API. The IP address of the hub, and a User ID are required to access the light via the API. Information on how to obtain these values can be found [here.](https://developers.meethue.com/documentation/getting-started)

Example Color Values:
| Color | Hue | Saturation | Brightness |
| ----- | :---: | :---: | :---: |
| Red | 65535 | 254 | 254 |
| Orange | 6500 | 254 | 254 |
| Yellow | 9000 | 254 | 254 |
| Green | 16000 | 254 | 254 |
| Blue | 43000 | 254 | 254 |
| White | 58275 | 254 | 254 |


Properties
----------
- **hub_config**: Configuration for the Hub. IP address of the hub. Your unique user id obtained from the API and the light to control.
  - *hub_ip*: IP Address of the hub.
  - *user_id*: Unique user_id returned from the api.
  - *light_number*: Which light on the hub to contol.
- **kill_switch**: Advanced Property, When selected this will turn off the light when the nio service stops.
- **light_config**: Configuration for the power and color of the light. 
  - *on_state*: integer, Turn the bulb on (1) or off (0).
  - *hue*: integer, The hue value is a wrapping value between 0 and 65535. Both 0 and 65535 are red, 25500 is green and 46920 is blue.
  - *sat*: integer, Saturation of the bulb, with 0 being white and 254 being most color.
  - *bri*: integer, Brightness of the bulb, with 1 being least and 254 being most brightness.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Same list of signals.

Commands
--------
None

Dependencies
------------
requests

