from apps import app, db


# Iniciar a aplicação em modo Debug e na porta 8000
if __name__ == "__main__":
    app.run(debug=True, port=7000)