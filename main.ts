function setamber () {
    pins.analogWritePin(AnalogPin.P0, 767)
    pins.analogWritePin(AnalogPin.P1, 63)
    pins.analogWritePin(AnalogPin.P2, 0)
    for (let index = 0; index < 1; index++) {
        basic.pause(100)
    }
    images.iconImage(IconNames.Sad).showImage(0)
}
function setred () {
    pins.analogWritePin(AnalogPin.P0, 511)
    pins.analogWritePin(AnalogPin.P1, 0)
    pins.analogWritePin(AnalogPin.P2, 0)
    for (let index = 0; index < 2; index++) {
        basic.pause(100)
    }
    text = text_list[randint(0, text_list.length - 1)]
    basic.showString("" + (text))
    images.iconImage(IconNames.Skull).showImage(0)
}
function setgreen () {
    pins.analogWritePin(AnalogPin.P0, 0)
    pins.analogWritePin(AnalogPin.P1, 511)
    pins.analogWritePin(AnalogPin.P2, 0)
    images.iconImage(IconNames.Heart).showImage(0)
}
let distance = 0
let text = ""
let text_list: string[] = []
pins.analogWritePin(AnalogPin.P0, 0)
pins.analogWritePin(AnalogPin.P1, 0)
pins.analogWritePin(AnalogPin.P2, 0)
let safe = 175
let unsafe = 125
text_list = ["Uh-oh!", "Eeek!", "Oops!", "Eff-off!", "Wibble!"]
basic.forever(function () {
    distance = sonar.ping(
    DigitalPin.P8,
    DigitalPin.P16,
    PingUnit.Centimeters
    )
    basic.showNumber(distance)
    if (distance == 0 || distance > safe) {
        setgreen()
    } else if (distance > unsafe) {
        setamber()
    } else if (distance < unsafe) {
        setred()
    }
    basic.pause(5000)
})
