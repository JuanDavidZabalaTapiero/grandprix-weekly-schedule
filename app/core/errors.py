from flask import render_template


def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(error):
        print(error)
        return render_template("500.html")
