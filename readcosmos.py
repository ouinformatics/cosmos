import telnetlib
import time
import json

HOST="192.168.88.234"
PORT=2000

tn = telnetlib.Telnet(HOST, port=PORT)

tn.write('showversion\r\n')
tn.read_eager()

tn.write('showheader')
header = tn.read_until('\r\n')
print header


while True:
    tn.write('rdata\r\n')
    record = tn.read_until('\r\n')
    record = [ item.strip() for item in record.split(',') ]
    print json.dumps(record)
    time.sleep(10)


