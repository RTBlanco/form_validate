from form_validate import app

@app.route('/')
def home():
  return "<h1>test</h1>"