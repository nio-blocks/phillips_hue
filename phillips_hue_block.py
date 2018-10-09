from nio.block.base import Block, Signal
from nio.properties import VersionProperty, StringProperty, IntProperty, BoolProperty

import requests


class PhillipsHue(Block):

    version = VersionProperty('0.1.0')
    hub_ip = StringProperty(title='Hub IP Address', default='[[IP]]')
    user_id = StringProperty(title='User ID', default='[[ID]]')
    light_number = IntProperty(title='Light Number', default=2)
    on_state = IntProperty(title='1 for on 0 for off', default=0)
    
    def process_signals(self, signals):
        for signal in signals:
            self.api_url = 'http://{0}/api/{1}/lights/{2}/state'.format(
            	        self.hub_ip(signal),
            	        self.user_id(signal),
            	        self.light_number(signal))
            if self.on_state(signal) == 1:
            	self.data = '{"on":true}'
            else:
                self.data = '{"on":false}'
            x = requests.put(self.api_url, self.data)
            print(x.text)
            
        self.notify_signals(signals)
