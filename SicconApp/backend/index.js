const app = require('express')()
const consign = require('consign')

consign()
    .include('./config/passport.js')
    .then('./config/middlewares.js')
    .then('./api')
    .then('./config/routes.js')
    .into(app)

app.listen(5010, () => {
    console.log("Running on 5010 ...")
})
