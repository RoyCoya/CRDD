// case base routes
import CaseBase from '@/apps/CaseBase/CaseBase.vue';
// import CaseSearchResults from '@/apps/CaseBase/SearchResults/SearchResults.vue';
import CaseDetails from '@/apps/CaseBase/CaseDetails/CaseDetails.vue';

export const routes_CaseBase = [{
    path: '/case/',
    component: CaseBase,
    name: 'Case_CaseBase',
},
// {
//   path: '/case/search/',
//   component: CaseSearchReults,
//   name: 'Case_SearchResults',
// },
{
    path: '/case/details/:id/',
    component: CaseDetails,
    name: 'Case_Details',
},
];

export default routes_CaseBase;
