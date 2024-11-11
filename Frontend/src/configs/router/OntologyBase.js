// ontology base routes
import OntologyBase from '@/apps/OntologyBase/OntologyBase.vue';
import OntologySearchResults from '@/apps/OntologyBase/SearchResults/SearchResults.vue';
import ConceptDetails from '@/apps/OntologyBase/ConceptDetails/ConceptDetails.vue';

export const routes_OntologyBase = [{
    path: '/ontology/',
    component: OntologyBase,
    name: 'Ontology_OntologyBase',
  },
  {
    path: '/ontology/concepts/',
    component: OntologySearchResults,
    name: 'Ontology_SearchResults',
    meta: { requiresAuth: true },
  },
  {
    path: '/ontology/concepts/:id',
    component: ConceptDetails,
    name: 'Ontology_Details',
  },
  ];

export default routes_OntologyBase;