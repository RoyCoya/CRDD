import axios from 'axios';
import backend from "@/configs/backend";
import { param } from 'jquery';

// TODO: 用户偏好
const languages = [
    'Chinese','English'
]
const definition_sets = ['Biomedical Informatics Ontology System']
const urls = backend.api_ontology.concept

/* 
    Internal functions
*/

export const fetchData = async (conceptFunction, concept, params) => {
    try {
        let response = await axios.get(conceptFunction(concept.element_id), { params: params });
        return { "status": response.status, "data": response.data.data };
    } catch (error) {
        return backend.errorReturn(error);
    }
}

/* 
    External functions
*/


// sort terms by preference
// TODO: add definition set preference
export const sortTerms = (terms) => {
    return terms.sort((a, b) => {
        const aIndex = Math.min(...a.languages.map(lang => languages.indexOf(lang)).filter(index => index !== -1));
        const bIndex = Math.min(...b.languages.map(lang => languages.indexOf(lang)).filter(index => index !== -1));
        if (aIndex !== undefined && bIndex !== undefined) {
            return aIndex - bIndex;
        }
        if (aIndex !== undefined) return -1;
        if (bIndex !== undefined) return 1;
        return 0;
    })
}

export const search = async (representation) => {
    try {
        let response = await axios.get(urls.search, {
            params: {
                "representation": representation,
                "limit": 20
            }
        });
        return { "status": response.status, "data": response.data.data };
    } catch (error) {
        return backend.errorReturn(error)
    }
}

export const retrieve = async (element_id) => {
    try {
        let response = await axios.get(urls.retrieve(element_id));
        return { "status": response.status, "data": response.data.data };
    } catch (error) {
        return backend.errorReturn(error)
    }
}

export const getRepresentation = async (concept, language = 'English') => {
    return fetchData(urls.representations, concept, {"limit": 1, "language": language });
}

export const getRepresentations = async (concept, params) => {
    return fetchData(urls.representations, concept, params);
};

export const getPreferTerms = async (concept, params) => {
    return fetchData(urls.prefer_terms, concept, params);
};

// get prefer terms as a list with only terms' value
// TODO: prefer language add-on term

export const getPreferTermList = async (concept, params) => {
    let response = await getPreferTerms(concept, params);
    switch (response.status) {
        case 200:
            {
                let terms = response.data
                if (terms.every(obj => !obj.languages.includes('Chinese'))) {
                    let cn_response = await getRepresentation(concept, "Chinese")
                    // TODO: 当prefer term数据越来越多后改成直接替换而非插入（或者根据语言偏好顺序来改？没想好）
                    if (cn_response.status == 200) {
                        terms.splice(0, 0, cn_response.data[0])
                    }
                }
                return terms.map(term => term.value);
            }
        case 404:
            {
                let cn_response = await getRepresentation(concept, "Chinese")

                if (cn_response.status == 404) {
                    cn_response = await getRepresentation(concept)
                }
                return [cn_response.data[0].value]
            }
        default: return ["暂无表述"]
    }
}

export const getSynonyms = async (concept, params) => {
    return fetchData(urls.synonyms, concept, params);
};

export const getRelations = async (concept, params) => {
    return fetchData(urls.relations, concept, params);
};



export default 'Concept functions';