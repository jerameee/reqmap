import os
from io import BytesIO

import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, jsonify, render_template, request, send_file

from models import Requirement, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    requirements = Requirement.query.all()
    return render_template('index.html', requirements=requirements)

@app.route('/requirements', methods=['POST'])
def create_requirement():
    data = request.get_json()
    new_req = Requirement(
        title=data['title'],
        description=data['description'],
        priority=data['priority'],
        status=data['status']
    )
    db.session.add(new_req)
    db.session.commit()
    return jsonify({'message': 'Requirement created successfully!'}), 201

@app.route('/requirements/<int:id>', methods=['PUT'])
def update_requirement(id):
    data = request.get_json()
    req = Requirement.query.get_or_404(id)
    req.title = data['title']
    req.description = data['description']
    req.priority = data['priority']
    req.status = data['status']
    req.version += 1
    db.session.commit()
    return jsonify({'message': 'Requirement updated successfully!'})

@app.route('/requirements/<int:id>', methods=['DELETE'])
def delete_requirement(id):
    req = Requirement.query.get_or_404(id)
    db.session.delete(req)
    db.session.commit()
    return jsonify({'message': 'Requirement deleted successfully!'})

@app.route('/requirements/trace', methods=['GET'])
def trace_requirements():
    requirements = Requirement.query.all()
    graph = nx.DiGraph()

    for req in requirements:
        graph.add_node(req.id, label=req.title)
        if req.parent_id:
            graph.add_edge(req.parent_id, req.id)

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, arrows=True, node_size=3000, node_color='lightblue')

    labels = nx.get_node_attributes(graph, 'label')
    nx.draw_networkx_labels(graph, pos, labels, font_size=8)

    output = BytesIO()
    plt.savefig(output, format='png')
    plt.close()
    output.seek(0)
    return send_file(output, mimetype='image/png')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


