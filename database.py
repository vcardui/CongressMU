# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: May 26th, 2025
# | Last update..: May 26th, 2025
# | WhatIs.......: MariaDB - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# How to connect Python programs to MariaDB: https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
# Flask with MariaDB: A Comprehensive Guide: https://readmedium.com/flask-with-mariadb-a-comprehensive-guide-0be504b0970f

# ------------------------- Libraries -------------------------


# Integrate MariaDB to app
import MySQLdb

# ------------------------- Classes -------------------------
class MariaDB:
    def __init__(self):

        # Initialize MySQL
        self.mysql = MySQLdb.connect(host='localhost',
                                user='root',
                                passwd='97cb42K3a8yef!ds)/6#)VQV',
                                db='flask_db')

        self.cursor = self.mysql.cursor()

    def insert(self, insert_cmd):
        try:
            self.cursor.execute(insert_cmd)
            self.mysql.commit()
            return True
        except Exception as e:
            print("Problem inserting into db: " + str(e))
            return False

    def select(self, select_cmd):
        try:
            self.cursor.execute(select_cmd)
            return self.cursor.fetchall()

        except Exception as e:
            print("Problem selecting into db: " + str(e))
            return False