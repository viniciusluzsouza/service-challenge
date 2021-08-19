import React from 'react'
import { Switch, Route, Redirect } from 'react-router'

import Home from '../components/home/Home'
import PaginaLogin from '../components/login/PaginaLogin'

export default props =>
    <Switch>
        <Route exact path='/' component={PaginaLogin} />
        <Route path='/login' component={PaginaLogin} />
        <Route path='/home' component={Home} />
        <Redirect from='*' to='/' />
    </Switch>