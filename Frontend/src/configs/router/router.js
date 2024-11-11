// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import { jwtDecode } from 'jwt-decode';

// import components
import routes_TestPage from './Test';
import routes_HomePage from './HomePage';
import routes_CaseBase from './CaseBase';
import routes_OntologyBase from './OntologyBase';
import routes_UserAuthorization from './Authorization';

// concatenate all routes
export const routes = [
    ...routes_TestPage,
    ...routes_UserAuthorization,
    ...routes_HomePage,
    ...routes_OntologyBase,
    ...routes_CaseBase,
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

// auth check
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('accessToken');
    if (to.meta.requiresAuth) {
        if (!token) {
            next({
                path: '/login',
                query: { redirect: to.fullPath }
            });
        } else {
            try {
                const decodedToken = jwtDecode(token);
                const isExpired = decodedToken.exp * 1000 < Date.now();
                if (isExpired) {
                    alert("登录已过期，请重新登录。");
                    next({
                        path: '/login',
                        query: { redirect: to.fullPath }
                    });
                } else {
                    next();
                }
            } catch (error) {
                console.error("令牌解析错误：", error);
                next('/login');
            }
        }
    } else {
        next();
    }
});

export default router;
