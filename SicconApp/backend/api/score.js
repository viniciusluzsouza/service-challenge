const url = require('url')
const http = require('http')

module.exports = app => {
    const get = async (req, res) => {
        cpf = url.parse(req.url, true).query.cpf
        
        if (!cpf) res.status(400).send("No CPF informed!")

        const options = {
            hostname: 'score-calculator',
            port: 5003,
            path: `/credit_calc?cpf=${cpf}`,
            method: 'GET'
        }

        const newreq = http.request(options, result => {
            console.log(`Get score for CPF ${cpf} [ResultCode: ${result.statusCode}]`)
            if (result.statusCode === 200) {
                result.on('data', d => {
                    res.json({data: JSON.parse(d.toString())})
                })
            } else {
                res.status(result.statusCode).send()
            }
        })

        newreq.on('error', error => {
            res.status(500).send()
        })

        newreq.end()
    }

    return { get }
}
