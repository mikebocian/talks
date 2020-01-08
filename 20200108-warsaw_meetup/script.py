import requests
import time

desired_depth = 7

def deeper(txhash, depth):
    isFraud(txhash)
    print('Going to: ' + txhash + ' at depth: ' + str(depth))
    if depth < desired_depth: 
        r = requests.get("https://api.blockcypher.com/v1/btc/main/txs/" + txhash)
        inputs  = r.json()['inputs']
        for inp in inputs:
            try:
                deeper(inp['prev_hash'], depth+1)
            except:
                return

def isFraud(txhash):
    if txhash == '3d0b134570101fbb1d61370c0c122c219d130ae3760fb072309f6f2b2eeaec7b':
        print('FRAUD!!!!')

    
deeper("f854aebae95150b379cc1187d848d58225f3c4157fe992bcd166f58bd5063449?token=9d56627bbe214a19a82141a0c645768d", 0)
