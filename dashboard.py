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
# | Last update..: May 27th, 2025
# | WhatIs.......: Dashboard - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------


# ------------------------- Libraries -------------------------
# Database
import database

# ------------------------- Classes -------------------------
class Dashboard:
    def __init__(self, session):
        self.session = session

        db = database.MariaDB()

        user_data = db.select(f"""
            SELECT
                A.idmucuser, A.userkind, A.email, A.firstname, A.lastName, A.title, A.specialty
            FROM
                mucuser A
                INNER JOIN musession B ON A.idmucuser = B.idmucuser
            WHERE
                B.sessionnumber = '{self.session}'
        """)

        self.idmucuser = user_data[0][0]
        self.userkind = user_data[0][1]
        self.email = user_data[0][2]
        self.name = user_data[0][3]
        self.lastname = user_data[0][4]
        self.title = user_data[0][5]
        self.specialty = user_data[0][6]

        user_articles = db.select(f"""
            SELECT
                title
            FROM
                mucarticle
            WHERE
                author = {self.idmucuser};
            """)

        print(f"user_articles: {enumerate(user_articles)}")

        self.articles = ["Artículo 1", "Artículo 2",  "Artículo 3"]
        self.evaluations = ["Evaluación 1", "Evaluación 2", "Evaluación 3"]