/* global paddles TOTAL random Paddle */

function nextGeneration() {
    calculateFitness();
    
    let topThree = pickTopThree();
    for (var i = 0; i < TOTAL; i++) {
        paddles[i] = spawner(topThree);
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

// Take top fitness, or take pure 2nd/3rd place, or take crossover 2nd/3rd
function spawner(parents) {
    var childType = Math.random(1);
    if (childType < 0.25) {
        var childBrainType1 = parents[0].brain.copy();
        var otherBrainType1 = parents[1].brain.copy();
        if (Math.random(1) < 0.5) {
            otherBrainType1 = parents[2].brain.copy();
        }
        var newChildType1 = new Paddle(0, childBrainType1.crossover(otherBrainType1));
        newChildType1.mutate();
        return newChildType1;
    } else if (childType < 0.5) {
        var childBrainType2 = parents[1].brain.copy();
        var otherBrainType2 = parents[2].brain.copy();
        if (Math.random(1) < 0.5) {
            otherBrainType2 = parents[0].brain.copy();
        }
        var newChildType2 = new Paddle(0, childBrainType2.crossover(otherBrainType2));
        newChildType2.mutate();
        return newChildType2;
    } else if (childType < 0.75) {
        var childBrainType3 = parents[2].brain.copy();
        var otherBrainType3 = parents[0].brain.copy();
        if (Math.random(1) < 0.5) {
            otherBrainType3 = parents[1].brain.copy();
        }
        var newChildType3 = new Paddle(0, childBrainType3.crossover(otherBrainType3));
        newChildType3.mutate();
        return newChildType3;
    } else {
        if (Math.random(1) < 0.5) {
            return parents[0];
        } else {
            if (Math.random(1) < 0.66) {
                return parents[1];
            } else {
                return parents[2];
            }
        }
    }
    
    // if (Math.random(1) < 0.5) {
    //     var childBrain0 = parents[0].brain.copy();
    //     childBrain0.mutate();
    //     var newChild0 = new Paddle(0, childBrain0);
    //     return newChild0;
    // } else {
    //     var r = Math.random(1);
    //     if (r < 0.33) {
    //         var childBrain1 = parents[1].brain.copy();
    //         childBrain1.mutate();
    //         var newChild1 = new Paddle(0, childBrain1);
    //         return newChild1;
    //     } else if (r < 0.66) {
    //         var childBrain2 = parents[2].brain.copy();
    //         childBrain2.mutate();
    //         var newChild2 = new Paddle(0, childBrain2);
    //         return newChild2;
    //     } else {
    //         var childBrain = parents[1].brain.copy();
    //         var otherBrain = parents[2].brain.copy();
    //         var newChild = new Paddle(0, childBrain.crossover(otherBrain));
    //         newChild.mutate();
    //         return newChild;
    //     }
    // }
    
    // var child = parents[0].brain.copy();
    // parents = shuffle(parents);
    // var otherDNA = parents[0].brain.copy();
    // var newChild = new Paddle(0, child.crossover(otherDNA));
    // newChild.mutate();
    // return newChild;
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