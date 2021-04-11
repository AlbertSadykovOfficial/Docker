from flask import Flask, Response, request
import requests
import hashlib
import redis

app = Flask(__name__)
salt = "UNIQUE_SALT"
default_name = 'Albert'
cache = redis.StrictRedis( host='redis', port=6369, db=0)


@app.route('/', methods=["GET", "POST"])
def mainpage():
  
  name = default_name
  # Обработка инъекции
  if request.method == "POST":
    name = html.escape( request.form['name'], quote=True )

  salted_name = salt + name
  name_hash = hashlib.sha256( salted_name.encode() ).hexdigest()
  header = '<html><head><title>Identidock</title></head><body>'
  body = ''' <form method="POST">
                Hello <input type="text" name="name" value="{}">
                <input type="submit" value="submit">
              </form>
              <p>Your Image:
                <img src="/monster/monster.png">
              </p>
         '''.format(name, name_hash)
  footer = '</body></html>'

  return header + body + footer


@app.route('/monster/<name>')
def get_identicon( name ):
  # Обработка инъекции
  name = html.escape( name , quote=True )
  image = cache.get( name )
  if image is None:
    #  Get image with 80x80 scale size
    print( "Cache miss (промах кэша)", flush=True)
    r = requests.get('http://dnmonster:8000/monster/' + name + '?size=80')
    image = r.content
    cache.set( name, image )

  return Response( image, mimetype='image/png' )


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')