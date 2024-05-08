from connexio import conect

def read():
    try:
        conn = conect()
        cur = conn.cursor()
        cur.execute("select * from product")

        result = cur.fetchall()
        list_prod = []
        for prod in result:
            dict_prod = produc_dict(prod)
            list_prod.append(dict_prod)

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return list_prod

def produc_dict(prod) -> dict:
    return {"name": prod[0], 
            "description": prod[1], 
            "company": prod[2], 
            "price": prod[3], 
            "units": prod[4], 
            "subcategory_id": prod[5], 
            "created_at": prod[6], 
            "updated_at": prod[7]
        }

def read_one(id):
    prod = []
    try:
        conn = conect()
        cur = conn.cursor()
        query = "select * from PELICULA where id = %s;"
        cur.execute(query, (id,))
        result = cur.fetchone()
        prod.append(result[0])
        prod.append(result[1])
        prod.append(result[2])
        prod.append(result[3])
        prod.append(result[4])
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return produc_dict(prod)