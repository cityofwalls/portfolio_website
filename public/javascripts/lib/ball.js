/* global WIDTH HEIGHT DIAMETER fill ellipse Math */

class Ball {
    constructor() {
        this.getNew();
    }
    
    getNew() {
        this.x = WIDTH / 2;
        this.y = HEIGHT / 2;
        this.r = DIAMETER / 2;
        this.v = [0, 0];
        this.speed = 7;
        
        if (Math.random(1) < 0.5) {
            this.v[0] = this.speed;
        } else {
            this.v[0] = -this.speed;
        }
        
        if (Math.random(1) < 0.5) {
            this.v[1] = 3 + Math.floor(Math.random() * 3);
        } else {
            this.v[1] = -3 - Math.floor(Math.random() * 3);
        }
    }
    
    show() {
        fill(255);
        ellipse(this.x, this.y, DIAMETER);
    }
    
    update() {
        this.x += this.v[0];
        this.y += this.v[1];
    }
    
    collide() {
        if (this.y - this.r < 0) {
            this.v[1] *= -1;
        } else if (this.y + this.r > HEIGHT) {
            this.v[1] *= -1;
        }
    }
}