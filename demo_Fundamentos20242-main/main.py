from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Lista para almacenar los regalos (diccionarios con nombre y destinatario)
regalos = []

@app.route('/')
def index():
    return render_template('index.html', regalos=regalos)

@app.route('/add_gift', methods=['POST'])
def add_gift():
    gift_name = request.form.get('gift_name')
    recipient = request.form.get('recipient')
    
    if gift_name and recipient:
        regalos.append({'gift_name': gift_name, 'recipient': recipient})
    
    return render_template('index.html', regalos=regalos)

@app.route('/get_gifts', methods=['GET'])
def get_gifts():
    gift_names = [gift['gift_name'] for gift in regalos]
    return jsonify(gift_names)

@app.route('/delete_gift', methods=['POST'])
def delete_gift():
    gift_name_to_delete = request.form.get('gift_name_to_delete')
    
    # Buscar y eliminar el regalo
    global regalos
    regalos = [gift for gift in regalos if gift['gift_name'] != gift_name_to_delete]
    
    return render_template('index.html', regalos=regalos)

if __name__ == '__main__':
    app.run(debug=True)