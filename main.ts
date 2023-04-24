input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
        `)
    Choice = "rock"
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    Choice = "scissors"
})
radio.onReceivedString(function (receivedString) {
    opponent_Choice = receivedString
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        `)
    Choice = "paper"
})
input.onGesture(Gesture.Shake, function () {
    if (Choice == "None") {
    	
    } else {
        radio.sendString(Choice)
    }
})
function Endgame () {
    if (Choice == "rock") {
        if (opponent_Choice == "rock") {
            basic.showLeds(`
                # # # # #
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                `)
        } else if (opponent_Choice == "paper") {
            basic.showLeds(`
                . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # # # .
                `)
        } else if (opponent_Choice == "scissors") {
            basic.showLeds(`
                . . . . .
                # . . . #
                # . # . #
                # . # . #
                . # . # .
                `)
        }
    }
    if (Choice == "paper") {
        if (opponent_Choice == "rock") {
            basic.showLeds(`
                . . . . .
                # . . . #
                # . # . #
                # . # . #
                . # . # .
                `)
        } else if (opponent_Choice == "paper") {
            basic.showLeds(`
                # # # # #
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                `)
        } else if (opponent_Choice == "scissors") {
            basic.showLeds(`
                . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # # # .
                `)
        }
    }
    if (Choice == "scissors") {
        if (opponent_Choice == "rock") {
            basic.showLeds(`
                . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # # # .
                `)
        } else if (opponent_Choice == "paper") {
            basic.showLeds(`
                . . . . .
                # . . . #
                # . # . #
                # . # . #
                . # . # .
                `)
        } else if (opponent_Choice == "scissors") {
            basic.showLeds(`
                # # # # #
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                `)
        }
    }
}
let opponent_Choice = ""
let Choice = ""
Choice = "None"
radio.setGroup(1)
opponent_Choice = ""
radio.sendNumber(1)
basic.forever(function () {
    Endgame()
})
