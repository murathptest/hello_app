from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello, My World!</h1>
    <form>
      <label>Name:</label>
      <input type="text" name="name"><br><br>
      <label>
        <input type="checkbox" name="subscribe"> Subscribe to newsletter
      </label><br><br>
      <button type="submit">Submit</button>
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
