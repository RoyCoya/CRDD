// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

// import components
import Home from '@/apps/HomePage/HomePage.vue';
import OntologyBase from '@/apps/OntologyBase/OntologyBase.vue';
import SearchResults from '@/apps/OntologyBase/SearchResults/SearchResults.vue';
import OntologyDetails from '@/apps/OntologyBase/OntologyDetails/OntologyDetails.vue';

// create routes
const routes_HomePage = [{
  path: '/',
  component: Home,
  name: 'HomePage',
},
];

const routes_OntologyBase = [{
  path: '/ontology/',
  component: OntologyBase,
  name: 'Ontology_OntologyBase',
},
{
  path: '/ontology/search',
  component: SearchResults,
  name: 'Ontology_SearchResults',
},
{
  path: '/ontology/details/:id',
  component: OntologyDetails,
  name: 'Ontology_Details',
},
];

// concatenate all routes
export const routes = [
  ...routes_HomePage,
  ...routes_OntologyBase,
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
