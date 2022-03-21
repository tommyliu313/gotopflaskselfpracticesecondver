@api.errorhandler(ValidationError)
def validation_error(e):
    return bad_request(e.args[0])
