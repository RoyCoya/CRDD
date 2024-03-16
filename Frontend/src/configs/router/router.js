// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

// import components
import routes_HomePage from './HomePage';
import routes_CaseBase from './CaseBase';
import routes_OntologyBase from './OntologyBase';

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
