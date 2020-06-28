from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


# Create your views here.
def index(request):
    cursor = connection.cursor()

    cursor.execute('SELECT id, letra FROM dictionary_letra')
    letras = cursor.fetchall()

    return render(request, 'pages/index.html', {'letras': letras})


def busqueda(request):
    if request.method == 'POST':
        termino = request.POST.get('nombreTermino', '')

        return redirect('/termino/' + termino.lower())


def diccionario(request, letra):
    lista_0 = list()
    lista_1 = list()
    lista_2 = list()
    i = 0
    cursor = connection.cursor()

    cursor.execute('SELECT id, letra FROM dictionary_letra')
    letras = cursor.fetchall()

    cursor.execute("SELECT id, termino FROM dictionary_termino as t where t.letra_id in (select id from "
                   "dictionary_letra where letra = '" + letra + "') ORDER BY termino")
    terminos = cursor.fetchall()
    if len(terminos) == 0:
        lista_0 = 'No hay terminos asociados a esta letra.'
    else:
        for _, termino in terminos:
            if i == 0:
                lista_0.append(termino)
                i += 1
            elif i == 1:
                lista_1.append(termino)
                i += 1
            elif i == 2:
                lista_2.append(termino)
                i = 0

    return render(request, 'pages/index.html',
                  {'letras': letras, 'id': letra, 'lista1': lista_0, 'lista2': lista_1, 'lista3': lista_2})


@csrf_exempt
def agregar_termino(request):
    if request.method == 'POST':
        termino = request.POST.get('nombreTermino', '')
        definicion = request.POST.get('nombreDefinicion', '')

        if termino and definicion:
            cursor = connection.cursor()

            cursor.execute("SELECT id, letra FROM dictionary_letra where letra ='" + termino[0].lower() + "';")
            letras = cursor.fetchall()

            cursor.execute("SELECT termino FROM dictionary_termino WHERE termino = '" + termino + "';")
            termino_db = cursor.fetchall()
            if len(termino_db) == 0:
                cursor.execute(
                    "INSERT INTO dictionary_termino (termino, letra_id, created_at, updated_at) VALUES ('" +
                    termino.lower() + "', '" + str(letras[0][0]) + "', '" + str(datetime.now()) + "', '" +
                    str(datetime.now()) + "');")
                cursor.execute("SELECT id, termino FROM dictionary_termino where termino = '" + termino + "';")
                termino_db = cursor.fetchall()

                cursor.execute(
                    "INSERT INTO dictionary_definicion (definicion, termino_id, created_at, updated_at) VALUES ('"
                    + definicion.lower() + "', '" + str(termino_db[0][0]) + "', '" + str(datetime.now()) + "', '" +
                    str(datetime.now()) + "');")
                messages.success(request, 'Termino agregado exitosamente.')
                return redirect('/')
            else:
                messages.error(request, 'Termino ya existe.')

    return render(request, 'pages/create.html')


def editar_termino(request, termino, id):
    cursor = connection.cursor()

    if request.method == 'POST':
        termino = request.POST.get('nombreTermino', '')
        cursor.execute("UPDATE dictionary_termino SET termino = '" + str(termino) + "', updated_at = '" + str(
            datetime.now()) + "' WHERE id = " + str(id) + ";")
        messages.success(request, 'Termino editado exitosamente.')
        return redirect('/termino/' + str(termino))
    else:
        cursor.execute("SELECT dictionary_definicion.id, definicion, dictionary_termino.id FROM dictionary_definicion"
                       " RIGHT JOIN dictionary_termino on termino_id = dictionary_termino.id WHERE termino = '" +
                       termino + "' ORDER BY definicion")
        definicion_db = cursor.fetchall()

    return render(request, 'pages/termino.html',
                  {'termino': termino, 'definiciones': definicion_db, 'id': definicion_db[0][2], 'definicion': '',
                   'form': 'termino'})


def eliminar_termino(request, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM dictionary_definicion WHERE termino_id = " + str(id) + ";")
    cursor.execute("DELETE FROM dictionary_termino WHERE id = " + str(id) + ";")
    messages.success(request, 'Termino eliminado exitosamente.')
    return redirect('/')


@csrf_exempt
def agregar_definicion(request):
    if request.method == 'POST':
        termino_id = request.POST.get('idTermino', '')
        definicion = request.POST.get('nombreDefinicion', '')
        if termino_id and definicion:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO dictionary_definicion (definicion, termino_id, created_at, updated_at) VALUES ('"
                + definicion + "', '" + str(termino_id) + "', '" + str(datetime.now()) + "', '" +
                str(datetime.now()) + "');")

            cursor.execute("SELECT id, termino FROM dictionary_termino where id = '" + termino_id + "';")
            termino = cursor.fetchall()

            messages.success(request, 'Definicion agregado exitosamente.')
            return redirect('/termino/' + str(termino[0][1]))


def editar_definicion(request, termino, id):
    definicion = str()
    cursor = connection.cursor()

    if request.method == 'POST':
        definicion = request.POST.get('nombreDefinicion', '')
        cursor.execute("UPDATE dictionary_definicion SET definicion = '" + str(definicion) + "', updated_at = '" + str(
            datetime.now()) + "'  WHERE id = " + str(id) + ";")
        messages.success(request, 'Definicion editada exitosamente.')
        return redirect('/termino/' + str(termino))
    else:
        cursor.execute(
            "SELECT dictionary_definicion.id, definicion, dictionary_termino.id FROM dictionary_definicion "
            "RIGHT JOIN dictionary_termino on termino_id = dictionary_termino.id WHERE termino = '" + termino +
            "' ORDER BY definicion")
        definicion_db = cursor.fetchall()
        for i, d, _ in definicion_db:
            if i == id:
                definicion = d

    return render(request, 'pages/termino.html',
                  {'termino': termino, 'definiciones': definicion_db, 'id': definicion_db[0][2],
                   'definicion': definicion, 'id_e': id, 'action': 'editar', 'form': 'definicion'})


def eliminar_definicion(request, letra, id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM dictionary_definicion WHERE id = " + str(id) + ";")
    messages.success(request, 'Definicion eliminada exitosamente.')
    return redirect('/termino/' + str(letra))


def ver(request, termino):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT dictionary_definicion.id, definicion, dictionary_termino.id FROM dictionary_definicion "
        "RIGHT JOIN dictionary_termino on termino_id = dictionary_termino.id WHERE termino = '" + termino +
        "' ORDER BY definicion")
    definicion_db = cursor.fetchall()
    if len(definicion_db) == 0:
        definicion_db = 'No hay definiciones asociados a este termino.'
        definicion_id = str()
    else:
        definicion_id = definicion_db[0][2]

    return render(request, 'pages/termino.html',
                  {'termino': termino, 'definiciones': definicion_db, 'id': definicion_id, 'definicion': '',
                   'action': 'agregar', 'form': 'definicion'})
