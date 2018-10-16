from unittest.mock import patch, ANY
from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..phillips_hue_block import PhillipsHue


class TestPhillipsHue(NIOBlockTestCase):

    def test_on(self):
        with patch(PhillipsHue.__module__ + '.requests') as mock_requests:
            blk = PhillipsHue()
            self.configure_block(blk,
                                 {'hub_config': {
                                      'hub_ip': '12.12.12.12',
                                      'user_id': '1232123ABCQ',
                                      'light_number': 5},
                                  'light_config': {
                                      'on_state': 1,
                                      'hue': 3000,
                                      'sat': 200,
                                      'bri': 100}
                                  })
            blk.start()
            blk.process_signals([Signal({})])
            self.assert_num_signals_notified(1)
            mock_requests.put.assert_called_with(
                'http://12.12.12.12/api/1232123ABCQ/lights/5/state',
                json={'on': True,
                      'hue': 3000,
                      'sat': 200,
                      'bri': 100})
            blk.stop()
