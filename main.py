from flask import Flask, request, jsonify
from geopy.distance import geodesic

app = Flask(__name__)

def calculate_distance(lat1, lon1, lat2, lon2):
    """Расчет расстояния между двумя точками."""
    point1 = (lat1, lon1)
    point2 = (lat2, lon2)
    distance = geodesic(point1, point2).kilometers
    return distance

def calculate_delivery_cost(distance):
    cost_per_km = 5
    delivery_cost = distance * cost_per_km
    return delivery_cost

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    if 'lat1' in data and 'lon1' in data and 'lat2' in data and 'lon2' in data:
        lat1, lon1, lat2, lon2 = data['lat1'], data['lon1'], data['lat2'], data['lon2']
        distance = calculate_distance(lat1, lon1, lat2, lon2)
        delivery_cost = calculate_delivery_cost(distance)
        return jsonify({'distance': distance, 'delivery_cost': delivery_cost})
    else:
        return jsonify({'error': 'Недостаточно данных'}), 400

if __name__ == '__main__':
    app.run(debug=True)



