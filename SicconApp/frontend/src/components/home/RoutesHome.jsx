import React from 'react'
import { Switch, Route, Redirect } from 'react-router'

import Inicio from '../user/Inicio'
import Score from '../user/Score'
import PaginaLogin from '../login/PaginaLogin'

export default props =>
    <Switch>
        <Route exact path='/' component={Inicio} />
        <Route path='/score' component={Score}/>
        <Route path='/logout' component={PaginaLogin}/>
        <Redirect from='*' to='/' />
    </Switch>