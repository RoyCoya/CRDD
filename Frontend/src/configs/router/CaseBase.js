// case base routes
import CaseBase from '@/apps/CaseBase/CaseBase.vue';
// import CaseSearchResults from '@/apps/CaseBase/SearchResults/SearchResults.vue';
import CaseDetails from '@/apps/CaseBase/CaseDetails/CaseDetails.vue';
import CaseView from '@/apps/CaseBase/CaseDetails/CaseView/CaseView.vue';
import InfoView from '@/apps/CaseBase/CaseDetails/CaseView/InfoView.vue';
import RelationView from '@/apps/CaseBase/CaseDetails/CaseView/RelationView.vue';
import TimelineView from '@/apps/CaseBase/CaseDetails/CaseView/TimelineView.vue';
import BodyView from '@/apps/CaseBase/CaseDetails/CaseView/BodyView.vue';
import CaseQuiz from '@/apps/CaseBase/CaseDetails/CaseQuiz/CaseQuiz.vue';
import CaseEdit from '@/apps/CaseBase/CaseDetails/CaseEdit/CaseEdit.vue';

const view = [{
    path: '/case/details/:id/view/info/',
    component: InfoView,
    name: 'Case_Details_View_Info',
},
{
    path: '/case/details/:id/view/relation/',
    component:RelationView,
    name: 'Case_Details_View_Relation',
},
{
    path: '/case/details/:id/view/timeline/',
    component:TimelineView,
    name: 'Case_Details_View_Timeline',
},
{
    path: '/case/details/:id/view/body/',
    component:BodyView,
    name: 'Case_Details_View_Body',
},
]

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
{
    path: '/case/details/:id/view/',
    component: CaseView,
    name: 'Case_Details_View',
},
...view,
{
    path: '/case/details/:id/quiz/',
    component: CaseQuiz,
    name: 'Case_Details_Quiz',
},
{
    path: '/case/details/:id/edit/',
    component: CaseEdit,
    name: 'Case_Details_Edit',
},
];

export default routes_CaseBase;
