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

def insert_product(name, description, company, price, units, subcategory_id,  created_at, updated_at):
    try: 
        conn = conect()
        cur = conn.cursor()
        query = "insert into product (name, description, company, price, units, subcategory_id,  created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, description, company, price, units, subcategory_id,  created_at, updated_at)
        cur.execute(query, values)

        conn.commit()
        film_id=cur.lastrowid
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return film_id

def update_product(id, price):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "update producte SET price = %s WHERE id = %s;"
        values  = (price, id)
        cur.execute(query, values)

        conn.commit()
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    
def delete_product(id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "delete from product where id = %s;"
        cur.execute(query, (id,))

        conn.commit()
    except Exception as e:
         return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()