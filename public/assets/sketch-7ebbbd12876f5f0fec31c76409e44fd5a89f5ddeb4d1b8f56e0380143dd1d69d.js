/* global background, createCanvas, Bird, key, Pipe, frameCount, nextGeneration, center */


const TOTAL = 250;
var birds = [];
var savedBirds = [];
var pipes = [];
let counter = 0;

function setup() {
    var canvas = createCanvas(400, 600);
    
    // Set a population of birds equal to TOTAL
    for (var i = 0; i < TOTAL; i++) {
        birds[i] = new Bird();
    }
}

function draw() {
    background(0);
    
    if (counter % 75 == 0) {
        pipes.push(new Pipe());
    }
    
    for (var i = pipes.length - 1; i >= 0; i--) {
        pipes[i].show();
        pipes[i].update();
        
        // Loop backwards through birds array and see if that bird is hitting a pipe. If so, we splice that bird out of the array and push it into savedBirds array
        for (var j = birds.length - 1; j >= 0; j--) {
            if (pipes[i].hits(birds[j])) {
                savedBirds.push(birds.splice(j, 1)[0]);
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
    
    // Check if entire generation is dead and repopulate, reset savedBirds array
    if (birds.length === 0) {
        counter = 0;
        nextGeneration();
        savedBirds = [];
        pipes = [];
        pipes.push(new Pipe());
    }
    
    counter++;
}

// User input to control bird (mouse click or space bar). Removed for ML project
// function mousePressed() {
//     bird.up();
// }

// function keyPressed() {
//     if (key == ' ') {
//         bird.up();
//     }
// }
;
