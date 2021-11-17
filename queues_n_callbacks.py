import asyncio
import time
from asyncio import Queue, wait_for, create_task, shield
from random import randint, random

class A:
	def __init__(self):
		self.tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		self.results = {}

	async def launchstuff(self):
		self.getq = Queue() #Can only start qeueue within asyncio context, can't access it outside
		self.results['test start'] = time.time()
		try:
			print("starting waiter")
			task = create_task(wait_for(self.wait_count(),20), name="outer_task")
			task.add_done_callback(self.cleanup_test)
		except asyncio.TimeoutError as e:
			print("outer loop timeout!")
		
		print("going through tasks")
		for i in self.tasks:
			print("putting task in")
			await asyncio.sleep(randint(0,1))
			print(f"putting {i} in")
			await self.getq.put(i)
		await task
		
						

	async def wait_count(self):
		while 1:
			print("we're waiting")
			try:
				print(f'queue length before get is {self.getq.qsize()}')
				await asyncio.sleep(0.5)
				result = await wait_for(self.getq.get(), 10)
				print(f'queue length after get is {self.getq.qsize()}')
				print(f'number popped is {result}')

			except asyncio.TimeoutError as e:
				print("timed out inner loop!")
				return
			except Exception as e:
				print(f"error occured {e}")
	
	def cleanup_test(self, task):
		print(task)
		print(task._exception)
		self.results['test end'] = time.time()
		self.results['total time'] = (self.results.get('test end') - self.results.get('test start'))

if __name__ == "__main__":
	a = A()
	asyncio.run(a.launchstuff())
	print(a.results)
