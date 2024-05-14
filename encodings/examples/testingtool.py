from pysms.graph_builder import GraphEncodingBuilder

builder = GraphEncodingBuilder(7, directed=False)
builder.maxDegreeTEST(3)
builder.solve(allGraphs=True)
