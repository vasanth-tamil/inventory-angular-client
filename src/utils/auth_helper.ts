export const AuthHelper = {
    getToken: () => localStorage.getItem('token'),
    removeToken: () => localStorage.removeItem('token'),
    saveToken: (token: string) => localStorage.setItem('token', token),
    isAuthenticated: () => localStorage.getItem('token') !== null,
    getBarearHeader: () => {
        const token = AuthHelper.getToken();
        return token ? { 'Content-type': 'application/json', 'Authorization': `Bearer ${token}` } : {};
    } 
}