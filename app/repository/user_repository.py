from app.database import get_connection

def get_user_by_email(email: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """ 
        SELECT  id,
                username,
                email,
                password,
                role
        FROM public.users
        WHERE email = %s
        """,
        (email,)
    )
    user = cur.fetchone()
    cur.close()
    conn.close()

    return user

def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id,
               username,
               email,
               role
        FROM public.users
        """
    )
    users = cur.fetchall()
    cur.close()
    conn.close()

    return users

def get_user_by_id(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id,
               username,
               email,
               role
        FROM public.users
        WHERE id = %s
        """,
        (user_id,)
    )
    user = cur.fetchone()
    cur.close()
    conn.close()

    return user

def create_user(username,email,password,role):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO public.users(
            username,
            email,
            password,
            role
        )
        VALUES (%s, %s, %s,%s)
        RETURNING id,
                  username,
                  email,
                  role
        """,
        (
            username,
            email,
            password,
            role
        )
    )
    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return user

def update_user_repo(user_id, username, email, password, role):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users
        SET username=%s,
            email=%s,
            password=COALESCE(%s, password),
            role=%s
        WHERE id=%s
        RETURNING id, username, email, role
    """, (username, email, password, role, user_id))

    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return user

def update_user_partial_repo(user_id, username, email, password, role):

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users
        SET
            username = %s,
            email = %s,
            password = %s,
            role = %s
        WHERE id = %s
        RETURNING id, username, email, role
    """, (username, email, password, role, user_id))

    user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    return user

def delete_user_repo(user_id):

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM users WHERE id=%s
    """, (user_id,))
    conn.commit()
    cur.close()
    conn.close()