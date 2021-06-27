export function generator(): Uint8Array {
    const bytes: Array<number> = [];

    // ...

    const uint16 = new Uint16Array(bytes);
    return new Uint8Array(
        uint16.buffer,
        uint16.byteOffset,
        uint16.byteLength
    );
}