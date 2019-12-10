
# Automitive UI - Dashboard Sensors
## Introduction using a system diagram

![system diagram](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/system_diagram.png)

## Bill of Materials/Budget

<table style="width:100%" >
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Shipping Fee</th>
	<th>Total Cost</th>
	<th>From</th>
  </tr>
  <tr>
    <td>Hall Effect Sensor</td>
    <td>CAD$ 7.99</td>
	<td>CAD$ 4.02</td>
	<td>CAD$ 12.01</td>
    <td>SunFounder</td>
  </tr>
  <tr>
    <td>Raspberry Pi</td>
    <td>CAD$ 153.16</td>
	<td>CAD$ 4.77</td>
	<td>CAD$ 157.93</td>
    <td>CanaKit</td>
  </tr>
  <tr>
    <td>Magnet</td>
    <td>CAD$ 1.50</td>
	<td>CAD$ 0.00</td>
	<td>CAD$ 1.70</td>
    <td>Dollarama</td>
  </tr>

  <tr>
    <td>PCB board</td>
    <td>CAD$ 0.00</td>
	<td>CAD$ 0.00</td>
	<td>CAD$ 0.00</td>
    <td>Prototype Lab</td>
</tr>
<tr>
   <td>Elcosure</td>
    <td>CAD$ 0.00</td>
	<td>CAD$ 0.00</td>
	<td>CAD$ 0.00</td>
    <td>Idea Lab</td>
  </tr>
</table>

<table style="width:100%" >
  <tr>
    <th>Total cost</th>
    <th>CAD$ 171.64</th>
  </tr>
</table>

## Time Commitment

![schedule](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/schedule.PNG)

## Mechanical Assembly

### Make connection

```
network={
	ssid="WiFi Name"
	password="WiFi Password"
	priority=999
	}
```

![ip_addr](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/ip_addr.PNG)

### Design Bread Board circuit

![BB_Design](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/Hall%20Effect%20Sensor_BB.ps.png)

### Check Sensor supply power

![check power voltage](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/Check_Power_Voltage.jpg)

### Design PCB

![pcb design](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/design/Hall%20Effect%20Sensor%20pcb_pcb.jpg)

### Coding

```
import RPi.GPIO as GPIO

HALL = 12

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(HALL, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def change_detected(channel):
	if GPIO.input(HALL) == GPIO.LOW:
		print("Magnetic material detected.")
	else:
		print("No magnetic material.")

GPIO.add_event_detect(HALL, GPIO.BOTH, change_detected, bouncetime=25)

try:
	while True:
		pass

except KeyboardInterrup:
	print("Ctrl-C - quit")

finally:
	GPIO.cleanup()
```

## PCB / Soldering

![pcb](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/pcb.png)


## Power Up and production testing

### Bread Board Power up

![BB_power_up](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/BBwithSensor.jpg)

### PCB Power up

![PCB_power_up](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/power_on_pcb.PNG)

### Result/Output

![result](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/output_of_sensor_test.jpg)

## Enclosure

Elcoser design link(stl file): https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/full_design_case.stl

![3D case](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/case.PNG)

