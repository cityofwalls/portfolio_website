/* global WIDTH HEIGHT PAD_WIDTH rect fill NeuralNetwork noStroke */

class Paddle {
    constructor(x, brain) {
        this.w = PAD_WIDTH;
        this.h = HEIGHT / 5;
        this.x = x;
        this.y = HEIGHT / 2 - (this.h / 2);
        this.v = 0;
        this.a = 3;
        this.score = 0.0;
        this.fitness = 0.0;
        
        if (brain) {
            this.brain = brain.copy();
        } else {
            // inputs: this.y, ball.y
            /*
                First trying with 2 input, 4 hidden, and 2 output nodes.
                My argument is that a paddle only needs to see its y value and the ball's y value
                to make a decision. The output values will be used to see if the paddle should move
                up, down, or stay still (==).
            */
            this.brain = new NeuralNetwork(2, 6, 3);
        }
    }
    
    mutate() {
        this.brain.mutate(0.1);
    }
    
    show(color) {
        // noStroke();
        fill(color[0], color[1], color[2]);
        rect(this.x, this.y, this.w, this.h);
    }
    
    update() {
        this.y += this.v;
    }
    
    up() {
        this.v -= this.a;
    }
    
    down() {
        this.v += this.a;
    }
    
    stop() {
        this.v = 0;
    }
    
    stayOnScreen() {
        if (this.y < 0) {
            this.y = 0;
            this.v = 0;
        }
        if (this.y > HEIGHT - this.h) {
            this.y = HEIGHT - this.h;
            this.v = 0;
        }
    }
    
    collide(b) {
        var paddleSide = this.x < WIDTH / 2;
        if (paddleSide) {
            if (b.x - b.r < this.x + this.w) {
                if (b.y >= this.y && b.y <= this.y + this.h) {
                    // This paddle reflected the ball! score + 0.2
                    this.score += 1.0; // 0.4
                    if (b.v[0] < 30.0) {
                        b.v[0] *= -1.1;
                    } else {
                        b.v[0] *= -1.0;
                    }
                    return false;
                } else {
                    b.getNew();
                    return true;
                }
            }
        } else {
            if (b.x + b.r > this.x) {
                if (b.y >= this.y && b.y <= this.y + this.h) {
                    // This paddle reflected the ball! score + 0.2
                    this.score += 1.0; // 0.4
                    if (b.v[0] < 30.0) {
                        b.v[0] *= -1.1;
                    } else {
                        b.v[0] *= -1.0;
                    }
                    return false;
                } else {
                    b.getNew();
                    return true;
                }
            }
        }
    }
    
    think(b) {
        let inputs = [this.y, b.y];
        let outputs = this.brain.predict(inputs);
        
        if (outputs[0] > outputs[1] && outputs[0] > outputs[2]) {
            this.stop();
        } else if (outputs[1] > outputs[0] && outputs[1] > outputs[2]) {
            this.up();
        } else if (outputs[2] > outputs[0] && outputs[2] > outputs[1]) {
            this.down();
        } else if (outputs[0] === outputs[1]) {
            this.stop();
        } else if (outputs[1] === outputs[2]) {
            this.up();
        } else if (outputs[0] === outputs[2]) {
            this.down();
        } else {
            this.stop();
        }
        
        // if (outputs[0] < outputs[1]) {
        //     this.up();
        // } else if (outputs[0] > outputs[1]) {
        //     this.down();
        // } else {
        //     this.stop();
        // }
    }
}