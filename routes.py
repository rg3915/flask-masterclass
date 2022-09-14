def init_app(home):
    @home.route('/')
    def index():
        return "Olá, Flask!"
