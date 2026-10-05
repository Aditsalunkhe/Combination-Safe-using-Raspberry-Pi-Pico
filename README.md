# Raspberry Pi Pico Combination Safe

A 3-digit combination safe. Turn the potentiometer dial to a digit (0 to 9),
press the button to enter it, and if the code is correct a servo swings the
lock open. A wrong code flashes the red LED.

**Live simulation:** https://wokwi.com/projects/477029533191591937

## Features
- Potentiometer dial for digit selection
- Button to confirm each digit
- Servo lock opens for 3 seconds on the correct code
- Green LED for success, red LED flashes for a wrong code
- Serial output shows the dial value and entered digits

## Components
| Part | Qty |
|---|---|
| Raspberry Pi Pico | 1 |
| Potentiometer | 1 |
| Push button | 1 |
| Servo motor | 1 |
| LEDs (green, red) | 2 |
| 220Ω resistors | 2 |

## Wiring
| Component | Pico pin |
|---|---|
| Potentiometer SIG | GP26 (ADC0) |
| Potentiometer VCC / GND | 3V3(OUT) / GND |
| Button | GP14 and GND |
| Servo signal | GP16 |
| Servo V+ / GND | VBUS / GND |
| Green LED (via resistor) | GP10 |
| Red LED (via resistor) | GP11 |

## How to run
1. Open the Wokwi link (MicroPython Pico template) and press ▶.
2. Turn the dial until the serial monitor shows the digit you want.
3. Click the button to enter it. Repeat for all 3 digits.
4. Default code: **3 - 7 - 1** (change `CODE` in `main.py`).

## How it works
The ADC reads the potentiometer (0 to 65535) and scales it to a digit from
0 to 9. Each button press stores the current digit. After 3 digits the list
is compared with `CODE`. A match drives the servo PWM (50 Hz) to 90° and
lights the green LED, otherwise the red LED flashes.

## Future improvements
- Lock out for 10 seconds after 3 wrong attempts
- Buzzer feedback on each key press
- Change the code from within the safe

## License
MIT
