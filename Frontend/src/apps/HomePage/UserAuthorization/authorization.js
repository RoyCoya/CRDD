import axios from 'axios';
import backend from "@/configs/api/backend";

const api = backend.api_authorization

/* 
    Internal functions
*/

/* 
    External functions
*/

export const login = async (username, password) => {
    try {
        let response = await axios.post(api.login, {
            "username": username,
            "password": password
        });
        return { "status": response.status, "data": response.data.data };
    } catch (error) {
        return backend.errorReturn(error)
    }
}