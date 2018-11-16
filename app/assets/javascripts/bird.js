/* global height, width, fill, ellipse, NeuralNetwork */

class Bird {
    constructor() {
        this.y = height / 2;
        this.x = 64;
    
        this.gravity = 0.6;
        this.lift = -15;
        this.velocity = 0;
        
        this.brain = new NeuralNetwork(4, 4, 1);
    }
    
    show() {
        fill(255);
        ellipse(this.x, this.y, 32, 32);
    }
    
    up() {
        this.velocity += this.lift;
    }
    
    // The bird will use its brain to decide if it should flap its wings or not
    think(pipes) {
        
        // Find the closest pipe (but ignore pipes behind us)
        let closest = null;
        let closestD = Infinity;
        for (var i = 0; i < pipes.length; i++) {
            let d = pipes[i].x - this.x;
            if (d < closestD && d > 0) {
                closest = pipes[i];
                closestD = d;
            }
        }
        
        // Inputs will be: bird's y, next pipe's top y, next pipe's bottom y, and next pipe's x
        // Normalizing data to be between 0 and 1... divide by height or width as appropriate 
        let inputs = [this.y / height, closest.top / height, closest.bottom / height, closest.x / width];
        
        let output = this.brain.predict(inputs);
        
        // The result of the prediction in this case is a single bit (0 or 1), and this is used to decide of the bird will flap its wings or not
        if (output > 0.5) {
            this.up();
        }
    }
    
    update() {
        this.velocity += this.gravity;
        this.velocity *= 0.9;
        this.y += this.velocity;
        
        // Stop bird from going off bottom of screen
        if (this.y > height) {
            this.y = height;
            this.velocity = 0;
        }
        
        // Stop bird from going off top of screen
        if (this.y < 0) {
            this.y = 0;
            this.velocity = 0;
        }
    }
}