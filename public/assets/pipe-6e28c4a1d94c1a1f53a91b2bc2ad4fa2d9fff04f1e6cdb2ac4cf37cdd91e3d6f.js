/* global random, height, width, fill, rect, translate */


class Pipe {
    constructor() {
        this.spacing = 175;
        this.top = random(height / 6, 2 / 3 * height);
        this.bottom = height - (this.top + this.spacing);
        
        //this.top = random(height / 6, height / 2.5);
        //this.bottom = random(height / 6, height / 2.5);

        this.x = width;
        this.w = 80;
        this.speed = 3;

        this.passed = false;
        this.highlight = false;
    }
    
    hits(bird) {
        if (bird.y < this.top || bird.y > height - this.bottom) {
            if (bird.x > this.x && bird.x < (this.x + this.w)) {
                this.highlight = true;
                return true;
            }
        }
        this.highlight = false;
        return false;
    }
    
    //this function is used to calculate scores and checks if we've went through the pipes
    pass(bird) {
        if (bird.x > this.x && !this.passed) {
            this.passed = true;
            return true;
        }
        return false;
    }
    
    show() {
        fill(255);
        
        if (this.highlight) {
            fill(255, 0, 0);
        }
        
        rect(this.x, 0, this.w, this.top);
        rect(this.x, height - this.bottom, this.w, this.bottom);
    }
    
    update() {
        this.x -= this.speed;
    }
    
    offscreen() {
        return this.x < -this.w;
    }
}
;
