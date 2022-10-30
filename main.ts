input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Yes)
    basic.showNumber(steps)
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    steps += 1
})
let steps = 0
steps = 0
radio.setGroup(1)
radio.setFrequencyBand(7)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.clearScreen()
basic.forever(function () {
    radio.sendValue("steps", steps)
    basic.pause(10 * (60 * 1000))
})
