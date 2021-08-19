import React, { Component } from 'react'
import Main from '../templates/Main'
import api from '../../services/api'
import './Score.css'

const headerProps = {
    icon: 'search',
    title: ' Consulta Score',
    subtitle: 'Página para consulta de score de CPF!'
}

const initialState = {
    cpf: "",
    rate: null,
    scoreData: {}
}

export default class Score extends Component {
    state = { ...initialState }

    getScore() {
        api.get(`/score?cpf=${this.state.cpf}`).then(resp => {
            console.log(resp.data)
            this.setState({rate: resp.data.data.rate})
            this.setState({scoreData: resp.data.data.data})
            this.renderScore()
            this.renderIncomesTable()
            this.renderGoodsTable()
            this.renderLastCreditQuery()
            this.renderLastCreditCardPurchase()
        })
    }

    updateField(event) {
        const cpf = event.target.value
        this.setState({cpf})
    }

    renderNothing() {
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
                            onClick={e => this.getScore(e)}>
                            Consultar
                        </button>
                    </div>
                </div>
            </div>
        )
    }

    renderScore() {
        if (this.state.rate == null)
            return null
        
        return (
            <div className="col-3 col-md-3">
                <table className="table table-borderless">
                    <thead>
                        <tr>
                            <th>Score</th>
                            <th>Idade</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><h1>{this.state.rate}</h1></td>
                            <td><h1>{this.state.scoreData.age}</h1></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        )
    }

    renderIncomes() {
        return this.state.scoreData.incomes.map(income => {
            return (
                <tr>
                    <td>{income.type}</td>
                    <td>R$ {income.value}</td>
                    <td>{income.since}</td>
                </tr>
            )
        })
    }

    renderIncomesTable() {
        if (!this.state.scoreData.incomes)
            return null
            
        return (
            <div>
                <hr />
                <h3>Informações de Renda</h3>
                <table className="table mt-4">
                    <thead>
                        <tr>
                            <th>Tipo</th>
                            <th>Valor</th>
                            <th>Data Inicio</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.renderIncomes()}
                    </tbody>
                </table>
            </div>
        )
    }

    renderGoods() {
        return this.state.scoreData.goods.map(good => {
            return (
                <tr>
                    <td>{good.type}</td>
                    <td>R$ {good.value}</td>
                </tr>
            )
        })
    }

    renderGoodsTable() {
        if (!this.state.scoreData.incomes)
            return null
            
        return (
            <div class='mydiv'>
                <hr />
                <h3>Informações de Bens</h3>
                <table className="table mt-4">
                    <thead>
                        <tr>
                            <th>Tipo</th>
                            <th>Valor</th>
                        </tr>
                    </thead>
                    <tbody>
                        {this.renderGoods()}
                    </tbody>
                </table>
            </div>
        )
    }

    renderFinantialMovementTable() {
        if (!this.state.scoreData.financial_movement)
            return null
            
        return (
            <div class='mydiv'>
                <hr />
                <h3>Informações de Bens</h3>
                <table className="table mt-4">
                    <thead>
                        <tr>
                            <th>Entradas</th>
                            <th>Saídas</th>
                            <th>Saldo</th>
                            <th>Período</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>R$ {this.state.scoreData.financial_movement.inputs}</td>
                            <td>R$ {this.state.scoreData.financial_movement.outputs}</td>
                            <td>R$ {this.state.scoreData.financial_movement.inputs - this.state.scoreData.financial_movement.outputs}</td>
                            <td>{this.state.scoreData.financial_movement.from} - {this.state.scoreData.financial_movement.to}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        )
    }

    renderLastCreditCardPurchase() {
        if (!this.state.scoreData.last_credit_card_purchase)
            return null

        const months = this.state.scoreData.last_credit_card_purchase.months
        const value = this.state.scoreData.last_credit_card_purchase.value
        const datetime = this.state.scoreData.last_credit_card_purchase.datetime
        return (
            <div class='mydiv'>
                <hr />
                <h3>Dados da última compra com cartão de crédito:</h3>
                <p><b>Valor:</b> R$ {value}</p>
                <p><b>Parcelamento:</b> {months}</p>
                <p><b>Data/Hora:</b> {datetime}</p>
            </div>
        )
    }

    renderLastCreditQuery() {
        if (!this.state.scoreData.last_credit_query)
            return null

        const good = this.state.scoreData.last_credit_query.good
        const inst = this.state.scoreData.last_credit_query.institution
        const value = this.state.scoreData.last_credit_query.value
        const datetime = this.state.scoreData.last_credit_query.datetime
        return (
            <div class='mydiv'>
                <hr />
                <h3>Dados da última consulta de crédito:</h3>
                <p><b>Bem:</b> {good}</p>
                <p><b>Valor:</b> R$ {value}</p>
                <p><b>Instituição:</b> {inst}</p>
                <p><b>Data/Hora:</b> {datetime}</p>
            </div>
        )
    }

    render() {
        return (
            <Main {...headerProps}>
                {this.renderNothing()}
                {this.renderScore()}
                {this.renderIncomesTable()}
                {this.renderGoodsTable()}
                {this.renderFinantialMovementTable()}
                {this.renderLastCreditQuery()}
                {this.renderLastCreditCardPurchase()}
            </Main>
        )
    }
}