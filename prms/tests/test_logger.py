import sys
import time
import socket
import unittest
import threading

import bf2mocks

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.host = bf2mocks.host()
        #self.realiylogger = bf2mocks.realitylogger(self.host)
        sys.modules['host'] = self.host
        #sys.modules['host'] = g_host
        #sys.modules['game'] = g_game
        #sys.modules['game'].realitylogger = g_realiylogger

        import ms_logger
        self.ms_logger = ms_logger
    
    def tearDown(self):
        self.ms_logger = None
        sys.modules['host'] = None
    
    def test_can_send_echo(self):
        test_message = 'echo'

        print('')
        print(self.ms_logger.host)
        print(sys.modules['host'])
        print(self.host)
        self.assertTrue(self.ms_logger._debug_echo(test_message))
        self.assertTrue(test_message in self.host._game._state._echo)

    def test_can_send_ingame(self):
        test_message = 'ingame'

        self.ms_logger._debug_ingame(test_message)
        self.assertTrue(test_message in self.host._game._state._chat['server'])


if __name__ == '__main__':
    unittest.main()
