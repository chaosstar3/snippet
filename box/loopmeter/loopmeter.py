import time
from datetime import datetime, timedelta
import math

def m_pace(value: float):
	m = 1

	if value > 0:
		l = math.floor(math.log10(value))
		if l < 0:
			m = 10 ** (-l)

	return f"{timedelta(seconds=int(m*value))}/{m}"

def m_speed(value: float):
	m = 1
	unit = "s"

	if value < 0.1:
		step = [(60, "m"), (60, "h"), (24, "d")]

		for _m, _unit in step:
			if value >= 0.1:
				break
			value *= _m
			unit = _unit

		if value < 0.1:
			l = round(math.log10(value))
			if l < 0:
				m *= 10 ** (-l)
				value *= 10 ** (-l)

	return f"{value:.2f}/{m if m != 1 else ""}{unit}"

class LoopMeter:
	WIDTH = 100
	def __init__(self, header: str, start: float = None):
		"""
		Args
		- header: display name
		- start: initial time in seconds (e.g., time.time())
		"""
		if start is None:
			start = time.time()
		self.header = header
		self.init = start
		self.start = start

	def start(self):
		self.start = time.time()

	def ing(self, count: int, total: int = None):
		now = time.time()
		if count == 0:
			self.start = now

		elapsed = timedelta(seconds=int(now - self.init))
		taken = now - self.start
		pace = taken / count if count > 0 else 0

		fmt = f"{self.header}: {elapsed}: {count} x {m_pace(pace)}"
		if total is not None:
			ratio = count / total if total > 0 else -1
			remaining = timedelta(seconds=int(pace * (total - count)))
			estimate = datetime.now() + remaining

			fmt += f" | {ratio:.2%} + {remaining} = {estimate.strftime('%H:%M:%S')}"

		print(fmt.ljust(LoopMeter.WIDTH), end="\r")

	def done(self, count: int):
		taken = time.time() - self.start
		speed = count / taken if taken > 0 else 0

		fmt = f"{self.header}: {count} / {timedelta(seconds=int(taken))} = {m_speed(speed)}"
		wait = self.start - self.init
		if wait > 60:
			fmt += f" | +w {timedelta(seconds=int(wait))}"

		print(fmt.ljust(LoopMeter.WIDTH))
