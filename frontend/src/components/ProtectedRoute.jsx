import React from 'react';
import {Navigate} from 'react-router-dom';

function ProtectedRoute({children}){
     return sessionStorage.getItem('access_token') ? children : <Navigate to='/' />

}
export default ProtectedRoute;