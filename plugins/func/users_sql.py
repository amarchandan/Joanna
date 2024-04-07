# RANDOM GEN FUNCTION
def gcgenfunc(len=10):
  import string
  import random
  chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
  return ''.join(random.choice(chars) for _ in range(len))

# insert registration data
def insert_reg_data(user_id, username, antispam_time, reg_at, bot_id):
    import psycopg2
    conn = psycopg2.connect('postgres://joanna_xhp6_user:5PXJoIhxjH4oPu1ynx0Hr2X0cmYE70Fu@dpg-co96umi0si5c7397c9j0-a/joanna_xhp6')
    db = conn.cursor()
    db.execute(
        f"INSERT INTO users VALUES ('{user_id}','{username}','FREE','N/A','N/A','50','30','{antispam_time}','0','{reg_at}','{bot_id}')")
    conn.commit()
    conn.close()

# fetch info from userid


def fetchinfo(user_id):
    import psycopg2
    conn = psycopg2.connect('postgres://joanna_xhp6_user:5PXJoIhxjH4oPu1ynx0Hr2X0cmYE70Fu@dpg-co96umi0si5c7397c9j0-a/joanna_xhp6')
    db = conn.cursor()
    db.execute(f"SELECT * FROM users WHERE id='{user_id}'")
    info = db.fetchone()
    conn.commit()
    conn.close()
    return info

# fetch all info from table


def getalldata():
    import psycopg2
    conn = psycopg2.connect('postgres://joanna_xhp6_user:5PXJoIhxjH4oPu1ynx0Hr2X0cmYE70Fu@dpg-co96umi0si5c7397c9j0-a/joanna_xhp6')
    db = conn.cursor()
    db.execute(f"SELECT * FROM users")
    info = db.fetchall()
    conn.commit()
    conn.close()
    return info
# UPDATE DATA FROM TABLE


def updatedata(user_id, module_name, value):
    import psycopg2
    conn = psycopg2.connect('postgres://joanna_xhp6_user:5PXJoIhxjH4oPu1ynx0Hr2X0cmYE70Fu@dpg-co96umi0si5c7397c9j0-a/joanna_xhp6')
    c = conn.cursor()
    c.execute(f"UPDATE users SET {module_name}='{value}' WHERE id='{user_id}'")
    conn.commit()
    conn.close()

# PLAN AND EXPIRY CHECK


async def plan_expirychk(user_id):
    try:
        from pyrogram import Client, filters
        from datetime import date
        import psycopg2
        today = str(date.today())
        plan_resp = fetchinfo(user_id)
        expiry = str(plan_resp[4])
        if expiry != 'N/A' and expiry < today:
            module_name = "expiry"
            value = "N/A"
            updatedata(user_id, module_name, value)
            module_name = "plan"
            value = "N/A"
            updatedata(user_id, module_name, value)
            resp = """
   Hey 
   Your current plan has expired. regain access purchase again using /buy
      """
            await Client.send_message(user_id, resp)
    except Exception as e:
        print(e)
