from nio.block.base import Block, Signal
from nio.properties import VersionProperty, StringProperty, IntProperty, \
                           ObjectProperty, PropertyHolder

import requests


class HubConfig(PropertyHolder):

    hub_ip = StringProperty(title='Hub IP Address', default='[[IP]]')
    user_id = StringProperty(title='User ID', default='[[ID]]')
    light_number = IntProperty(title='Light Number', default=2)


class LightConfig(PropertyHolder):

    on_state = IntProperty(title='1 for on 0 for off', default=0)
    hue = IntProperty(title='Hue (0-65535)', default=0)
    sat = IntProperty(title='Saturation (0-254)', default=0)
    bri = IntProperty(title='Brightness (1-254)', default=1)


class PhillipsHue(Block):

    version = VersionProperty('0.1.0')
    hub_config = ObjectProperty(
        HubConfig, title='Hub Configuration', default=HubConfig())
    light_config = ObjectProperty(
        LightConfig, title='Light Configuration', default=LightConfig())

    def process_signals(self, signals):
        for signal in signals:
            self.data = {}
            self.api_url = 'http://{0}/api/{1}/lights/{2}/state'.format(
                        self.hub_config().hub_ip(signal),
                        self.hub_config().user_id(signal),
                        self.hub_config().light_number(signal))
            if self.light_config().on_state(signal) == 1:
                self.data["on"] = True
                self.data["hue"] = self.light_config().hue(signal)
                self.data["sat"] = self.light_config().sat(signal)
                self.data["bri"] = self.light_config().bri(signal)
            else:
                self.data["on"] = False
            x = requests.put(self.api_url, json=self.data)
            self.logger.debug(x.text)
            self.logger.debug(self.data)

        self.notify_signals(signals)

    def stop(self):
        self.api_url = 'http://{0}/api/{1}/lights/{2}/state'.format(
                    self.hub_config().hub_ip(),
                    self.hub_config().user_id(),
                    self.hub_config().light_number())
        self.data["on"] = False
        x = requests.put(self.api_url, json=self.data)
        self.logger.debug(x.text)
        super().stop()
