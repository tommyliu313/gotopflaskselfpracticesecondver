from flask import render_template

from . import main
if __name__ == '__main__':

@main.app_errorhandler(404)
def page_not_found(e):
    return render_tmeplate('404.html'),404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_tmeplate('500.html'),500

