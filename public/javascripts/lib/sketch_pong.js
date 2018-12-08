/* global createCanvas background line stroke strokeWeight Paddle Ball nextGeneration keyCode LEFT_ARROW RIGHT_ARROW UP_ARROW DOWN_ARROW */

const WIDTH = 500;
const HEIGHT = 500;
const PAD_WIDTH = 20;
const NUM_PADDLES = 2;
const DIAMETER = 30;
const TOTAL = 8;

var c;
var paddles = [];
var currentPaddles = [];
var p1 = 0;
var p2 = 1;
var ball;

var paddleColor = [250, 250, 250];

function setup() {
    createCanvas(WIDTH, HEIGHT);
    
    for (var i = 0; i < TOTAL; i++) {
        if (i % 2 === 0) {
            paddles.push(new Paddle(0));
        } else {
            paddles.push(new Paddle(WIDTH - PAD_WIDTH));
        }
    }
    
    getCurrentPaddles();
    ball = new Ball();
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
    
    // Paddle movement... allow paddles to think
    for (var i = 0; i < currentPaddles.length; i++) {
        currentPaddles[i].think(ball);
        currentPaddles[i].update();
        currentPaddles[i].show(paddleColor);
        currentPaddles[i].stayOnScreen();
    }
    
    // Ball movement
    ball.update();
    ball.show();
    ball.collide();
    
    // Ball hitting a Paddle?
    for (var i = 0; i < currentPaddles.length; i++) {
        var miss = currentPaddles[i].collide(ball);
        if (miss) {
            if (i === 0) {
                currentPaddles[1].score += 1.0;
            } else {
                currentPaddles[0].score += 1.0;
            }
            saveScores();
            incrementPlayers();
            getCurrentPaddles();
        }
    }
}

function saveScores() {
    paddles[p1].score = currentPaddles[0].score;
    paddles[p2].score = currentPaddles[1].score;
}

function incrementPlayers() {
    if (p2 < TOTAL - 1) {
        p2++;
    } else {
        p1++;
        if (p1 === TOTAL - 1) {
            p1 = 0;
            p2 = 1;
            updatePaddleColor();
            nextGeneration();
        } else {
            p2 = p1 + 1;
        }
    }
}

/* Each generation will play ALLvALL with their scores increasing as they go */
function getCurrentPaddles() {
    currentPaddles = [];
    currentPaddles.push(new Paddle(0, paddles[p1].brain));
    currentPaddles[0].score = paddles[p1].score;
    currentPaddles.push(new Paddle(WIDTH - PAD_WIDTH, paddles[p2].brain));
    currentPaddles[1].score = paddles[p2].score;
}

function updatePaddleColor() {
    var r = Math.random();
    if (r < 0.333) {
        paddleColor[0] -= 25;
    } else if (r < 0.666) {
        paddleColor[1] -= 25;
    } else {
        paddleColor[2] -= 25;
    }
    
    for (var i = 0; i < paddleColor.length; i++) {
        if (paddleColor[i] < 50) {
            paddleColor[i] = 250;
        }
    }
}

// function keyPressed() {
//     if (keyCode === LEFT_ARROW) {
//         paddles[0].up();
//     } else if (keyCode === RIGHT_ARROW) {
//         paddles[0].down();
//     }
//     if (keyCode === UP_ARROW) {
//         paddles[1].up();
//     } else if (keyCode === DOWN_ARROW) {
//         paddles[1].down();
//     }
// }

// function keyReleased() {
//     if (keyCode === LEFT_ARROW || keyCode === RIGHT_ARROW) {
//         paddles[0].stop();
//     } else if (keyCode === UP_ARROW || keyCode === DOWN_ARROW) {
//         paddles[1].stop();
//     }
// }