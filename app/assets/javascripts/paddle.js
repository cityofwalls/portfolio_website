/* global WIDTH HEIGHT PAD_WIDTH rect fill */

class Paddle {
    constructor(x) {
        this.w = PAD_WIDTH;
        this.h = HEIGHT / 5;
        this.x = x;
        this.y = HEIGHT / 2 - (this.h / 2);
        this.v = 0;
    }
    
    show() {
        fill(255);
        rect(this.x, this.y, this.w, this.h);
    }
    
    update() {
        this.y += this.v;
    }
    
    up() {
        this.v = -2;
    }
    
    down() {
        this.v = 2;
    }
    
    stop() {
        this.v = 0;
    }
}