#!/usr/bin/env python
import requests

def _read_from_file(file_path):
	f_hdl = file(file_path,'r')
	value = f_hdl.readline()
	f_hdl.close()
	return value

def _temperature_stats():
	board = float(_read_from_file("/sys/class/hwmon/hwmon0/device/temp1_input"))/1000
	core_0 = float( _read_from_file("/sys/class/hwmon/hwmon0/device/temp2_input"))/1000
	core_1 = float(_read_from_file("/sys/class/hwmon/hwmon0/device/temp3_input"))/1000
	return (board,core_0,core_1)

def _power_stats():
	capacity = float(_read_from_file("/sys/class/power_supply/BAT1/capacity"))
	voltage = float( _read_from_file("/sys/class/power_supply/BAT1/voltage_now"))/10e5
	current = float( _read_from_file("/sys/class/power_supply/BAT1/current_now"))/10e5
	return (capacity,voltage,current)

temp_stats = _temperature_stats()
pows = _power_stats()
payload = {'api_key': 'TAAQHWLOGOP7RLO1','field1': temp_stats[0],'field2': temp_stats[1],'field3': temp_stats[2],'field4': pows[0],'field5': pows[1],'field6': pows[2]}
req = requests.post("http://api.thingspeak.com/update",payload)
print req.text

