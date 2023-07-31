import pandas as pd
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def union_sets(set1, set2):
    return set1.union(set2)

def intersection_sets(set1, set2):
    return set1.intersection(set2)

def difference_sets(set1, set2):
    return set1.difference(set2)

def complement_set(universal_set, set1):
    return universal_set.difference(set1)

def cardinality_set(set1):
    return len(set1)

def plot_venn_diagram(set1, set2):
    common_elements = intersection_sets(set1, set2)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=[0], y=[0],
                             mode='markers',
                             marker=dict(size=0.1, color='white'))
                 )

    fig.add_trace(go.Scatter(x=[0.5], y=[0],
                             mode='markers',
                             marker=dict(size=0.1, color='white'))
                 )

    fig.add_trace(go.Scatter(x=[0.25], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='blue', opacity=0.3),
                             text='A',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.75], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='red', opacity=0.3),
                             text='B',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.5], y=[0],
                             mode='markers',
                             marker=dict(size=70, color='purple', opacity=0.3),
                             text='A ∩ B',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.65], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='purple', opacity=0.3),
                             text='A - B',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.35], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='purple', opacity=0.3),
                             text='B - A',
                             showlegend=False)
                 )

    fig.update_layout(
        title='Interactive Venn Diagram',
        shapes=[
            dict(type='circle',
                 xref='x', yref='y',
                 x0=0, y0=0, x1=0.5, y1=1,
                 line_color='blue'),
            dict(type='circle',
                 xref='x', yref='y',
                 x0=0.5, y0=0, x1=1, y1=1,
                 line_color='red')
        ],
        annotations=[
            dict(x=0.25, y=0.2,
                 xref='x', yref='y',
                 text='A', showarrow=False),
            dict(x=0.75, y=0.2,
                 xref='x', yref='y',
                 text='B', showarrow=False),
            dict(x=0.5, y=0.2,
                 xref='x', yref='y',
                 text='A ∩ B', showarrow=False),
            dict(x=0.65, y=0.2,
                 xref='x', yref='y',
                 text='A - B', showarrow=False),
            dict(x=0.35, y=0.2,
                 xref='x', yref='y',
                 text='B - A', showarrow=False),
        ]
    )

    if common_elements:
        common_text = ", ".join(map(str, common_elements))
        fig.add_annotation(
            x=0.5, y=0.15,
            xref='x', yref='y',
            text='Common Elements: {' + common_text + '}',
            showarrow=False
        )

    fig.show()

def plot_3d_sierpinski(n):
    # Generate Sierpinski triangle fractal in 3D
    points = np.array([[0.0, 0.0, 0.0]])
    for _ in range(n):
        new_points = []
        for p in points:
            new_points.append(p + [0.0, 0.0, 0.5])
            new_points.append(p + [0.5, 0.0, 0.0])
            new_points.append(p + [0.0, 0.5, 0.0])
        points = np.array(new_points)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='blue', s=10)
    plt.title('Sierpinski Triangle Fractal (3D)')
    plt.axis('off')
    plt.show()

def display_math_expression():
    x, y = sp.symbols('x y')
    expr = sp.cos(x) + sp.sin(y)
    sp.pprint(expr)

# Example usage
universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print("Union:", union_sets(set1, set2))
print("Intersection:", intersection_sets(set1, set2))
print("Difference (A - B):", difference_sets(set1, set2))
print("Difference (B - A):", difference_sets(set2, set1))

print("Complement of Set A:", complement_set(universal_set, set1))
print("Cardinality of Set A:", cardinality_set(set1))

plot_venn_diagram(set1, set2)
plot_3d_visualization()
plot_3d_sierpinski(n=3)
display_math_expression()
