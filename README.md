# Taller — Predicción de deserción

Instrucciones rápidas para ejecutar la aplicación localmente.

- Ejecutar la interfaz Streamlit (frontend):

```bash
streamlit run streamlit_app.py
```

- Ejecutar el backend Flask por separado (opcional, para llamadas HTTP):

```bash
python server.py
```

Notas:
- `server.py` contiene un guard que evita arrancar el servidor de desarrollo cuando
  el archivo es ejecutado por Streamlit (previene errores con `signal`).
- Para despliegue en producción, use un WSGI/ASGI server (por ejemplo `gunicorn` o `uvicorn`).
