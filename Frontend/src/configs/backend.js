// backend apis
const backendBaseUrl = "http://localhost:8000/"; // change to your backend address
// top application
const Ontology = backendBaseUrl + "ontology";
const Case = backendBaseUrl + "case";

const api_ontology = {
  "concept": {
    "search": `${Ontology}/concepts/`,
    "retrieve": (element_id) => `${Ontology}/concepts/${element_id}`,
    "representations": (element_id) => `${Ontology}/concepts/${element_id}/representations/`,
    "prefer_terms": (element_id) => `${Ontology}/concepts/${element_id}/prefer_terms/`,
    "synonyms": (element_id) => `${Ontology}/concepts/${element_id}/synonyms/`,
    "relations": (element_id) => `${Ontology}/concepts/${element_id}/relations/`,
  },
  "definition_set":{
    "retrieve": (element_id) => `${Ontology}/definition_sets/${element_id}`,
  }
}

const api_case = {
  "case": {
    "searchByID": null
  }
}

const errorReturn = (error) =>{
  return error.response ? 
  {"status": error.response.status, "data" : error.response.data} : 
  {"status": -1, "data" : {"message":"网络错误，无法请求服务器"}}
}

export default {
  backendBaseUrl,
  api_ontology,
  api_case,
  errorReturn,
};
