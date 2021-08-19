import './Nav.css'
import React from 'react'
import { Link } from 'react-router-dom'

export default props =>
    <aside className="menu-area">
        <nav className="menu">
            {/* Refatorar (Criar componente) (tipo o header) */}
            <Link to="/">
                <i className="fa fa-home"></i> Início
            </Link>
            <Link to="/score">
                <i className="fa fa-search"></i> Score
            </Link>
            <Link to="/logout">
                <i className="fa fa-power-off"></i> Logout
            </Link>    
        </nav>
    </aside>