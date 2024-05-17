import datetime
import json
import os
import random
import re
import time

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from plugins.func.users_sql import *

session = requests.session()
cc_list = []


class Generar_tarjeta:
    def __init__(self, BIN, cantidad=1, solo_impresion=False):
        splitter = BIN.split("|")
        try:
            self.ccnum = re.sub("[^0-9a-z]", "", splitter[0].lower())
            if self.ccnum.isnumeric():
                if self.ccnum[0:1] == "3":
                    if len(self.ccnum) == 15:
                        self.ccnum = self.ccnum[0:15].replace(self.ccnum[-4:], "x")
                else:
                    if len(self.ccnum) == 16:
                        self.ccnum = self.ccnum[0:16].replace(self.ccnum[-4:], "x")
        except:
            return "INCOMPLETED DATA!"
        try:
            self.mes = splitter[1]
        except IndexError:
            self.mes = None
        try:
            self.ano = splitter[2]
        except IndexError:
            self.ano = None
        try:
            self.cvv = splitter[3]
        except IndexError:
            self.cvv = None

        self.localidad_bin = "Desconocida"
        self.RONDAS_GEN = 10000
        self.CANTIDAD_TARJETAS = cantidad
        self.lista_tarjetas = []
        self.dic_tarjetas = {}
        if self.CANTIDAD_TARJETAS >= 1:
            for i in range(0, 10000):
                tarj_creada = self.crear_tarjeta()
                self.lista_tarjetas.append(tarj_creada["datos_completos"])
                # Plantilla dato
                self.dic_tarjetas[i] = {
                    "numero": tarj_creada["numero_tarjeta"],
                    "fecha": tarj_creada["venc"],
                    "codigo_seg": tarj_creada["codigo_seg"],
                    "dato_completo": tarj_creada["datos_completos"],
                }
        else:
            self.crear_tarjeta()

    def __repr__(self):
        listcc = ""
        for n in self.lista_tarjetas:
            listcc += f"<code>{n}</code>\n"

        return f"{listcc}-{self.ccnum}"

    def json(self):
        return json.dumps(self.dic_tarjetas)

    def crear_tarjeta(self):
        tarjeta = {}
        tarjeta["numero_tarjeta"] = self.crear_numero(self.ccnum)
        tarjeta["codigo_seg"] = self.generar_codigo_seguridad()
        tarjeta["venc"] = self.generar_fecha_venc()
        self.string = ""
        self.string += tarjeta["numero_tarjeta"]
        self.string += "|" + tarjeta["venc"]["fecha_completa"]
        self.string += "|" + tarjeta["codigo_seg"]
        tarjeta["datos_completos"] = self.string
        return tarjeta

    def gen_aleatorio(self, BIN):
        self.ccnum = (
            self.ccnum.ljust(15, "x")
            if self.ccnum[0] == "3"
            else self.ccnum.ljust(16, "x")
        )
        numero = ""
        self.ccnum = re.sub("[^0-9]", "x", self.ccnum)
        for i in self.ccnum:
            numero += str(random.randint(0, 9)) if i.lower() == "x" else i
        return numero

    def checkear(self, cc):
        num = list((map(int, str(cc))))
        return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

    def crear_numero(self, BIN):
        numero = self.gen_aleatorio(BIN)
        for i in range(1, self.RONDAS_GEN):
            numero = self.gen_aleatorio(BIN)
            chk0 = self.checkear(numero)
            if chk0 and numero:
                return numero

    def generar_fecha_venc(self):
        fecha = {"anio": None, "mes": None, "fecha_completa": None}

        def gen_anio():
            try:
                self.ano = re.sub("[^0-9]", " ", self.ano)
                BinCheck = int(self.ccnum[0:1])
                if 3 <= int(BinCheck) <= 6:
                    if 4 <= int(BinCheck) <= 6:
                        matchano = re.findall(
                            r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-1])\b", self.ano
                        )
                        ano = matchano[0]
                        if len(ano) == 2:
                            ano = f"20{ano}"
                        return ano
                    elif int(BinCheck) == 3:
                        matchano = re.findall(
                            r"\b(3[0-1]|2[2-9]|202[2-9]|203[0-1])\b", self.ano
                        )
                        ano = matchano[0]
                        if len(ano) == 2:
                            ano = f"20{ano}"
                        return ano
            except:
                anio_actual = datetime.datetime.now().year
                return anio_actual + random.randint(1, 9)

        fecha["anio"] = str(gen_anio())

        def gen_mes():
            try:
                self.mes = re.sub("[^0-9]", " ", self.mes)
                BinCheck = int(self.ccnum[0:1])
                if 3 <= int(BinCheck) <= 6:
                    if 4 <= int(BinCheck) <= 6:
                        matchmes = re.findall(r"\b(0[1-9]|1[0-2])\b", self.mes)
                        mes = matchmes[0]
                        return mes
                    elif int(BinCheck) == 3:
                        matchmes = re.findall(r"\b(0[1-9]|1[0-2])\b", self.mes)
                        mes = matchmes[0]
                        return mes
            except:
                mes = random.randint(1, 12)
                if mes > 9:
                    return str(mes)
                else:
                    return "0" + str(mes)

        fecha["mes"] = gen_mes()
        fecha["fecha_completa"] = fecha["mes"] + "|" + fecha["anio"]
        return fecha

    def generar_codigo_seguridad(self):
        if self.ccnum[0] == "3":
            if self.cvv != None:
                if re.search(r"[0-9x]", self.cvv.lower()):
                    if self.cvv.lower().find("x") >= 0:
                        self.cvv = re.sub("[^0-9a-z]", "x", self.cvv.lower())
                        self.cvv = re.sub(r"[a-z]", "x", self.cvv.lower())
                        self.cvv = self.cvv.ljust(3, "x")
                        numero = ""
                        for i in self.cvv:
                            numero += (
                                str(random.randint(0, 9)) if i.lower() == "x" else i
                            )
                        return numero[0:4]
                    else:
                        self.cvv = re.sub("[^0-9a-z]", "x", self.cvv.lower())
                        self.cvv = re.sub(r"[a-z]", "x", self.cvv.lower())
                        self.cvv = self.cvv.ljust(3, "x")
                        numero = ""
                        for i in self.cvv:
                            numero += (
                                str(random.randint(0, 9)) if i.lower() == "x" else i
                            )
                        return numero[0:4]
            return str(random.randint(1001, 9998))

        else:
            if self.cvv != None:
                if re.search(r"[0-9x]", self.cvv.lower()):
                    if self.cvv.lower().find("x") >= 0:
                        self.cvv = re.sub("[^0-9a-z]", "x", self.cvv.lower())
                        self.cvv = re.sub(r"[a-z]", "x", self.cvv.lower())
                        self.cvv = self.cvv.ljust(3, "x")
                        numero = ""
                        for i in self.cvv:
                            numero += (
                                str(random.randint(0, 9)) if i.lower() == "x" else i
                            )
                        return numero[0:3]
                    else:
                        self.cvv = re.sub("[^0-9a-z]", "x", self.cvv.lower())
                        self.cvv = re.sub(r"[a-z]", "x", self.cvv.lower())
                        self.cvv = self.cvv.ljust(3, "x")
                        numero = ""
                        for i in self.cvv:
                            numero += (
                                str(random.randint(0, 9)) if i.lower() == "x" else i
                            )
                        return numero[0:3]
            return str(random.randint(101, 998))


