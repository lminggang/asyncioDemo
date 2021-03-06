from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def test(request):
    text = request.raw_args.get('name', 'no name param')
    return json({'hello': 'world', 'name': text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)