import React, { Component } from 'react'
import api from '../../services/api'
import { login, logout } from '../../services/auth'
import './PaginaLogin.css'
import logo from '../../assets/imgs/logo.png'

const initialState = {
    email: '',
    password: '',
    error: null
}

export default class PaginaLogin extends Component {

    state = { ...initialState }

    makeLogin = async e => {
        e.preventDefault();
        const { email, password } = this.state;
        if (!email || !password) {
            this.setState({ error: "Informe e-mail e senha para efetuar o login" });
        } else {
          try {
            const response = await api.post("/signin", { email, password });
            login(response.data.token);
            this.props.history.push("/home");
          } catch (err) {
            this.setState({
              error: "Login não pôde ser realizado. Verifique suas credenciais."
            });
          }
        }
      };

    renderLogin() {
        return (
            <div className="body text-center">
                <div className="form">
                    <div className="row">
                        <img src={logo} alt="" className="mb-4" width="600" height="230" />
                    </div>
                    <div className="row">
                        <div className="form-signin">
                            <h1 className="h3 mb-3 font-weight-normal">Faça o login</h1>
                            <input type="email" className="form-control"
                                placeholder="E-mail" name="email"
                                onChange={e => this.setState({ email: e.target.value })}
                                required autoFocus />
                            <input type="password" className="form-control"
                                placeholder="Senha" name="password"
                                onChange={e => this.setState({ password: e.target.value })}
                                required />
                            <button className="btn btn-lg btn-primary btn-block" type="submit"
                                onClick={e => this.makeLogin(e)}>Entrar</button>
                            {this.renderError()}
                            <p className="mt-5 mb-3 text-muted">&copy; 2019</p>
                        </div>
                    </div>
                </div>
            </div>

        )
    }

    trataProps() {
        if (this.props.history.action === "PUSH") {
            logout()
            window.location.reload()
        }
    }

    renderError() {
        if (this.state.error) {
            return (
                <div>
                    <p className="mt-5 mb-3 text-danger">{this.state.error}</p>
                </div>
            )
        }
    }

    render() {
        return (
            <main>
                {this.trataProps()}
                {this.renderLogin()}
            </main>
        )
    }
}