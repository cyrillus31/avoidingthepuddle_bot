import psycopg2

def add_row(link):
    try:
        conn = psycopg2.connect(dbname="atp_youtube", password="qwe")
        cur = conn.cursor()

        cur.execute("INSERT INTO video_urls (url) VALUES (%s)", (link,))
        conn.commit()

    except(Exception, psychopg2.DatabaseError) as error:
        print(error)

    finally:
        cur.close()
        conn.close()



