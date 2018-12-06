/* global WIDTH HEIGHT fill ellipse */


class Ball {
    constructor() {
        this.x = WIDTH / 2;
        this.y = HEIGHT / 2;
        this.r = 30;
        this.v = [0, 0];
        
        if (Math.random(1) < 0.5) {
            this.v[0] = 2;
        } else {
            this.v[0] = -2;
        }
        
        if (Math.random(1) < 0.5) {
            this.v[1] = 2;
        } else {
            this.v[1] = -2;
        }
    }
    
    show() {
        fill(255);
        ellipse(this.x, this.y, this.r);
    }
    
    update() {
        this.x += this.v[0];
        this.y += this.v[1];
    }
    
    collide() {
        if (this.y - (this.r / 2) < 0) {
            this.v[1] *= -1;
        } else if (this.y + (this.r / 2) > HEIGHT) {
            this.v[1] *= -1;
        }
    }
}
;
