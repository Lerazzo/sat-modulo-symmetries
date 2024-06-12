from planarity import PlanarGraphBuilder, planar_encoding_schnyder
from pysms.graph_builder2 import GraphEncodingBuilder


# k = 0

# for i in range(1,13):
#     if k < i:
#         builder_kura = GraphEncodingBuilder(i, directed=False)
#         builder_kura.paramsSMS["planar"] = 5
#         #builder_kura.minDegree(k)
#         builder_kura.solve(allGraphs=True)
#         print("Done with: ", k, i)




builder_schnyder = PlanarGraphBuilder(5, directed=False)
planar_encoding_schnyder(builder_schnyder.V, builder_schnyder.var_edge, builder_schnyder, builder_schnyder, True)
builder_schnyder.minConnectivity(1)

builder_schnyder.solve(allGraphs=True)
