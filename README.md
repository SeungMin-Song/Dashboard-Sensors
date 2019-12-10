
# Automitive UI - Hall Effect Sensor
## Introduction using a system diagram

The subject of our project team is Automotive UI. Our main goal is to make it easier and faster for doctors, nurses and paramedics to communicate. The main purpose in hardware is to design and build dashboard for paramedics.

My sensor is a hall effect sensor. Hall effect sensors are devices used to measure the magnitude of a magnetic field. The output voltage is directly proportional to the magnetic field strength through it. The sensor can be tested with magnetic materials. This allows you to get various values such as RPM, speed and distance.

At CENG317 I focused on sensor connection and testing. As you can see on the system diagram, I used a magnet to generate a magnetic field between the Hall effect sensor and the magnet. At this time, the voltage value of the signal changes and this data is sent to Raspberry Pi. I used a Wi-Fi connection to connect my Raspberry Pi to my laptop(screen), displaying the information from the Hall Effect sensor.

![system diagram](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/system_diagram.png)

## Bill of Materials/Budget

To implement this project, I purchased a hall effect sensor, a Raspberry Pi 4 B and a magnet. The total price is $ 171.64. Both the PCB board and enclosure are made in the school and are free.

<table style="width:100%" >
  <tr>
    <th>Product Name</th>
    <th>Price</th>
    <th>Shipping Fee</th>
	<th>Total Cost</th>
	<th>From</th>
  </tr>
  <tr>
    <td>SunFounder Switch Hall Sensor Module for Arduino and Raspberry Pi</td>
    <td>CAD$ 7.99</td>
	<td>CAD$ 4.02</td>
	<td>CAD$ 12.01</td>
    <td>SunFounder</td>
  </tr>
  <tr>
    <td>CanaKit Raspberry Pi 4 Starter Kit (4GB RAM)</td>
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
   <td>Elcosure(Using 3D printer)</td>
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

Most of the schedule was almost identical to the schedule(photo), except for breadboard milestone and pcb power up.

I was having trouble connecting my Raspberry Pi to my laptop on Breadboard Milestone. I tried to link this using only what I have. But I failed and my schedule was delayed for a week. I was trying to keep using a Wi-Fi connection from my Raspberry Pi to my laptop. Eventually I solved this problem in a week and returned to my schedule.

In PCB power-up I faced the problem of not turning on when using pcb. But I knew this was a problem with my sordering, and I finished pcb power ups two days later.

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

