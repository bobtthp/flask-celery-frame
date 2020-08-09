from plog import create_app


app = create_app()

if __name__ == '__main__':
    app.run(
        port=12345,
        debug=True,
    )