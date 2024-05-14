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
    return {"product_id": prod[0],
            "name": prod[1], 
            "description": prod[2], 
            "company": prod[3], 
            "price": prod[4], 
            "units": prod[5], 
            "subcategory_id": prod[6], 
            "created_at": prod[7], 
            "updated_at": prod[8]
        }

def produc_dict_join(prod) -> dict:
    return {"category": prod[0],
            "subcategory": prod[1], 
            "product": prod[2], 
            "company": prod[3], 
            "price": prod[4]
        }

def read_one(id):
    prod = []
    try:
        conn = conect()
        cur = conn.cursor()
        query = "select * from product where product_id = %s;"
        cur.execute(query, (id,))
        result = cur.fetchone()
        if result is not None:
            prod.append(result[0])
            prod.append(result[1])
            prod.append(result[2])
            prod.append(result[3])
            prod.append(result[4])
            prod.append(result[5])
            prod.append(result[6])
            prod.append(result[7])
            prod.append(result[8])
        else:
            return {"status": -1, "message": f"No se encontró ningún producto con el ID {id}"}
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return produc_dict(prod)

def readAll():
    try:
        conn = conect()
        cur = conn.cursor()
        query = "SELECT c.name AS cat, s.name AS subcat, p.name AS prod, p.company AS empresa, p.price AS preu FROM product p INNER JOIN subcategory s ON p.subcategory_id = s.subcategory_id INNER JOIN category c ON s.category_id = c.category_id"
        
        cur.execute(query)
        result = cur.fetchall()
        
        list_prod = []
        for prod in result:
            dict_prod = produc_dict_join(prod)
            list_prod.append(dict_prod)

    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return list_prod

def insert_product(name, description, company, price, units, subcategory_id, created_at, updated_at):
    try: 
        conn = conect()
        cur = conn.cursor()
        query = "insert into product (name, description, company, price, units, subcategory_id,  created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, description, company, price, units, subcategory_id, created_at, updated_at)
        cur.execute(query, values)

        conn.commit()
        id_product=cur.lastrowid
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    finally:
        conn.close()
    return id_product

def update_product(id, price):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "update product SET price = %s WHERE product_id = %s;"
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
        query = "delete from product where product_id = %s;"
        cur.execute(query, (id,))

        conn.commit()
    except Exception as e:
         return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()

def inser_all():
    try:
        conn = conect()
        cur = conn.cursor()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()