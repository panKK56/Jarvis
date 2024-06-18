from pyHS100 import SmartBulb

def turn_on_bulb():
    ip_address="ip_address"
    bulb = SmartBulb(ip_address)
    bulb.turn_on()
    print(f"Bulb at {ip_address} turned ON.")

def turn_off_bulb():
    ip_address="ip_address"
    bulb = SmartBulb(ip_address)
    bulb.turn_off()
    print(f"Bulb at {ip_address} turned OFF.")




