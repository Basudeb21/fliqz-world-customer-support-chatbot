# app/db/mysql.py

import pymysql

from app.core.config import settings


def get_connection():

    return pymysql.connect(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DATABASE,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )


def fetch_one(query, params=None):

    connection = get_connection()

    try:

        with connection.cursor() as cursor:

            cursor.execute(
                query,
                params
            )

            return cursor.fetchone()

    finally:

        connection.close()


def fetch_all(query, params=None):

    connection = get_connection()

    try:

        with connection.cursor() as cursor:

            cursor.execute(
                query,
                params
            )

            return cursor.fetchall()

    finally:

        connection.close()


def execute(query, params=None):

    connection = get_connection()

    try:

        with connection.cursor() as cursor:

            cursor.execute(
                query,
                params
            )

            return cursor.lastrowid

    finally:

        connection.close()