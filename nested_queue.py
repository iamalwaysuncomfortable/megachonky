import asyncio
from random import randint
from asyncio import Queue


class G:
    async def auxincli_output_iter(self):
        while 1:
            result = await self.q.get()
            asyncio.sleep(1)
            yield result

    async def handle(self):
        async for m in self.auxincli_output_iter():
            if not (m % 3):
                print("Putting new message in queue")
                await self.messages.put(m)
            else:
                print("do other async stuff")

    async def read_messages(self):
        while 1:
            message = await self.messages.get()
            print(f"message is {message}")

    async def mimicstuff(self):
        self.q = Queue()
        for i in range(60):
            await self.q.put(i)
        print("populated Queue")
        self.messages = Queue()
        i = 0
        asyncio.create_task(self.handle())
        asyncio.create_task(self.read_messages())
        while i < 25:
            ri = randint(1, 6)
            await asyncio.sleep(0.3)
            if not ri % 3:
                print("Putting new numbers in queue")
                ri2 = randint(1, 6)
                await self.q.put(ri2)
                i = i + 1


if __name__ == "__main__":
    g = G()
    print("running async")
    asyncio.run(g.mimicstuff())
