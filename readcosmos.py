import telnetlib
import time
import json

wait=0.3

def connect(HOST,PORT):
    return telnetlib.Telnet(HOST,port=PORT)

def runcommand(command, expect):
    """ Wrapper to execute commands on COSMOS data loggers """
    tn = telnetlib.Telnet(HOST,port=PORT)
    tn.write(command)
    #time.sleep(wait)
    out = tn.read_until(expect,timeout=5)
    tn.close()
    return out
     
def checknpm(HOST,PORT):
    return(runcommand('GetNPMTH'))

def getheader(command='showdataheader\r\n',expect="N1RH,"):
    return runcommand(command, expect).strip()

def getversion(command='showversion\r\n',expect='No Telem'):
    return runcommand( command, expect).strip()

def getdata():
    command = 'rdata\r\n'
    return runcommand(command, expect='\r\n').strip().split(',')


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print "%s <hostname> <port>" % (sys.argv[0])
    HOST=sys.argv[1]
    PORT=sys.argv[2]
    #print getheader()
    time.sleep(0.5)
    header = "RecordNum,Time (UTC),P_mb, T1_degC,RH1,Vbat,N1C,N1ET(s),N1T(C),N1RH".split(',')
    data = [item.lstrip().rstrip() for item in getdata()]
    print json.dumps(dict(zip(header,data)),indent=2)
   

