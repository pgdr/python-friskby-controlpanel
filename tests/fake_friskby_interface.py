# -*- coding: utf-8 -*-
"""
    Friskby Interface

    In interface between Friskby Control panel, and everything required from
    the rest of the friskby universe.

    Licence
    =======
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""


class FakeFriskbyInterface():

    def __init__(self):
        self.fails = False

    def download_and_save_config(self, url, filename):
        if self.fails:
            raise ValueError("Was asked to fail.")