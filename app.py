# import necessary packages
from gpiozero import LED
from flask import Flask, render_template, request

# create a Flask object
app = Flask(__name__)

# create an object that refers to a relay
relay1 = LED(2)
relay2 = LED(3)
relay3 = LED(4)
relay4 = LED(17)
relay5 = LED(27)
relay6 = LED(22)
relay7 = LED(10)
relay8 = LED(9)

# set the relay off; remember the relay works with inverted logic
relay1.on()
relay2.on()
relay3.on()
relay4.on()
relay5.on()
relay6.on()
relay7.on()
relay8.on()

# save current relay state
relay1_state = 'OFF'
relay2_state = 'OFF'
relay3_state = 'OFF'
relay4_state = 'OFF'
relay5_state = 'OFF'
relay6_state = 'OFF'
relay7_state = 'OFF'
relay8_state = 'OFF'

# display the main web page
@app.route('/')
def main():
    if relay1.value == 0:
        relay1_state = 'ON'
    else:
        relay1_state = 'OFF'

    if relay2.value == 0:
        relay2_state = 'ON'
    else:
        relay2_state = 'OFF'

    if relay3.value == 0:
        relay3_state = 'ON'
    else:
        relay3_state = 'OFF'

    if relay4.value == 0:
        relay4_state = 'ON'
    else:
        relay4_state = 'OFF'

    if relay5.value == 0:
        relay5_state = 'ON'
    else:
        relay5_state = 'OFF'

    if relay6.value == 0:
        relay6_state = 'ON'
    else:
        relay6_state = 'OFF'

    if relay7.value == 0:
        relay7_state = 'ON'
    else:
        relay7_state = 'OFF'

    if relay8.value == 0:
        relay8_state = 'ON'
    else:
        relay8_state = 'OFF'

    # pass the relay state to the index.html and return it to the user
    return render_template('index.html', relay1_state=relay1_state,
    relay2_state=relay2_state,
    relay3_state=relay3_state,
    relay4_state=relay4_state,
    relay5_state=relay5_state,
    relay6_state=relay6_state,
    relay7_state=relay7_state,
    relay8_state=relay8_state
    )

# execute control() when someone presses the on/off buttons
@app.route('/<action>')
def control(action):
    global relay1_state
    global relay2_state
    global relay3_state
    global relay4_state
    global relay5_state
    global relay6_state
    global relay7_state
    global relay8_state
    # if the action part of the URL is 'on', turn the relay on
    if action == 'r1_on':
        # set the relay on
        relay1.off()
        # save the relay state
        relay1_state = 'ON'
    if action == 'r1_off':
        relay1.on()
        relay1_state = 'OFF'

    if action == 'r2_on':
        relay2.off()
        relay2_state = 'ON'
    if action == 'r2_off':
        relay2.on()
        relay2_state = 'OFF'

    if action == 'r3_on':
        relay3.off()
        relay3_state = 'ON'
    if action == 'r3_off':
        relay3.on()
        relay3_state = 'OFF'

    if action == 'r4_on':
        relay4.off()
        relay4_state = 'ON'
    if action == 'r4_off':
        relay4.on()
        relay4_state = 'OFF'

    if action == 'r5_on':
        relay5.off()
        relay5_state = 'ON'
    if action == 'r5_off':
        relay5.on()
        relay5_state = 'OFF'

    if action == 'r6_on':
        relay6.off()
        relay6_state = 'ON'
    if action == 'r6_off':
        relay6.on()
        relay6_state = 'OFF'

    if action == 'r7_on':
        relay7.off()
        relay7_state = 'ON'
    if action == 'r7_off':
        relay7.on()
        relay7_state = 'OFF'

    if action == 'r8_on':
        relay8.off()
        relay8_state = 'ON'
    if action == 'r8_off':
        relay8.on()
        relay8_state = 'OFF'

    # pass the relay state to the index.html and return it to the user
    return render_template('index.html', relay1_state=relay1_state,
    relay2_state=relay2_state,
    relay3_state=relay3_state,
    relay4_state=relay4_state,
    relay5_state=relay5_state,
    relay6_state=relay6_state,
    relay7_state=relay7_state,
    relay8_state=relay8_state
    )

# start the web server at localhost on port 80
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)