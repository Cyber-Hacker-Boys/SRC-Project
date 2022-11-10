import socket

from django.http import HttpResponseRedirect
from django.shortcuts import render
from getmac import get_mac_address as gma
from scapy.all import *
from scapy.layers.inet import IP, ICMP
from scapy.layers.inet import TCP, UDP


# Create your views here.

def index(request):
    if request.method == 'GET':
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        local_mac = gma()
        return render(request, 'ipApp/index.html', {'clientIP': local_ip, 'clientMac': local_mac})


def sendT(request):
    if request.method == "POST":

        version = 4
        ihl = int(request.POST['ihlT'])
        tos = int(request.POST['tosT'])
        lenT = int(request.POST['lenT'])
        ident = int(request.POST['identT'])
        flags = request.POST['flagsT']

        if flags == '0':
            flags = 0

        fragment = int(request.POST['fragmentT'])
        ttl = int(request.POST['ttlT'])
        protocol = int(request.POST['protocolsT'])
        check = int(request.POST['headerCT'])
        srcIP = request.POST['srcIPT']
        destIP = request.POST['destIPT']
        opt = request.POST['optIPT']

        srcPort = int(request.POST['srcPort'])
        destPort = int(request.POST['destPort'])
        seqNum = int(request.POST['seqNum'])
        ackNum = int(request.POST['ackNum'])
        dOff = int(request.POST['dOff'])
        rBits = int(request.POST['rBits'])
        cFlags = request.POST['cFlags']
        winSize = int(request.POST['winSize'])
        checkST = int(request.POST['checkST'])
        uPont = int(request.POST['uPont'])
        dataT = request.POST['optionsTCP']

        dataTT = request.POST['dataTC']

        dataTS = dataT.split(",")
        dataTS.pop()
        dataO = []
        for i in dataTS:
            if i == "1":
                dataO.append(('NOP', ''))
            elif i == "2":
                dataO.append(('MSS', 4))
            elif i == "3":
                dataO.append(('SAckOK', ''))
            elif i == "4":
                dataO.append(('Timestamp', (1098453, 0)))

        ip = IP(version=version, ihl=ihl, tos=tos, len=lenT, id=ident, flags=flags, frag=fragment, ttl=ttl,
                proto=protocol,
                chksum=check, src=srcIP, dst=destIP, options=opt)

        tcp = TCP(sport=srcPort, dport=destPort, seq=seqNum, ack=ackNum, dataofs=dOff, reserved=rBits, flags=cFlags,
                  window=winSize, chksum=checkST, urgptr=uPont, options=dataO)

        send(ip / tcp / Raw(dataTT))

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def sendU(request):
    if request.method == "POST":

        dMac = request.POST['ethDesU']
        eMac = request.POST['ethSrcU']
        typeT = 0x800

        version = 4
        ihl = int(request.POST['ihlU'])
        tos = int(request.POST['tosU'])
        lenI = int(request.POST['lenUI'])
        ident = int(request.POST['identU'])
        flags = request.POST['flagsU']

        if flags == '0':
            flags = 0

        fragment = int(request.POST['fragmentU'])
        ttl = int(request.POST['ttlU'])
        protocol = int(request.POST['protocolsU'])
        check = int(request.POST['headerCU'])
        srcIP = request.POST['srcIPU']
        destIP = request.POST['destIPU']
        opt = request.POST['optIPU']

        srcPort = int(request.POST['srcPortU'])
        destPort = int(request.POST['destPortU'])
        lenU = int(request.POST['lenU'])
        checkSU = int(request.POST['checkSU'])

        dataUD = request.POST['dataU']

        ip = IP(version=version, ihl=ihl, tos=tos, len=lenI, id=ident, flags=flags, frag=fragment, ttl=ttl,
                proto=protocol,
                chksum=check, src=srcIP, dst=destIP, options=opt)

        udp = UDP(sport=srcPort, dport=destPort, len=lenU, chksum=checkSU)

        send(ip / udp / Raw(dataUD))

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def sendI(request):
    if request.method == "POST":

        version = 4
        ihl = int(request.POST['ihlI'])
        tos = int(request.POST['tosI'])
        lenI = int(request.POST['lenII'])
        ident = int(request.POST['identI'])
        flags = request.POST['flagsI']

        if flags == '0':
            flags = 0

        fragment = int(request.POST['fragmentI'])
        ttl = int(request.POST['ttlI'])
        protocol = int(request.POST['protocolsI'])
        check = int(request.POST['headerCI'])
        srcIP = request.POST['srcIPI']
        destIP = request.POST['destIPI']
        opt = request.POST['optIPI']

        typeI = int(request.POST['typeI'])
        codeI = int(request.POST['codeI'])
        checkI = int(request.POST['checkS'])

        dataIC = request.POST['dataAI']

        ip = IP(version=version, ihl=ihl, tos=tos, len=lenI, id=ident, flags=flags, frag=fragment, ttl=ttl,
                proto=protocol,
                chksum=check, src=srcIP, dst=destIP, options=opt)

        icmp = ICMP(type=typeI, code=codeI, chksum=checkI)

        send(ip / icmp / Raw(dataIC))

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


