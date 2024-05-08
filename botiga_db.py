from connexio import conect

def read():
    try:
        conn = conect()
        cur = conn.cursor()
        cur.execute("select * from product")

        result = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return result

def to_dict_json(product) -> list:
    llista = []
    
    dict = {}
    llista.append(product)
    return