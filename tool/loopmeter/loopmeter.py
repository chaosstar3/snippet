class LoopMeter:
	WIDTH = 80
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

	def ing(self, count: int, total: int = None):
		now = time.time()
		if count == 0:
			self.start = now

		elapsed = timedelta(seconds=int(now - self.init))
		taken = now - self.start
		pace = taken / count if count > 0 else 0
		multiple = _calc_multiple(pace)

		fmt = f"{self.header}: {elapsed}: {count} x {pace*multiple:.2f}/{multiple}"
		if total is not None:
			ratio = count / total if total > 0 else -1
			remaining = timedelta(seconds=int(pace * (total - count)))
			estimate = datetime.now() + remaining
			fmt += f" | {ratio:/.2%} + {remaining} = {estimate}"

		print(fmt.ljust(Meter.WIDTH), end="\r")

	def done(self, count: int):
		taken = time.time() - self.start
		speed = count / taken if taken > 0 else 0
		multiple = _calc_multiple(speed)

		fmt = f"{self.header}: {count} / {timedelta(seconds=int(taken))} = {speed*multiple:.2f}/{multiple}"
		wait = self.start - self.init
		if wait > 60:
			fmt += f" | +w {timedelta(seconds=int(wait))}"

		print(fmt.ljust(Meter.WIDTH))
