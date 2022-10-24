def on_gesture_shake():
    global steps
    steps += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 0
num_msgs_sent = 0
radio.set_group(1)
radio.set_frequency_band(7)
radio.set_transmit_power(7)
basic.show_icon(IconNames.YES)
basic.clear_screen()

def on_forever():
    global num_msgs_sent
    radio.send_value("steps", steps)
    radio.send_value("msg", num_msgs_sent)
    num_msgs_sent += 1
    basic.pause(10 * (60 * 1000))
basic.forever(on_forever)
