import time
import sys
import datetime
import Adafruit_DHT
import os

#this_dir = os.path.dirname(os.path.realpath(__file__))
#file_path = os.path.join(this_dir, 'log.json')
file_path = '/var/www/html/log.json'

humidity = 0.0
temperature = 0.0
i = 0

while True:
    humidity_momentary, temperature_momentary = Adafruit_DHT.read_retry(11, 21)
    
    try: 
        print ('{0} | Momentary Temp: {1:0.1f} C |  Humidity: {2:0.1f} %'.format(i, temperature_momentary, humidity_momentary))
     
        if i == 0:
            humidity = humidity_momentary
            temperature = temperature_momentary
        elif humidity_momentary < 130:
            humidity = (humidity + humidity_momentary) / 2.0
            temperature = (temperature + temperature_momentary) / 2.0
        else:
            print('READING ERROR!')

        print ('{0} | Avarage   Temp: {1:0.1f} C |  Humidity: {2:0.1f} %'.format(i, temperature, humidity))
        i += 1
        
        if i >= 60:
            date = str(datetime.datetime.now())
            print ('{0} | Momentary Temp: {1:0.1f} C |  Humidity: {2:0.1f} %'.format(date, temperature, humidity))
            with open(file_path, 'a') as outfile:
                outfile.seek(0, os.SEEK_END)
                outfile.seek(outfile.tell() - 1, os.SEEK_SET)
                outfile.truncate()
                outfile.write(',\n' + '["' + date + '", ' + str(temperature) + ', ' + str(humidity) + ']]')
            i = 0

    except:
        print('CATCHED EXCEPTION')
    finally:              
        time.sleep(5)


