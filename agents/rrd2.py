import time
import rrdtool
from agents.getSNMP import consultaSNMP
comunidad = "Redes"

total_input_traffic = 0
total_output_traffic = 0


while 1:
    total_input_traffic = int(
        consultaSNMP(comunidad,'localhost',
                     '1.3.6.1.2.1.4.31.3.1.5.2.3'))
    total_output_traffic = int(
        consultaSNMP(comunidad,'localhost',
                     '1.3.6.1.2.1.4.31.3.1.32.2.3'))

    valor = "N:" + str(total_input_traffic) + ':' + str(total_output_traffic)
    print(valor)
    rrdtool.update('net3.rrd', valor)
    rrdtool.dump('net3.rrd','net3.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)