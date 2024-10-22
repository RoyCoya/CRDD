import axios from 'axios';
import backend from "@/configs/backend";

const urls = backend.api_ontology.definition_set;

/* 
    Internal functions
*/

/* 
    External functions
*/

// retrieve definition set info by element id
export const retrieve = async (element_id) => {
    try {
        let response = await axios.get(urls.retrieve(element_id));
        return {"status":response.status, "data" : response.data.data};
    } catch (error) {
        return backend.errorReturn(error) 
    }
}

export const getName = async (element_id) => {
    return (await retrieve(element_id)).data[0].value
}

export default 'Definition set functions';
