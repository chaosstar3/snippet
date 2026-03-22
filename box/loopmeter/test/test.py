#helper.py
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import unittest

import time
from loopmeter import LoopMeter, m_pace, m_speed

class TestLoopMeter(unittest.TestCase):
	def test_multiple(self):
		self.assertEqual(m_pace(1), "0:00:01/1")
		self.assertEqual(m_pace(42), "0:00:42/1")
		self.assertEqual(m_pace(1000), "0:16:40/1")
		self.assertEqual(m_pace(0.9), "0:00:09/10")
		self.assertEqual(m_pace(0.1), "0:00:01/10")
		self.assertEqual(m_pace(0.001), "0:00:01/1000")

		# second format
		self.assertEqual(m_speed(1), "1.00/s")
		self.assertEqual(m_speed(4), "4.00/s")
		self.assertEqual(m_speed(0.01), "0.60/m")
		self.assertEqual(m_speed(3/86400), "0.12/h")
		self.assertEqual(m_speed(3/10/86400), "0.30/d")
		self.assertEqual(m_speed(3/1000/86400), "3.00/1000d")

def test():
	meter = LoopMeter("Test")
	for i in range(10):
		time.sleep(1)
		meter.ing(i*i*1000, 100000)
	print("")
	meter.done(3)

if __name__ == "__main__":
	unittest.main()
	#test()