def ICMP_sweep(request):
    if request.method == "POST":
        startIPScan = request.POST['startIPScan']
        endIPScan = request.POST['endIPScan']
        # thr = threading.Thread(target=icmpSweep, args=(startIPScan, endIPScan), daemon=True)
        # thr.start()
        scanData = icmpSweep(startIPScan, endIPScan)

        return render(request, 'ipApp/report.html', {'scanD': scanData[:-1], 'result': scanData[-1]})
    else:
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


# -----ICMPsweeper----
def iprange(ip1, ip2):
    ip1_1 = ip1.split(".")
    ip2_2 = ip2.split(".")
    iparr = []
    for i in range(0, len(ip1_1)):
        ip1_1[i] = int(ip1_1[i])

    for i in range(0, len(ip2_2)):
        ip2_2[i] = int(ip2_2[i])

    for i in range(ip1_1[0], ip2_2[0] + 1):
        for j in range(ip1_1[1], ip2_2[1] + 1):
            for k in range(ip1_1[2], ip2_2[2] + 1):
                for z in range(ip1_1[3], ip2_2[3] + 1):
                    temp = str(i) + '.' + str(j) + '.' + str(k) + '.' + str(z)
                    iparr.append(temp)
    return iparr


#########################################################
# ICMPsweeper remake with multithreading (Fast AF)      #
#                                                       #
# This might be a bit overkill, and the implementation  #
# might not get you the most accurate results in some   #
# cases. But it sure is fast as hell (and I was bored)  #
# Also, you can use this to implement other things      #
# like a port scanner, or anything that would benefit   #
# from multithreading.                                  #
#                                                       #  
# - JoaoAJMatos (https://github.com/JoaoAJMatos)        #
#########################################################

from threading import Thread, RLock as rLock

import time

try:
    from queue import Queue, Empty
except:
    from Queue import Queue, Empty

# We need to set a limit to the number of threads in the pool since scapy needs to be able to acces /dev/bpf to capture
# network traffic. If we spawn too many threads, we will run out of file descriptors and the program will crash.
# Idk for sure what the limit is, but tried it with 200 threads, and it didn't work.
MAX_THREADS = 100
DEFAULT_TIMEOUT = 0.1  # The default timeout for the ICMP requests


class Worker(Thread):
    def __init__(self, task_queue, thread_name, polling_timeout):
        super(Worker, self).__init__(name=thread_name)
        self.__task_queue = task_queue
        self.__terminated = False
        self.__thread_name = thread_name
        self.__polling_timeout = polling_timeout

    def run(self):
        while not self.__terminated:
            # locking implemented by the Queue class
            # blocks until a task is queued
            task = None
            try:
                task = self.__task_queue.get()
            except Empty:
                pass

            if task is not None:
                if isinstance(task, AbstractRunnable):
                    try:
                        task.execute()
                    except BaseException as ex:
                        print("Caught exception while executing task : %s: %s" % (ex.__class__.__name__, ex))

                    # notify the queue that the task is done
                    self.__task_queue.task_done()
                else:
                    print("Invalid object enqueued to task list.")

    def terminate(self):
        self.__terminated = True


