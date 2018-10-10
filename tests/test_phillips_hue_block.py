from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..phillips_hue_block import PhillipsHue


class TestPhillipsHue(NIOBlockTestCase):

    def test_process_signals(self):
        blk = PhillipsHue()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {})
