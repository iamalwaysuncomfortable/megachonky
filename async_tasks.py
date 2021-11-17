import asyncio
from asyncio import create_task

async def ima_task():
	qnh = create_task(ima_fail_nohandle())
	#error calls immediately after qnh is garbage collected
	return 1

async def ima_fail():
	try:
		print(g)
	finally:
		print("handling exception in a final way that might cleanup resources")

async def ima_fail_nohandle():
	print(g)

def sync_callback(thing):
	print(" ")
	print("I'm a sync callback being called by the event loop")
	print("==================================================")
	try:
		qqq.create_task(ima_fail())
	except: 
		print("qqq exception caught")
	print(f"type of thing passed to callback is {type(thing)}")
	print(f"thing is {thing}")
	print(f"result of things is {thing.result()}")

async def get_future():
	print("I'm a calling function starting")
	print("===============================")
	print("code I'm calling is:")
	print("f = ima_task()")
	print("q = create_task(f)")
	print("q.add_done_callback(sync_callback))")
	f = ima_task()
	ff = ima_fail()
	q = create_task(f)
	qq = create_task(ff)
	q.add_done_callback(sync_callback)
	qq.add_done_callback(sync_callback)

	
	await asyncio.sleep(3)
	print(" ")
	print(" ")
	print("This is my reference to the callback still in the calling function")
	print("==================================================================")
	print(f"q dir is {dir(q)}")
	print(f"q type is {type(q)}")
	print(f"q done is {q.done()}")
	print(f"_state() is {q._state}")
	print(f"exception is {q._exception}")
	
	print(f"qq type is {type(qq)}")
	#print(f"qq exception is {qq._exception}")
	print(f"qq done is {qq.done()}")
	#print(f"qq exception is {qq._exception}")
	#errors don't call until q or qq or garbage collected, so there's a 3 second delay


async def run():
	asyncio.create_task(asyncio.wait_for(get_future(), 12))
	i = 0
	while 1:
		i = i+1
		await asyncio.sleep(2)
		if not i%6:
			asyncio.wait_for(get_future())
		print("keeping event loop going")

asyncio.run(run())
