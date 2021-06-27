export namespace Ernaculere {
    interface Token {
        type: string;
        data: TokenData;
    }

    interface TokenData {
        value: string;
        index: number;
    }
}