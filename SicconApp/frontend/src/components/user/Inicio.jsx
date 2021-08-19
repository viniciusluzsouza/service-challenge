import React, { Component } from 'react'
import Main from '../templates/Main'
import api from '../../services/api'

const headerProps = {
    icon: 'home',
    title: ' Consulta CPF',
    subtitle: 'Página para consulta de cadastro!'
}

const initialState = {
    cpf: "",
    registryData: {},
    registryDebts: [],
    error: ""
}

export default class Registry extends Component {
    state = { ...initialState }

    clear() {
        this.setState({registryData: initialState.registryData})
        this.setState({registryDebts: initialState.registryDebts})
    }

    getRegistry() {
        api.get(`/registryinfo?cpf=${this.state.cpf}`).then(resp => {
            this.setState({error: ""})
            this.setState({registryData: resp.data.data})
            this.setState({registryDebts: resp.data.data.debts})
            this.renderRegistry()
            this.renderRegistryDebtsTable()
        }).catch(error => {
            this.clear()
            if (error.response && error.response.status === 404) {
                this.setState({error: "CPF não encontrado!"})
            } else {
                this.setState({error: "Erro no servidor!"})
            }
        })
    }

    updateField(event) {
        const cpf = event.target.value
        this.setState({cpf})
    }

    renderError() {
        if (!this.state.error || this.state.error === "")
            return

        return (
            <p style={{color:'red'}}color="red"><b>{this.state.error}</b></p>
        )
    }

    renderForm() {
        return (
            <div className="form">
                <div className="row">
                    <div className="col-4 col-md-4">
                        <div className="form-group">
                            <label>Informe o CPF que deseja consultar</label>
                            <input type="text" className="form-control"
                                name="cpf"
                                value={this.state.cpf}
                                onChange={e => this.updateField(e)}
                                placeholder="Digite o CPF ..." />
                        </div>
                    </div>
                    <div className="d-inline-flex align-items-end">
                        <button className="btn btn-primary" style={{marginBottom: 16}}
                            onClick={e => this.getRegistry(e)}>
                            Consultar
                        </button>
                    </div>
                </div>
            </div>
        )
    }

    renderRegistry() {
        if (!this.state.registryData.cpf)
            return null
            
        return (
            <div>
                <h3>Informações do Cadastro</h3>
                <table className="table mt-4">
                    <thead>
                        <tr>
                            <th>Nome</th>
                            <th>CPF</th>
                            <th>Endereco</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{this.state.registryData.name}</td>
                            <td>{this.state.registryData.cpf}</td>
                            <td>{this.state.registryData.address}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        )
    }

    renderRegistryDebts() {
        return this.state.registryDebts.map(debt => {
            return (
                <tr>
                    <td>R$ {debt.value}</td>
                    <td>{debt.months}</td>
                    <td>R$ {debt.value / debt.months}</td>
                </tr>
            )
        })
    }

    renderRegistryDebtsTable() {
        if (!this.state.registryData.cpf)
            return null
        
        return (
            <div>
                <h3>Lista de dívidas</h3>
                <table className="table mt-4">
                    <thead>
                        <tr>
                            <th>Valor</th>
                            <th>Parcelas</th>
                            <th>Valor por parcela</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.renderRegistryDebts()}
                    </tbody>
                </table>
            </div>
        )
    }

    render() {
        return (
            <Main {...headerProps}>
                {this.renderForm()}
                {this.renderError()}
                {this.renderRegistry()}
                {this.renderRegistryDebtsTable()}
            </Main>
        )
    }
}