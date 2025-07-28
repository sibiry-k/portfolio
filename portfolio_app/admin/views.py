from flask import flash, redirect, request, url_for
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('main.login', next=request.url))
        else:
            flash('У вас нет прав для доступа к этой странице')
            return redirect(url_for('main.index'))


class ProjectView(ModelView):
    form_excluded_columns = []
    form_columns = [
        'title',
        'description',
        'stack',
        'role',
        'tasks',
    ]
