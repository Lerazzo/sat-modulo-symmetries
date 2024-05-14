from planarity import PlanarGraphBuilder, planar_encoding_schnyder
from pysms.graph_builder import GraphEncodingBuilder

builder_kura = GraphEncodingBuilder(6, directed=False)
builder_kura.paramsSMS["outerplanar"] = True 
builder_kura.paramsSMS["planar"] = 5


builder_schnyder = PlanarGraphBuilder(6, directed=False)
planar_encoding_schnyder(builder_schnyder.V, builder_schnyder.var_edge, builder_schnyder, builder_schnyder, True)

builder_kura.solve(allGraphs=True)

builder_schnyder.solve(allGraphs=True)
