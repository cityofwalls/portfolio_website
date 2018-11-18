/* global background, createCanvas, Bird, key, Pipe, frameCount, nextGeneration, center */

const TOTAL = 250;
var birds = [];
var pipes = [];

function setup() {
    var canvas = createCanvas(400, 600);
    //canvas.center('vertical');
    canvas.position(30, 120);
    
    // Set a population of birds equal to TOTAL
    for (var i = 0; i < TOTAL; i++) {
        birds[i] = new Bird();
    }
    
    // Push first pipe to pipe array
    pipes.push(new Pipe());
}

function draw() {
    background(0);
    
    for (var i = pipes.length - 1; i >= 0; i--) {
        pipes[i].show();
        pipes[i].update();
        
        // Loop backwards through birds array and see if that bird is hitting a pipe. If so, we splice that bird out of the array
        for (var j = birds.length - 1; j >= 0; j--) {
            if (pipes[i].hits(birds[j])) {
                birds.splice(j, 1);
            }
        }
        
        if (pipes[i].offscreen()) {
            pipes.splice(i, 1);
        }
    }
    
    // Have each bird react to input, show and update each bird
    for (let bird of birds) {
        bird.think(pipes);
        bird.show();
        bird.update();
    }
    
    // Check if entire generation is dead and repopulate
    if (birds.length === 0) {
        nextGeneration();
    }
    
    if (frameCount % 100 == 0) {
        pipes.push(new Pipe());
    }
}

// function mousePressed() {
//     bird.up();
// }

// function keyPressed() {
//     if (key == ' ') {
//         bird.up();
//     }
// }