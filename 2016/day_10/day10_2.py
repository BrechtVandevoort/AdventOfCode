import re

class Factory:
	def __init__(self):
		self._bots = {}
		self._outputs = {}
		self._workqueue = []

	def get_bot(self, name):
		return self._bots[name]

	def get_output(self, name):
		return self._outputs[name]

	def register_bot(self, bot):
		self._bots[bot.name()] = bot

	def add_bot_to_workqueue(self, bot):
		self._workqueue.append(bot)

	def is_workqueue_empty(self):
		return len(self._workqueue) == 0

	def execute(self):
		while not self.is_workqueue_empty():
			self.execute_step()

	def execute_step(self):
		if self.is_workqueue_empty():
			return False
		bot = self._workqueue.pop(0)
		return bot.execute()

	def add_chip_to_output(self, chip, output_name):
		if output_name not in self._outputs:
			self._outputs[output_name] = []
		self._outputs[output_name].append(chip)

	def move_chip(self, chip, target):
		if target[:3] == 'bot':
			self._bots[target].give_chip(chip)
		else:
			self.add_chip_to_output(chip, target)

class Bot:
	def __init__(self, factory, name, low_target, high_target):
		self._factory = factory
		self._name = name
		self._low_target = low_target
		self._high_target = high_target
		self._chips = []

	def name(self):
		return self._name

	def give_chip(self, chip):
		self._chips.append(chip)
		if len(self._chips) >= 2:
			self._factory.add_bot_to_workqueue(self)

	def execute(self):
		if len(self._chips) < 2:
			return False
		low, high = sorted(self._chips[:2])
		self._chips = self._chips[2:]
		#print '%7s moved %2d to %10s and %2d to %10s' % (self._name, low, self._low_target, high, self._high_target)
		self._factory.move_chip(low, self._low_target)
		self._factory.move_chip(high, self._high_target)
		return True

factory = Factory()
for line in sorted(open('input.txt').readlines()):
	assignment_match = re.match('value (\d+) goes to (bot \d+)', line)
	execution_match = re.match('(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)', line)
	if execution_match:
		bot = Bot(factory, *execution_match.groups())
		factory.register_bot(bot)
	else:
		chip, name = assignment_match.groups()
		factory.get_bot(name).give_chip(int(chip))

factory.execute()

values = factory.get_output('output 0') + factory.get_output('output 1') + factory.get_output('output 2')
print reduce(lambda x, y: x*y, values, 1)
