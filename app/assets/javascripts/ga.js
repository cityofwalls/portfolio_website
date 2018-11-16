/* global TOTAL, birds, Bird */

function nextGeneration() {
    // Create new generation
    for (var i = 0; i < TOTAL; i++) {
        birds[i] = new Bird();
    }
}