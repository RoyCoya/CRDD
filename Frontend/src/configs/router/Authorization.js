// case base routes
import UserAuthorization from '@/apps/HomePage/UserAuthorization/UserAuthorization.vue';
// import CaseSearchResults from '@/apps/CaseBase/SearchResults/SearchResults.vue';


export const routes_UserAuthorization = [{
    path: '/login/',
    component: UserAuthorization,
    name: 'HomePage_login',
},
];

export default routes_UserAuthorization;
