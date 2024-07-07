export class ApiConstant {
    static baseUrl: string = 'http://localhost:5000';

    // authentication
    static signUp = `${this.baseUrl}/auth/sign-up`;
    static signIn = `${this.baseUrl}/auth/sign-in`;
    static signOut = `${this.baseUrl}/auth/sign-out`;
    
    // inventory
    static inventory = `${this.baseUrl}/inventory`;
} 