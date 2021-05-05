def setamber():
    pins.analog_write_pin(AnalogPin.P0, 767)
    pins.analog_write_pin(AnalogPin.P1, 63)
    pins.analog_write_pin(AnalogPin.P2, 0)
    for index in range(1):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        basic.pause(100)
    images.icon_image(IconNames.SAD).show_image(0)
def setred():
    pins.analog_write_pin(AnalogPin.P0, 511)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 0)
    for index2 in range(2):
        music.play_tone(523, music.beat(BeatFraction.QUARTER))
        basic.pause(100)
    basic.show_string("Feeling lucky?")
    images.icon_image(IconNames.SKULL).show_image(0)
def setgreen():
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 511)
    pins.analog_write_pin(AnalogPin.P2, 0)
    images.icon_image(IconNames.HEART).show_image(0)
distance = 0
pins.analog_write_pin(AnalogPin.P0, 0)
pins.analog_write_pin(AnalogPin.P1, 0)
pins.analog_write_pin(AnalogPin.P2, 0)
safe = 175
unsafe = 125

def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P8, DigitalPin.P16, PingUnit.CENTIMETERS)
    basic.show_number(distance)
    if distance == 0 or distance > safe:
        setgreen()
    elif distance > unsafe:
        setamber()
    elif distance < unsafe:
        setred()
    basic.pause(5000)
basic.forever(on_forever)
