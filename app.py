from flask import Flask, request, render_template, jsonify
import webbrowser
from threading import Timer
import json

app = Flask(__name__)

def czy_spojny(graf):
    if not graf:
        return True
    odwiedzone = set()
    def dfs(wierzcholek):
        odwiedzone.add(wierzcholek)
        for sasiad in graf.get(wierzcholek, []):
            if sasiad not in odwiedzone:
                dfs(sasiad)
    start = next(iter(graf))
    dfs(start)
    return len(odwiedzone) == len(graf)

def czy_nieskierowany(graf):
    for v in graf:
        for sasiad in graf[v]:
            if v not in graf.get(sasiad, []):
                return False
    return True

def szukanie_trojkatow(graf):
    trojkaty = []
    for v in graf:
        for u in graf[v]:
            if u > v:
                for w in graf[v]:
                    if w > u and w in graf[u]:
                        trojkaty.append([v, u, w])
    return trojkaty

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_graph():
    try:
        graf = json.loads(request.form['graph'])
        if not czy_nieskierowany(graf):
            return jsonify({'error': 'Graf jest skierowany — analiza dotyczy tylko grafów nieskierowanych.'})
        spojny = czy_spojny(graf)        
        trojkaty = szukanie_trojkatow(graf)
        return jsonify({
            'spojny': spojny,
            'trojkaty': trojkaty
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = 5000
    url = f"http://127.0.0.1:{port}"

    Timer(1, lambda: webbrowser.open(url)).start()

    app.run(port=port)