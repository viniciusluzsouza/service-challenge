
module.exports = app => {
    app.post('/signin', app.api.auth.signin)
    app.route('/registryinfo').all(app.config.passport.authenticate()).get(app.api.registry.get)
    app.route('/score').all(app.config.passport.authenticate()).get(app.api.score.get)
}