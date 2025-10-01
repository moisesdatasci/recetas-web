# 🍳 Recetas Web - Django Project

Aplicación web de recetas desarrollada con Django que permite a los usuarios explorar y descubrir recetas de cocina. Proyecto académico que implementa el patrón MTV (Model-Template-View), diseño responsivo con Bootstrap y gestión de contenido dinámico.

## 📋 Características

- ✨ Página de inicio con jumbotron destacado
- 📖 Lista completa de recetas con tarjetas visuales
- 🔍 Vista detallada de cada receta (ingredientes e instrucciones)
- 📧 Formulario de contacto funcional con validación
- 📱 Diseño responsivo con Bootstrap 5
- 🖼️ Gestión de imágenes para cada receta
- 🎨 Navbar y footer en todas las páginas
- 🔄 Herencia de templates para código reutilizable

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python 3.x, Django 4.x
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Base de datos:** SQLite (desarrollo)
- **Gestión de imágenes:** Pillow

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/moisesdatasci/recetas-web.git
cd recetas-web
```

2. **Crear y activar entorno virtual**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

```

3. **Instalar dependencias**
```bash
pip install django pillow
```

4. **Realizar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Aplicación: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

## 📁 Estructura del Proyecto

```
recetas-web/
│
├── recetas_web/           
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── recetas/              
│   ├── models.py       
│   ├── views.py       
│   ├── urls.py           
│   ├── admin.py           
│   └── templates/         
│       └── recetas/
│           ├── base.html
│           ├── inicio.html
│           ├── lista_recetas.html
│           ├── detalle_receta.html
│           ├── contacto.html
│           └── confirmacion.html
│
├── static/               
│   ├── css/
│   │   └── estilos.css
│   └── images/
│
├── media/                 
│   └── recetas/
│
├── manage.py
├── db.sqlite3
└── README.md
```

## 💻 Uso

### Agregar Recetas

1. Accede al panel de administración: http://127.0.0.1:8000/admin/
2. Inicia sesión con tu superusuario
3. Ve a "Recetas" y haz clic en "Agregar Receta"
4. Completa los campos:
   - Nombre de la receta
   - Ingredientes (uno por línea)
   - Instrucciones paso a paso
   - Imagen de la receta
5. Guarda los cambios

### Navegar por el Sitio

- **Inicio:** Muestra las últimas 6 recetas agregadas
- **Recetas:** Lista completa de todas las recetas
- **Detalle:** Clic en cualquier receta para ver información completa
- **Contacto:** Formulario para enviar mensajes

## 🎯 Funcionalidades Implementadas

### Modelo MTV
- ✅ Modelo `Receta` con campos: nombre, ingredientes, instrucciones, imagen
- ✅ Vistas basadas en funciones para manejo de lógica
- ✅ Templates con herencia y contenido dinámico

### Navegación
- ✅ Navbar responsivo con enlaces a todas las secciones
- ✅ URLs dinámicas con etiquetas `{% url %}`
- ✅ Redirección después de envío de formularios

### Contenido Estático y Dinámico
- ✅ Archivos CSS personalizados
- ✅ Gestión de imágenes estáticas y media
- ✅ Bootstrap 5 integrado vía CDN

### Templates
- ✅ Template base con herencia
- ✅ Iteradores `{% for %}` para listar recetas
- ✅ Condicionales `{% if %}` para validaciones
- ✅ Filtros de Django (`truncatewords`, `linebreaks`)

### Manejo de Errores
- ✅ Vista 404 con `get_object_or_404`
- ✅ Validación de formularios con mensajes
- ✅ Página de confirmación personalizada

## 🌐 Páginas del Sitio

| Página | Ruta | Descripción |
|--------|------|-------------|
| Inicio | `/` | Jumbotron y últimas recetas |
| Recetas | `/recetas/` | Lista completa de recetas |
| Detalle | `/receta/<id>/` | Información completa de una receta |
| Contacto | `/contacto/` | Formulario de contacto |
| Confirmación | `/confirmacion/` | Mensaje de confirmación |
| Admin | `/admin/` | Panel de administración |

## 🎨 Personalización

### Modificar Estilos
Edita el archivo `static/css/estilos.css` para personalizar:
- Colores
- Tipografía
- Espaciados
- Animaciones

### Agregar Más Campos al Modelo
1. Edita `recetas/models.py`
2. Ejecuta `python manage.py makemigrations`
3. Ejecuta `python manage.py migrate`

## 📝 Requisitos de la tarea Cumplidos

- ✅ Estructura MVC/MTV implementada
- ✅ Navbar, Jumbotron y Footer
- ✅ Páginas estáticas y dinámicas
- ✅ Navegación funcional entre páginas
- ✅ Contenido estático (imágenes y CSS)
- ✅ Modelo de datos con campos requeridos
- ✅ Vistas genéricas y específicas
- ✅ Herencia de templates
- ✅ Iteradores y condicionales en templates
- ✅ Manejo de errores y redirecciones
- ✅ URLs dinámicas
- ✅ Diseño responsivo con Bootstrap

## 👥 Autores

- Moisés Ortega - Sin grupo - Desarrollo completo

## 📄 Licencia

Este proyecto es de uso académico para el curso de Backend Python de Talento Digital.

## 📞 Contacto

Para preguntas o sugerencias:
- Email: moises.ortega@usach.cl
- GitHub: [@tu-usuario](https://github.com/moisesdatasci)

---

⭐ **¡No olvides dar una estrella al proyecto si te resultó útil!**
