def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connessione al server DHCP in corso...')
        wlan.connect('nomeSSID', 'pwdSSID')
        while not wlan.isconnected():
            pass
    print('Configurazione ottenuta dal derver DHCP:', wlan.ifconfig())
if __name__ == '__main__':
    do_connect()
    import temp_rH
    