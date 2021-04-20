def setamber():
    pins.analog_write_pin(AnalogPin.P0, 762)
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
range2 = 0
pins.analog_write_pin(AnalogPin.P0, 0)
pins.analog_write_pin(AnalogPin.P1, 0)
pins.analog_write_pin(AnalogPin.P2, 0)

def on_forever():
    global range2
    range2 = sonar.ping(DigitalPin.P8, DigitalPin.P16, PingUnit.CENTIMETERS)
    basic.show_number(range2)
    if range2 == 0 or range2 > 170:
        setgreen()
    elif range2 > 125:
        setamber()
    elif range2 < 125:
        setred()
    basic.pause(5000)
basic.forever(on_forever)
