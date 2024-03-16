// ontology base routes
import OntologyBase from '@/apps/OntologyBase/OntologyBase.vue';
import OntologySearchResults from '@/apps/OntologyBase/SearchResults/SearchResults.vue';
import OntologyDetails from '@/apps/OntologyBase/OntologyDetails/OntologyDetails.vue';

export const routes_OntologyBase = [{
    path: '/ontology/',
    component: OntologyBase,
    name: 'Ontology_OntologyBase',
  },
  {
    path: '/ontology/search/',
    component: OntologySearchResults,
    name: 'Ontology_SearchResults',
  },
  {
    path: '/ontology/details/:id/',
    component: OntologyDetails,
    name: 'Ontology_Details',
  },
  ];

export default routes_OntologyBase;