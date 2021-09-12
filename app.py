from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def lista():  # put application's code here
    #TODO
    #Criar um dicionario para produtos com nome, preco e imagem

    lista_tops = {'#1':
                  # MUSICA         BANDA     FOTO
                      ['Já te Superei', 'Baroes',
                       'https://studiosol-a.akamaihd.net/tb/652x652/palcomp3-discografia/7/2/f/2/78abc8f4a92e421582ab8de53833b5f2.jpg'],
                  '#2':
                      ['Snow', 'Chili Peppers', 'https://i.scdn.co/image/ab6761610000e5eb5815bab04d87f264f06c8939']
                  }

    return render_template('index.html', lista_tops=lista_tops)


if __name__ == '__main__':
    app.run()
