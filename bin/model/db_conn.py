import sqlite3
from datetime import datetime


class Connection:
    topping_type = {
        '攻擊': 0,
        '防禦': 1,
        '體力': 2,
        '攻速': 3,
        '暴擊': 4,
        '冷卻': 5,
        '傷抗': 6,
        '暴抗': 7,
        '增益': 8,
        '減益': 9,
    }

    def __init__(self):
        self.con = sqlite3.connect('cookie_topping.db')

    def get_all_toppings(self):
        cur_obj = self.con.cursor()

        cur_obj.execute("SELECT * FROM toppings")
        for row in cur_obj.fetchall():
            print(row)

    def import_toppings(self, data_list):
        cur_obj = self.con.cursor()

        for data in data_list:
            print(data)
            cur_obj.execute(f"INSERT INTO toppings(type,ATK,DEF,HP,SPD,CRIT,COOL,D_RESIST,C_RESIST,BUFF,DEBUFF) VALUES "
                            f"({self.topping_type[data[0]]}, {data[1] if data[1] else 0}, "
                            f"{data[2] if data[2] else 0}, {data[3] if data[3] else 0}, "
                            f"{data[4] if data[4] else 0}, {data[5] if data[5] else 0}, "
                            f"{data[6] if data[6] else 0}, {data[7] if data[7] else 0}, "
                            f"{data[8] if data[8] else 0}, {data[9] if data[9] else 0}, "
                            f"{data[10] if data[10] else 0})")

        self.con.commit()

    def add_toppings(self, data):
        cur_obj = self.con.cursor()
        cur_obj.execute(f"INSERT INTO toppings(type,ATK,DEF,HP,SPD,CRIT,COOL,D_RESIST,C_RESIST,BUFF,DEBUFF) VALUES "
                        f"({data[0]}, {data[1] if data[1] else 0}, {data[2] if data[2] else 0}, "
                        f"{data[3] if data[3] else 0}, {data[4] if data[4] else 0}, "
                        f"{data[5] if data[5] else 0}, {data[6] if data[6] else 0}, "
                        f"{data[7] if data[7] else 0}, {data[8] if data[8] else 0}, "
                        f"{data[9] if data[9] else 0}, {data[10] if data[10] else 0})")
        self.con.commit()

    def search_toppings(self, condition_dict):
        cur_obj = self.con.cursor()

        conditions = []
        for key, value in condition_dict.items():
            conditions.append(f"{key} = {value}")

        cur_obj.execute(f"SELECT * FROM toppings WHERE {' AND '.join(conditions)}")
        return cur_obj.fetchall()

    def fuzzy_search_toppings(self, condition_list):
        cur_obj = self.con.cursor()

        conditions = []
        for condition_dict in condition_list:
            conditions.append(f"{condition_dict['key']} {condition_dict['operator']} {condition_dict['value']}")

        print(f"SELECT * FROM toppings WHERE {' AND '.join(conditions)}")

        cur_obj.execute(f"SELECT * FROM toppings WHERE {' AND '.join(conditions)}")
        return cur_obj.fetchall()

    def add_cookie(self, cookie_name, cool):
        cur_obj = self.con.cursor()

        cur_obj.execute(f"INSERT INTO cookies(cookie_name,cool_time) VALUES('{cookie_name}', {cool})")
        cookie_id = cur_obj.lastrowid
        for num in range(3):
            for pos in range(5):
                cur_obj.execute(f"INSERT INTO cookies(cookie_id,part_num,part_pos,is_lock) VALUES({cookie_id} ,"
                                f"{num}, {pos}, '{False}')")
        self.con.commit()

    def get_all_cookies(self):
        cur_obj = self.con.cursor()

        cur_obj.execute("SELECT * FROM cookies")
        for row in cur_obj.fetchall():
            print(row)

    def get_cookie_desc(self, id):
        cur_obj = self.con.cursor()

        cur_obj.execute(f"SELECT desc FROM cookies WHERE id = {id}")
        row = cur_obj.fetchone()

        return row[0] if row[0] else ''

    def add_record(self, top_id, raw_cookie_id, new_cookie_id):
        cur_obj = self.con.cursor()

        raw_desc = self.get_cookie_desc(raw_cookie_id)
        new_desc = self.get_cookie_desc(new_cookie_id)

        cur_obj.execute(f"INSERT INTO records VALUES({top_id}, {raw_cookie_id}, '{raw_desc}', {new_cookie_id}, "
                        f"'{new_desc}', {int(datetime.now().timestamp())})")
        self.con.commit()

    def delete_record(self, top_id, modify_time):
        cur_obj = self.con.cursor()

        cur_obj.execute(f"DELETE FROM records WHERE top_id = {top_id} AND modify_time = {modify_time}")

        self.con.commit()

    def get_topping_records(self, top_id):
        cur_obj = self.con.cursor()

        cur_obj.execute(f"SELECT * from records WHERE top_id = {top_id} ORDER BY modify_time DESC")
        return cur_obj.fetchall()

    def get_records(self):
        cur_obj = self.con.cursor()

        cur_obj.execute("SELECT * FROM records")
        for row in cur_obj.fetchall():
            print(row)

    def init_color(self):
        cur_obj = self.con.cursor()
        color_dict = {
            0: 'e6b8af',
            1: 'ffffff',
            2: 'ffffff',
            3: 'ffffff',
            4: 'ffe599',
            5: 'd5a6bd',
            6: 'f9cb9c',
            7: 'ffffff',
            8: 'ffffff',
            9: 'ffffff',
        }

        for top_type, color in color_dict.items():
            cur_obj.execute(f"INSERT OR IGNORE INTO color VALUES('{top_type}', '{color}')")
        self.con.commit()

    def get_color_setting(self):
        cur_obj = self.con.cursor()

        cur_obj.execute("SELECT * FROM color")
        for row in cur_obj.fetchall():
            print(row)

    def set_color(self, top_type, color):
        cur_obj = self.con.cursor()

        cur_obj.execute(f"UPDATE color SET color = '{color}' WHERE top_type = {top_type}")


