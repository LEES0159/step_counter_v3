input.onGesture(Gesture.Shake, function () {
    steps += 1
})
let steps = 0
let num_msgs_sent = 0
radio.setGroup(1)
radio.setFrequencyBand(7)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.clearScreen()
basic.forever(function () {
    radio.sendValue("msg", num_msgs_sent)
    radio.sendValue("steps", steps)
    num_msgs_sent += 1
    basic.pause(10 * (60 * 1000))
})
