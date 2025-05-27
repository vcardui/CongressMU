# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: May 6th, 2025
# | Last update..: May 26th, 2025
# | WhatIs.......: Dashboard - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------


# ------------------------- Libraries -------------------------


# ------------------------- Classes -------------------------
class Dashboard:
    def __init__(self, session):
        self.session = session

        self.idmucuser = ""
        self.userkind = ""
        self.email = "vanessa@reteguin.com"
        self.password = "aabb$12345678"
        self.titleOptions = 0
        self.specialty = "Dormir"

        self.articles = ["Artículo 1", "Artículo 2", "Artículo 3"]
        self.evaluations = ["Evaluación 1", "Evaluación 2", "Evaluación 3"]