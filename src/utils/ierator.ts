export class Iterator {
    private input: Array<unknown>;
    private pointer: number;
    private max: number;

    static from(input: Array<unknown>): Iterator {
        return new this([...input]);
    }

    constructor(input: Array<unknown>) {
        this.input = input;
        this.pointer = 0;
        this.max = input.length;
    }

    next(): unknown {
        const result = this.input.pop();
        this.max = this.input.length;
        return result;
    }

    sizeHint(): number {
        return this.input.length;
    }

    peekable(): this | null {
        if (typeof(this.input[this.pointer + 1]) === 'undefined') return null;
        return this; 
    }

    peek(): unknown | null {
        if (typeof(this.input[this.pointer + 1]) === 'undefined') return null;
        return this.input[this.pointer + 1];
    }

    skip(n: number): this {
        this.pointer =+ n; 
        return this;
    }

    flatten(n = 1): this {
        this.input = this.input.flat(n)
        return this;
    }
}