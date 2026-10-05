from machine import Pin, PWM, ADC
import time

pot = ADC(26)
btn = Pin(14, Pin.IN, Pin.PULL_UP)
green = Pin(10, Pin.OUT)
red = Pin(11, Pin.OUT)
servo = PWM(Pin(16)); servo.freq(50)

def angle(a):
    servo.duty_u16(int(1638 + a / 180 * 6554))   # 0.5ms to 2.5ms pulse

CODE = [3, 7, 1]
entry = []
last = -1
angle(0)

while True:
    digit = pot.read_u16() * 10 // 65536         # dial reads 0-9
    if digit != last:
        print("Dial:", digit); last = digit
    if btn.value() == 0:
        entry.append(digit)
        print("Entered:", digit)
        time.sleep_ms(300)
        while btn.value() == 0:
            pass
        if len(entry) == len(CODE):
            if entry == CODE:
                print("UNLOCKED")
                green.on(); angle(90); time.sleep(3)
                angle(0); green.off()
            else:
                print("WRONG CODE")
                for _ in range(4):
                    red.toggle(); time.sleep_ms(150)
                red.off()
            entry = []