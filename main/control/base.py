from flask import make_response, render_template

from auth import auth
from flask_restful import Resource
from model import BaseCategory


def base_auth_response(template, **kwargs):
	cats, _ = BaseCategory.get_dbs()
	user_db = auth.current_user_db()
	return make_response(render_template(template, menu=cats, user_db=user_db, **kwargs))
