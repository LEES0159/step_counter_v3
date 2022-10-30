def on_button_pressed_ab():
    basic.show_icon(IconNames.YES)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global steps
    steps += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

steps = 1000
radio.set_group(1)
radio.set_frequency_band(7)
radio.set_transmit_power(7)
basic.show_icon(IconNames.YES)
basic.clear_screen()

def on_forever():
    radio.send_value("steps", steps)
    serial.write_value("steps", steps)
basic.forever(on_forever)
