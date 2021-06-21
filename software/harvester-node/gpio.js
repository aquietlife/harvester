const Gpio = require('onoff').Gpio;

const buttons = {
  1: new Gpio(6, 'in', 'both'),
  2: new Gpio(24, 'in', 'both'),
  3: new Gpio(12, 'in', 'both'),
  4: new Gpio(13, 'in', 'both'),
  5: new Gpio(22, 'in', 'both'),
  6: new Gpio(17, 'in', 'both'),
  7: new Gpio(16, 'in', 'both'),
  8: new Gpio(4, 'in', 'both'),
  buttonRecord: new Gpio(23, 'in', 'both'),
  buttonLoop: new Gpio(5, 'in', 'both'),
}

buttons[1].watch((err, value) => console.log("BUTTON 1!"));
buttons[2].watch((err, value) => console.log("BUTTON 2!"));
buttons[3].watch((err, value) => console.log("BUTTON 3!"));
buttons[4].watch((err, value) => console.log("BUTTON 4!"));
buttons[5].watch((err, value) => console.log("BUTTON 5!"));
buttons[6].watch((err, value) => console.log("BUTTON 6!"));
buttons[7].watch((err, value) => console.log("BUTTON 7!"));
buttons[8].watch((err, value) => console.log("BUTTON 8!"));
buttons.buttonRecord.watch((err, value) => console.log("buttonRecord"))
buttons.buttonLoop.watch((err, value) => console.log("buttonLoop"))

process.on('SIGINT', _ => {  
  for (button in buttons) {
    buttons[button].unexport();
  }  
});
