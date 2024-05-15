from connexio import conect

#Mètode que llegueix tots el productes.
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

#Mètode que retorna un to_dict del objecte producte
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

#Mètode to_dict que retorna el dict personalitzat del mètode readAll
def produc_dict_join(prod) -> dict:
    return {"category": prod[0],
            "subcategory": prod[1], 
            "product": prod[2], 
            "company": prod[3], 
            "price": prod[4]
        }

#Mètode que retornar un producte, buscat pel seu id.
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

#Mètode que busca el nom de la categoria i subcategoria, a més de tots els camps de producte, a través d'una consulta amb joins
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

#Mètode per inserir un producte nou a la base de dades.
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

#Mètode que permet modificar el preu d'un producte.
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
    
#Mètode que eliminar un producte de la base de dades a través del id.
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

#Mètode que obre un arxiu .csv i dins d'un while va fent crides de mètodes per poder inserir o modificar totes les taules de la base de dades 'botiga.'
def insert_all():
    with open("llista_productes.csv", "r") as fitxer:
        saltLinia = fitxer.readline()
        linia = fitxer.readline()
        list_elements = []
        while linia:
            list_elements = linia.split(",")
            idCat = id_cat(list_elements[0])
            if idCat is None:
                insCat = ins_cat(list_elements[0], list_elements[1])
            else:
                uptCat = upt_cat(list_elements[1], list_elements[0])
            idSubcat = id_subcat(list_elements[2])
            if idSubcat is None:
                insSubcat = ins_subcat(list_elements[2], list_elements[3], list_elements[0])
            else:
                uptSubcat = upt_subcat(list_elements[3], list_elements[0], list_elements[2])
            idProd = id_prod(list_elements[4])
            if idProd is None:
                insProd = ins_prod(list_elements[4], list_elements[5], list_elements[6], list_elements[7], list_elements[8], list_elements[9], list_elements[2])
            else:
                uptProd = upt_prod(list_elements[5], list_elements[6], list_elements[7], list_elements[8], list_elements[9], list_elements[2], list_elements[4])
            linia = fitxer.readline()

#Els mètodes id_cat, id_subcat i id_prod retornen un id (si existeix), aquests mètodes son utilitzats en el mètode 'insert_all'
def id_cat(id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "SELECT category_id FROM category where category_id = %s"
        cur.execute(query, (id,))
        cat = cur.fetchone()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()
    return cat

def id_subcat(id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "SELECT subcategory_id FROM subcategory where subcategory_id = %s"
        cur.execute(query, (id,))
        cat = cur.fetchone()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()
    return cat

def id_prod(id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "SELECT product_id FROM product where product_id = %s"
        cur.execute(query, (id,))
        cat = cur.fetchone()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()
    return cat

#Els mètodes ins_cat, ins_subcat i ins_prod es dedican a inserir a la base de dades 'botiga' totes les dades de l'arxiu .csv que no estan inserides a la base de dades.
def ins_cat(id, name):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "INSERT INTO category(category_id, name) VALUES (%s, %s)"
        cur.execute(query, (id, name))
        conn.commit()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()

def ins_subcat(id, name, cat_id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "INSERT INTO subcategory(subcategory_id, name, category_id) VALUES (%s, %s, %s)"
        cur.execute(query, (id, name, cat_id))
        conn.commit()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()

def ins_prod(id, name, descripcio, company, preu, units, subcat_id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "INSERT INTO product(product_id, name, description, company, price, units, subcategory_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (id, name, descripcio, company, preu, units, subcat_id))
        conn.commit()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()

#Els mètodes upt_cat, upt_subcat i upt_prod modifiquen totes de les dades de la base de dades 'botiga', sempre i quan l'id ja estigui inserit.        
def upt_cat(name, id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "UPDATE category SET name = %s WHERE category_id = %s"
        cur.execute(query, (name, id))
        conn.commit()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()

def upt_subcat(name, cat_id, subcat_id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "UPDATE subcategory SET name = %s, category_id = %s WHERE subcategory_id = %s"
        cur.execute(query, (name, cat_id, subcat_id))
        conn.commit()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()

def upt_prod(name, descripcio, company, preu, units, subcat_id, prod_id):
    try:
        conn = conect()
        cur = conn.cursor()
        query = "UPDATE product SET name = %s, description = %s, company = %s, price = %s, units = %s, subcategory_id = %s WHERE product_id = %s"
        cur.execute(query, (name, descripcio, company, preu, units, subcat_id, prod_id))
        conn.commit()
    except Exception as e:
        return { "status": -1, "message": f"Error de conexió:{e}"}
    finally:
         conn.close()
