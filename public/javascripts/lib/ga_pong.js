/* global paddles TOTAL random Paddle */

function nextGeneration() {
    calculateFitness();
    
    let topThree = pickTopThree();
    for (var i = 0; i < TOTAL; i++) {
        paddles[i] = breeder(topThree);
    }
}

function calculateFitness() {
    let sum = 0;
    
    for (let paddle of paddles) {
        sum += paddle.score;
    }
    
    for (let paddle of paddles) {
        paddle.fitness = paddle.score / sum;
    }
}

function pickTopThree() {
    let result = [];
    for (var i = 0; i < 3; i++) {
        var currentMax = paddles[0].fitness;
        var index = 0;
        for (var j = 1; j < paddles.length; j++) {
            if (paddles[j].fitness > currentMax) {
                currentMax = paddles[j].fitness;
                index = j;
            }
        }
        result.push(paddles.splice(index, 1)[0]);
    }
    return result;
}

function breeder(parents) {
    var child = parents[0].brain.copy();
    parents = shuffle(parents);
    var otherDNA = parents[0].brain.copy();
    var newChild = new Paddle(0, child.crossover(otherDNA));
    newChild.mutate();
    return newChild;
}

function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}

// function pickOne() {
//     var index = 0;
//     var r = random(1);
    
//     while (r > 0) {
//         r = r - paddles[index].fitness;
//         console.log(index);
//         index++;
//     }
//     index--;
    
//     let paddle = paddles[index];
//     let child = new Paddle(0, paddle.brain);
//     child.mutate();
//     return child;
// }