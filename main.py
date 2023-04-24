def on_button_pressed_a():
    global Choice
    basic.show_leds("""
        . . . . .
                . # # # .
                . # # # .
                . # # # .
                . . . . .
    """)
    Choice = "rock"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Choice
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
    Choice = "scissors"
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global opponent_Choice
    opponent_Choice = receivedString
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global Choice
    basic.show_leds("""
        . # . # .
                # . # . #
                . # . # .
                # . # . #
                . # . # .
    """)
    Choice = "paper"
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if Choice == "None":
        pass
    else:
        radio.send_string(Choice)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def Endgame():
    if Choice == "rock":
        if opponent_Choice == "rock":
            basic.show_leds("""
                # # # # #
                                . . # . .
                                . . # . .
                                . . # . .
                                . . # . .
            """)
        elif opponent_Choice == "paper":
            basic.show_leds("""
                . # . . .
                                . # . . .
                                . # . . .
                                . # . . .
                                . # # # .
            """)
        elif opponent_Choice == "scissors":
            basic.show_leds("""
                . . . . .
                                # . . . #
                                # . # . #
                                # . # . #
                                . # . # .
            """)
    if Choice == "paper":
        if opponent_Choice == "rock":
            basic.show_leds("""
                . . . . .
                                # . . . #
                                # . # . #
                                # . # . #
                                . # . # .
            """)
        elif opponent_Choice == "paper":
            basic.show_leds("""
                # # # # #
                                . . # . .
                                . . # . .
                                . . # . .
                                . . # . .
            """)
        elif opponent_Choice == "scissors":
            basic.show_leds("""
                . # . . .
                                . # . . .
                                . # . . .
                                . # . . .
                                . # # # .
            """)
    if Choice == "scissors":
        if opponent_Choice == "rock":
            basic.show_leds("""
                . # . . .
                                . # . . .
                                . # . . .
                                . # . . .
                                . # # # .
            """)
        elif opponent_Choice == "paper":
            basic.show_leds("""
                . . . . .
                                # . . . #
                                # . # . #
                                # . # . #
                                . # . # .
            """)
        elif opponent_Choice == "scissors":
            basic.show_leds("""
                # # # # #
                                . . # . .
                                . . # . .
                                . . # . .
                                . . # . .
            """)
opponent_Choice = ""
Choice = ""
Choice = "None"
radio.set_group(1)
opponent_Choice = ""

def on_forever():
    Endgame()
basic.forever(on_forever)
