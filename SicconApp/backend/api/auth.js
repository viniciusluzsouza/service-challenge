const { authSecret } = require('../env')
const jwt = require('jwt-simple')

module.exports = app => {
    const signin = async (req, res) => {
        console.log("User login ... ")
        email = req.body.email
        password = req.body.password

        if (!email || !password) {
            return res.status(400).send('No user and password found')
        }

        if (email != "admin" || password != "admin")
            return res.status(400).send('Invalid user or password!')

        const now = Math.floor(Date.now() / 1000)

        const payload = {
            name: "Admin",
            email: email,
            iat: now,
            exp: now + (60 * 60 * 24 * 3)
        }

        res.json({
            ...payload,
            token: jwt.encode(payload, authSecret)
        })
    }

    const validateToken = async (req, res) => {
        const userData = req.body || null
        try {
            if(userData) {
                const token = jwt.decode(userData.token, authSecret)
                if(new Date(token.exp * 1000) > new Date()) {
                    return res.send(true)
                }
            }
        } catch(e) {
            console.log("Problem with token validation!")
        }

        res.send(false)
    }

    return { signin, validateToken }
}