from dataclasses import dataclass, field

def get_rate():
  return 1.2

def send_payment():
  rate = get_rate()
  sample_payment = {"address":"0x123", "memo":"hi", "mcoin": 1, "pcoin": "10000000000000"}
  
  @dataclass
  class Payment:
    address: str
    memo: str
    mcoin: int = 0
    pcoin: int = 0
    coin: field(init = False) = 0

    
    def __post_init__(self):
      self.coin = rate / 1
    
  payment = Payment(**sample_payment)
  print(payment)
 
if __name__ == "__main__":
  send_payment()
