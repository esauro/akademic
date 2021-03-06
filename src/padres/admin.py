# -*- coding: utf-8 -*-
"""
    Akademic: Herramienta para el control del alumnado en centros escolares.

    Copyright (C) 2010  Galotecnia Redes Sistemas y Servicios S.L.L. <info@galotecnia.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django.contrib import admin
from models import Padre
from docencia.admin import BaseAdmin

class PadreAdmin(BaseAdmin):
    search_fields = ('persona__nombre', 'persona__apellidos', 'persona__documento_identificacion',)
    related_search_fields = {
        'persona':  ('nombre', 'apellidos', 'documento_identificacion',)
    }

admin.site.register(Padre, PadreAdmin)