# The ThreadPool class offers a simple Thread pool implementation for Python. It uses Python's Queues to coordinate
# tasks among a set of worker threads.
class ThreadPool(object):
    def __init__(self, size, name, daemon=False, polling_timeout=60):
        if size < 1:
            raise ValueError("Thread pool size should be higher 0")

        if polling_timeout < 1:
            raise ValueError("Polling timeout should be higher 0")

        self.__task_queue = Queue()
        self.__pool_size = size
        self.__pool_name = name
        self.__worker_threads = []
        self.__polling_timeout = polling_timeout
        self.__daemon = daemon

        self._create_worker_threads()

    # Adds the specified task to the task queue for a worker thread to start working on it. If any free worker
    # threads are waiting on the task queue, it will immediately pick up this task.
    def enqueue(self, task):
        if not isinstance(task, AbstractRunnable):
            raise ValueError("The task must be of AbstractRunnable or a subclass of it.")

        self.__task_queue.put(task)

    # Creates a new job object and adds it to the queue
    def add_task(self, function, *args):
        task = Job(function, *args)
        self.enqueue(task)

    def get_pool_size(self):
        with rLock():
            return self.__pool_size

    # Stop the worker threads
    # If the force flag is set, the worker threads will stop regardless of whether there are tasks left in the queue.
    # If it's not set, the threads will join the main thread.
    def stop(self, force=False):
        with rLock():
            if not force:
                self.__task_queue.join()

            for worker_thread in self.__worker_threads:
                worker_thread.terminate()

    def _create_worker_threads(self):
        with rLock():
            while len(self.__worker_threads) < self.__pool_size:
                thread_name = "%s-%s" % (self.__pool_name, (len(self.__worker_threads) + 1))
                worker_thread = Worker(self.__task_queue, thread_name, self.__polling_timeout)
                worker_thread.daemon = self.__daemon
                worker_thread.start()
                self.__worker_threads.append(worker_thread)


class AbstractRunnable(object):
    def __init__(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError


class Job(AbstractRunnable):
    def execute(self):
        self.function(*self.args, **self.kwargs)

    def __init__(self, function, *args, **kwargs):
        if not hasattr(function, '__call__'):
            raise ValueError("The task is not a valid function")

        self.function = function
        self.args = args
        self.kwargs = kwargs


# Wrapper function for sending ICMP packets
# Returns the response and the time it took to send the packet
def ping(ip, timeout=0.5):
    start = time.process_time()
    res = sr1(IP(dst=str(ip)) / ICMP(), timeout=timeout, verbose=1)
    return res, time.process_time() - start


# This function will be called in a separate thread for each IP in the range
def is_alive(ip, timeout, output_array, output_live_ips):
    resp = sr1(IP(dst=str(ip)) / ICMP(), timeout=timeout, verbose=0)

    # If we ommit the logging and the appending of blocking or down IPs, we can get the scanner to run
    # faster. On my machine, with a range of 255 IPs, the scan is half a second faster without the logging.
    if resp is not None and int(resp.getlayer(ICMP).type) == 0:
        print(f"{ip} is alive.")
        output_array.append(ip + " is alive.")
        output_live_ips.append(ip)


# The main function for the ICMP sweep
def icmpSweep(startIPScan, endIPScan):
    iparr = iprange(startIPScan, endIPScan)
    thread_count = MAX_THREADS
    alive_ips = []  # List of alive IPs
    output_array = []  # List of output strings

    # There's no need to spawn that many threads if the range is smaller than MAX_THREADS
    if len(iparr) < MAX_THREADS:
        thread_count = len(iparr)

    tp = ThreadPool(thread_count, "ICMP_Sweep", True, 1)  # True: Deamon threads, 1: Polling timeout
    start = time.process_time()  # Just to get the execution time

    # Start pushing jobs to the queue
    for ip in iparr:
        tp.add_task(is_alive, ip, DEFAULT_TIMEOUT, output_array, alive_ips)

    tp.stop()  # Stop the threads

    print("Elapsed time: %s" % (time.process_time() - start))
    print(f"{len(alive_ips)}/{len(iparr)} hosts are online.")

    output_array.append(str(len(alive_ips)) + "/" + str(len(iparr)) + "hosts are online.")

    return output_array
# -----ICMPsweeper----
