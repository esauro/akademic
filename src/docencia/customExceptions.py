# -*- encoding: utf-8 -*-
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

class UnauthorizedAccess(Exception):
	"""
		Excepción generada cuando un usuario intenta acceder a un método
		(normalmente una vista) que no le está permitido.
	"""
	pass

class FatalError(Exception):
	"""
		Excepción generada cuando un usuario intenta acceder a métodos sin pasar
		los argumentos correctos.
	"""	
	pass
