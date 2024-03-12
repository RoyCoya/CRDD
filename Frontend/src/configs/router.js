// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

// import components
import Home from '@/apps/HomePage/HomePage.vue';

import OntologyBase from '@/apps/OntologyBase/OntologyBase.vue';
import OntologySearchResults from '@/apps/OntologyBase/SearchResults/SearchResults.vue';
import OntologyDetails from '@/apps/OntologyBase/OntologyDetails/OntologyDetails.vue';

import CaseBase from '@/apps/CaseBase/CaseBase.vue';
// import CaseSearchResults from '@/apps/CaseBase/SearchResults/SearchResults.vue';
import CaseDetails from '@/apps/CaseBase/CaseDetails/CaseDetails.vue';

// homepage routes
const routes_HomePage = [{
  path: '/',
  component: Home,
  name: 'HomePage',
},
];

// ontology base routes
const routes_OntologyBase = [{
  path: '/ontology/',
  component: OntologyBase,
  name: 'Ontology_OntologyBase',
},
{
  path: '/ontology/search',
  component: OntologySearchResults,
  name: 'Ontology_SearchResults',
},
{
  path: '/ontology/details/:id',
  component: OntologyDetails,
  name: 'Ontology_Details',
},
];

// case base routes
const routes_CaseBase = [{
  path: '/case/',
  component: CaseBase,
  name: 'Case_CaseBase',
},
// {
//   path: '/case/search',
//   component: CaseSearchReults,
//   name: 'Case_SearchResults',
// },
{
  path: '/case/details/:id',
  component: CaseDetails,
  name: 'Case_Details',
},
];

// concatenate all routes
export const routes = [
  ...routes_HomePage,
  ...routes_OntologyBase,
  ...routes_CaseBase,
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
