# CalifiApp

Registrar y consultar las calificaciones de un grupo desde la consola.

Proyecto Scrum del **Submódulo 2: Aplica metodologías ágiles para el desarrollo de software**
CBTIS No. 200 · Programación · 3AM PGR · Docente: Mtro. Omar Torres Sánchez

## Equipo Scrum

| Rol | Integrante |
|-----|------------|
| Product Owner | (nombre) |
| Scrum Master | (nombre) |
| Equipo de desarrollo | (nombre) |

Tablero del proyecto: (pega aquí la liga de tu tablero de GitHub Projects)

## Historias de usuario terminadas

| HU | Historia | Estado |
|----|----------|--------|
| HU-01 | Registrar alumnos (máximo 30) | Terminada |
| HU-02 | Capturar calificaciones de 0 a 10 | Terminada |
| HU-03 | Calcular promedio y estatus (aprueba con 6) | Terminada |
| HU-04 | Mostrar reporte del grupo | Terminada |

## Cómo ejecutar

Abre PowerShell **dentro de la carpeta califiapp** y escribe:

```
python src/main.py
```

Si `python` no se reconoce, usa `py src/main.py`.

## Cómo correr las pruebas

```
python -m unittest discover -s tests -v
```

Debe decir **Ran 12 tests** y **OK**.

## Estructura del proyecto

```
califiapp/
├── README.md          <- la "portada" del proyecto
├── .gitignore         <- lo que Git NO debe guardar
├── data/
├── src/
│   ├── main.py            (menú de consola)
│   └── calificaciones.py  (lógica de las HU)
└── tests/
    └── test_calificaciones.py  (12 pruebas)
```

## Reglas del equipo para usar Git

- Antes de cada commit corre las pruebas: deben decir **OK**.
- Un commit = un cambio con sentido. El mensaje dice **qué hiciste**:
  - Bien: `HU-02: valida calificaciones de 0 a 10`
  - Mal: `cambios`, `ya quedó`, `asdf`
- Revisa con `git status` en qué estado estás (es tu GPS).
- Si algo se rompe y no has hecho commit: `git restore .`
- Nunca borres ni modifiques la carpeta oculta `.git`.
- Haz `git push` **antes de apagar** o reiniciar la computadora.
- Antes de empezar a trabajar en equipo, trae lo nuevo con `git pull`.
- Cierra tu sesión de GitHub al terminar: la PC del laboratorio es compartida.

Respaldo en la nube: este repositorio en GitHub (público, para que el docente lo revise).

## El ritual de cada clase

1. Instala Git: `git --version`
2. Dile quién eres: `git config --global user.name "Tu Nombre"` y `git config --global user.email "tu@correo.com"`
3. Baja tu proyecto: `git clone URL` y `cd califiapp`
4. Trabaja y prueba: `python src/main.py`
5. Toma la foto: `git add .` y `git commit -m "mensaje"`
6. Súbelo **antes de apagar**: `git push`

> La computadora olvida todo. GitHub no.
