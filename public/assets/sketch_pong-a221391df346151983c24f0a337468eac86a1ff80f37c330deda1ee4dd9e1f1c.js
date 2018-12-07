/* global createCanvas background line stroke strokeWeight Paddle keyCode LEFT_ARROW RIGHT_ARROW UP_ARROW DOWN_ARROW Ball */


const WIDTH = 400;
const HEIGHT = 400;
const PAD_WIDTH = 20;
const NUM_PADDLES = 2;
const DIAMETER = 30;

var paddles = [];
var ball = new Ball();

function setup() {
    createCanvas(WIDTH, HEIGHT);
    
    for (var i = 0; i < NUM_PADDLES; i++) {
        if (i % 2 === 0) {
            paddles.push(new Paddle(0));
        } else {
            paddles.push(new Paddle(WIDTH - PAD_WIDTH));
        }
    }
}

function draw() {
    background(0);
    
    // Draw center divider
    stroke(255);
    strokeWeight(5);
    line(WIDTH / 2, 0, WIDTH / 2, HEIGHT);
    
    // Draw goal areas for players
    line(PAD_WIDTH, 0, PAD_WIDTH, HEIGHT);
    line(WIDTH - PAD_WIDTH, 0, WIDTH - PAD_WIDTH, HEIGHT);
    
    // Paddle movement
    for (var i = 0; i < paddles.length; i++) {
        paddles[i].update();
        paddles[i].show();
        paddles[i].stayOnScreen();
    }
    
    // Ball movement
    ball.update();
    ball.show();
    ball.collide();
    
    // Ball hitting a Paddle?
    for (var i = 0; i < paddles.length; i++) {
        paddles[i].collide(ball);
    }
}

function keyPressed() {
    if (keyCode === LEFT_ARROW) {
        paddles[0].up();
    } else if (keyCode === RIGHT_ARROW) {
        paddles[0].down();
    }
    if (keyCode === UP_ARROW) {
        paddles[1].up();
    } else if (keyCode === DOWN_ARROW) {
        paddles[1].down();
    }
}

function keyReleased() {
    if (keyCode === LEFT_ARROW || keyCode === RIGHT_ARROW) {
        paddles[0].stop();
    } else if (keyCode === UP_ARROW || keyCode === DOWN_ARROW) {
        paddles[1].stop();
    }
}
;
