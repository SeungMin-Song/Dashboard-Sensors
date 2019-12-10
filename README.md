
# Automitive UI - Hall Effect Sensor

## Introduction using a system diagram

![system diagram](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/system_diagram.png)

The subject of our project team is Automotive UI. Our main goal is to make it easier and faster for doctors, nurses and paramedics to communicate. The main purpose in hardware is to design and build dashboard for paramedics.

My sensor is a hall effect sensor. Hall effect sensors are devices used to measure the magnitude of a magnetic field. The output voltage is directly proportional to the magnetic field strength through it. The sensor can be tested with magnetic materials. This allows you to get various values such as RPM, speed and distance.

At CENG317 I focused on sensor connection and testing. As you can see on the system diagram, I used a magnet to generate a magnetic field between the Hall effect sensor and the magnet. At this time, the voltage value of the signal changes and this data is sent to Raspberry Pi. I used a Wi-Fi connection to connect my Raspberry Pi to my laptop(screen), displaying the information from the Hall Effect sensor.

## Table of Contents

1.  [Introduction using a system diagram](#introduction-using-a-system-diagram)
2.  [Bill of Materials](#bill-of-materials) 
3.  [Time Commitment](#time-commitment)
4.  [Mechanical Assembly](#mechanical-assembly)
5.  [PCB with soldering](#pcb-with-soldering)
6.  [Power Up and production testing](#power-up-and-production-testing)
7.  [Enclosure](#enclosure)

## Bill of Materials

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
    <td>PCB board(https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/pcb.png)</td>
    <td>CAD$ 0.00</td>
	<td>CAD$ 0.00</td>
	<td>CAD$ 0.00</td>
    <td>Prototype Lab</td>
</tr>
<tr>
   <td>Enclosure (Using 3D printer: https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/full_design_case.stl)</td>
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

Receipt LINK(PNG file):<br>
   Hall Effect Sensor: <a href="https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/receiptForHallEffectSensor.PNG"> https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/receiptForHallEffectSensor.PNG </a><br>
   Raspberry Pi 4: <a href="https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/receiptForRaspberryPI.PNG"> https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/receiptForRaspberryPI.PNG </a>
   
Budget LINK: <a href="https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/documentation/NewBudget4SeungMinSong.pdf"> https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/documentation/NewBudget4SeungMinSong.pdf </a>


## Time Commitment

### shcedule spend time:

	1) Order Hall effect Sensor and Raspberry Pi: 1~2 day include shipping time
	
	2) Design BreadBoard and PCB: 1~2 day
	
	3) Test BreadBoard design and measure supply power: 1~2 hours
	
	4) Order pcb: 1 day
	
	5) Sordering PCB and test: 1~2 hours
	
	6) design enclosure and print: 2~3 days (printing time is around 12 hours)
	
	Total: 5 days 2 hours ~ 10 day 4 hours

## Mechanical Assembly

### Make connection

I set up auto connect wifi using the code below. If the Wi-Fi you created when you powered up your Raspberry Pi is ready to connect, the Raspberry Pi will connect to it by itself.

```
network={
	ssid="WiFi Name"
	password="WiFi Password"
	priority=999
	}
```

The ip address (172.20.10.5) in the picture below is the address you used to connect your Raspberry Pi to the VNC Viewer.

![ip_addr](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/ip_addr.PNG)

### Design Bread Board circuit

Create connection using BreadBoard

	- Raspberry Pi pin 4(5V) to VCC of hall effect sensor
	
	- Raspberry Pi pin 12(GPIO 18) to SIG of hall effect sensor
	
	- Raspberry Pi pin 14(GND) to GND of Hall effect sensor
	
![BB_Design](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/Hall%20Effect%20Sensor_BB.ps.png)

Design File (BB, schmetic): <a href="https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/software/Hall%20Effect%20Sensor.fzz"> https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/software/Hall%20Effect%20Sensor.fzz </a><br>

### Check Sensor supply power

Measure VCC to GND

![check power voltage](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/Check_Power_Voltage.jpg)

### Design PCB

Similar with BB design. Please make sure your pin location.
Using 3 pins header and 6 pins header

	- Raspberry Pi pin 4(5V) to VCC of hall effect sensor
	
	- Raspberry Pi pin 12(GPIO 18) to SIG of hall effect sensor
	
	- Raspberry Pi pin 14(GND) to GND of Hall effect sensor

![pcb design](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/design/Hall%20Effect%20Sensor%20pcb_pcb.jpg)

Design pcb(pcb): <a href="https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/software/Hall%20Effect%20Sensor%20pcb.fzz"> https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/software/Hall%20Effect%20Sensor%20pcb.fzz </a><br>

### Coding

This code is written in the Python language. This code indicates that the magnetic material is in detect when the sensor is in detect with a magnet or magnetic material.

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

## PCB with soldering

After get pcb board, make sure about pcb board.
And do soldering with headers(3 pins header and 6 pins header)

![pcb](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/pcb.png)


## Power Up and production testing

### How power up:

	1. connect BB(breadboard)/PCB to Hall Effect Sensor and Raspberry pi (using jumper wires)
	
	2. connect power to raspberry pi
	
	3. If Blue led turns on, you are success to power up.

#### Bread Board Power up

![BB_power_up](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/BBwithSensor.jpg)

#### PCB Power up

![PCB_power_up](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/power_on_pcb.PNG)

### Sensor Testing:
	
	Read values from sensor
	
		1. Connect raspberry pi to monitor/Labtop
		
		2. Run VNC Viewer
		
		3. Run your python progeram in the terminal
		
		4. Test using magnet (If you success, some sentence will be printed with orange LED)

#### Result/Output

when sensor detects magnetic or magnetic materials terminal prints "Magnetic material detected". If it removed, terminal prints "Nonmagnetic material".

![result](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/output_of_sensor_test.jpg)

## Enclosure

This is my enclosure. I built these enclosures using a 3D printer. First, the sensor's enclosure is open design for detect magnetic material. I made a separate enclosure for the sensor to reduce the impact on the Raspberry Pi when I thought it would be mounted on a car. Most enclosures of Raspberry Pi and pcb are encased in a case because their primary purpose is to protect them.

Enclosure design link(stl file): https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/full_design_case.stl

![3D case](https://github.com/SeungMin-Song/Dashboard-Sensors/blob/master/images/case.PNG)

