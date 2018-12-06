/* global TOTAL, birds, Bird, random, savedBirds */


function nextGeneration() {
    // Get the fitness of the previous generation
    calculateFitness();
    
    // Create new generation
    for (var i = 0; i < TOTAL; i++) {
        //birds[i] = new Bird();
        birds[i] = pickOne();
    }
}

function pickOne() {
    var index = 0;
    var r = random(1);
    
    while (r > 0) {
        r = r - savedBirds[index].fitness;
        index++;
    }
    index--;
    
    let bird = savedBirds[index]; // Not using fitness yet, testing out with random selection
    let child = new Bird(bird.brain);   // Create a child that is a copy of the selected bird's brain and mutate. This is where we could implement * Crossover *
    child.mutate();
    return child;
}

// Old pickOne, used a pure random selection, this clde was modified and added to the new function below index--
// Return a bird with probability mapped to its fitness
// function pickOne() {
    
// }

// Sum up a generation of bird's scores, then assign the fitness of the bird to be its score divided by the sum of all scores. This mapping of scores to fitness could be done using various mathematical formulae, but for now we will use a linear relationship.
function calculateFitness() {
    let sum = 0;
    
    for (let bird of savedBirds) {
        sum += bird.score;
    }
    
    // Linear fitness calculation
    for (let bird of savedBirds) {
        bird.fitness = bird.score / sum;
    }
}
;
