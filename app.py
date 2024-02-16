from flask import Flask, request
import languagemodels as lm

app = Flask('app')


@app.route('/')
def hello_world():
  q = request.args.get("q")
  res = lm.chat(f'''
        System: Respond as a helpful assistant your name is fury and you serve vishnu gupta call him boss
        User: {q}

        Assistant:
  ''')
  return res


app.run(host='0.0.0.0')