app = create_app()

# Define a route to fetch the available articles

@app.route("/articles", methods=["GET"], strict_slashes=False)


if __name__ == "__main__":
    app.run(debug=True)