async def GeneatedCC(extra):
    if int(extra[0]) == 3:
        cant = 15
    else:
        cant = 16
    return Generar_tarjeta(extra, cant, True)


# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual Telegram API ID and hash

# app = Client("Joanna",
#             api_id="24578407",
#             api_hash="5f711fbe013fd0d20147f62728118510",
#             bot_token="6669312789:AAG_d464Q2TU48Wbb_uMkMbUSPldGHIzbvM")


@Client.on_message(filters.command(["gen", "generate"]) & filters.private)
async def generate_cc(_, message: Message):
    try:
        user_id = str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == "None":
            resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
            await message.reply_text(resp, message.id)
        else:
            pm = fetchinfo(user_id)
            status = pm[2]
            role = status
            _, bin_input, *quantity = message.text.split(" ")
            quantity = int(quantity[0]) if quantity else 20
            time.perf_counter()
            session = requests.session()
            bin = session.get(f"https://lookup.binlist.net/{bin_input}").json()
            try:
                brand = bin["scheme"].upper()
            except:
                brand = "N/A"
            try:
                type = bin["type"].upper()
            except:
                type = "N/A"
            try:
                level = bin["brand"].upper()
            except:
                level = "N/A"
            try:
                bank_data = bin["bank"]
            except:
                bank_data = "N/A"
            try:
                bank = bank_data["name"].upper()
            except:
                bank = "N/A"
            try:
                country_data = bin["country"]
            except:
                country_data = "N/A"
            try:
                country = country_data["name"].upper()
            except:
                country = "N/A"
            try:
                flag = country_data["emoji"]
            except:
                flag = "N/A"
            try:
                currency = country_data["currency"].upper()
            except:
                currency = "N/A"
            cc_generator = await GeneatedCC(bin_input)
            ccc = [
                f"<code>{cc}</code>" for cc in cc_generator.lista_tarjetas[:quantity]
            ]
            cccf = [f"{cc}" for cc in cc_generator.lista_tarjetas[:quantity]]
            time.perf_counter()
            xxx = "\n".join(ccc)
            resp = f"""
 GENERATED SUCCESSFULLY ✅

{xxx}

┏－－－－－－－－－－－－┒
┠ Amount - <code>{quantity}</code>
┠ Bin - <code>{bin_input}</code>
┠ - - - Bin Info - - -
┠  {brand} - {level} - {type}
┠ Bank - {bank}
┠ Country - {country} - {flag} - {currency}
┠ Gen By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠print('𝙍𝝣𝘽𝝣𝙇™ </> ⚠️')</a>
┗－－－－－－－－－－－－┛"""

            resp1 = f"""
 GENERATED SUCCESSFULLY ✅

┏－－－－－－－－－┒
┠ Amount - <code>{quantity}</code>
┠ Bin - <code>{bin_input}</code>
┠ - - - Bin Info - - -
┠  {brand} - {level} - {type}
┠ Bank - {bank}
┠ Country - {country} - {flag} - {currency}
┠ Gen By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠print('𝙍𝝣𝘽𝝣𝙇™ </> ⚠️')</a>
┗－－－－－－－－－┛"""
            if quantity > 20:
                with open(f"{quantity}x_CC_GEN_BY_@JoannaChkBot.txt", "w") as file:
                    file.write("\n".join(cccf))
                await message.reply_document(
                    document=f"{quantity}x_CC_GEN_BY_@JoannaChkBot.txt",
                    caption=resp1,
                    reply_to_message_id=message.id,
                )
                os.remove(f"{quantity}x_CC_GEN_BY_@JoannaChkBot.txt")
            else:
                await message.reply_text(resp)

    except ValueError:
        await message.reply_text(
            "Invalid command format. Please use /gen BIN [QUANTITY]"
        )
