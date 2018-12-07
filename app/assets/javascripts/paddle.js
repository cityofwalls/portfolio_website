/* global WIDTH HEIGHT PAD_WIDTH rect fill */

class Paddle {
    constructor(x) {
        this.w = PAD_WIDTH;
        this.h = HEIGHT / 5;
        this.x = x;
        this.y = HEIGHT / 2 - (this.h / 2);
        this.v = 0;
        this.a = 3;
    }
    
    show() {
        fill(255);
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
                    b.v[0] *= -1.1;
                } else {
                    b.getNew();
                }
            }
        } else {
            if (b.x + b.r > this.x) {
                if (b.y >= this.y && b.y <= this.y + this.h) {
                    b.v[0] *= -1.1;
                } else {
                    b.getNew();
                }
            }
        }
    }
}