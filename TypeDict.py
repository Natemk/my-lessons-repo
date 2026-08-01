"""
from typing import TypedDict

class Vision(TypedDict):
    context : str
    search_strategy: str
    number_of_results: int

vision=Vision(context="I want to learn about Python programming.", search_strategy="Use online tutorials and documentation.", number_of_results=5)

def llm_call(vision: Vision) -> str:
    # Simulating a call to a language model with the provided vision
    return f"Context: {vision['context']}\nSearch Strategy: {vision['search_strategy']}\nNumber of Results: {vision['number_of_results']}"

llm_call_response = llm_call(vision)

print(llm_call_response)


from numpy.f2py.crackfortran import f

from typing import Union

def square(x: Union[str, int]) -> float:
    return x * x

x =5
x = 1.778
x = "Hello"

print(square(x))
"""
"""
from typing import Optional

def nice_message(name: Optional[str]) -> None:
    if name is None:
        return ("Hello, Guest!")
    else:
        return (f"Hello, {name}!")

name = nice_message(None)

print(name)
"""
#HEllo World Graph
"""
Objectives:
1. Understand the concept of a graph and its components (nodes and edges).
2. Learn how to represent a graph using an adjacency list or adjacency matrix.
3. Implement basic graph traversal algorithms (BFS and DFS).
4. Explore real-world applications of graphs in various domains.
5. Gain hands-on experience in solving graph-related problems using programming.
6. Understand the time and space complexity of graph algorithms.
7. Learn about directed and undirected graphs, weighted and unweighted graphs, and their properties.
8. Explore advanced graph algorithms such as Dijkstra's algorithm, Prim's algorithm, and Kruskal's algorithm.
9. Understand the concept of graph connectivity and components.
10. Learn about graph coloring and its applications in scheduling and resource allocation.
11. Explore graph algorithms for finding shortest paths, minimum spanning trees, and maximum flow.
12. Gain insights into graph theory concepts such as Eulerian and Hamiltonian paths, cycles, and circuits.
13. Understand the concept of graph isomorphism and its implications in various fields.
14. Learn about graph algorithms for solving real-world problems such as social network analysis, recommendation systems, and route optimization.
15. Gain proficiency in using graph libraries and tools for efficient graph representation and manipulation.
16. Understand the limitations and challenges of graph algorithms and explore potential solutions.
17. Learn about graph visualization techniques and tools for better understanding and communication of graph structures.
18. Explore advanced topics in graph theory such as spectral graph theory, random graphs, and graph embeddings.
19. Gain insights into the applications of graphs in machine learning, data mining, and network analysis.
20. Understand the ethical considerations and implications of using graph algorithms in various domains.
21. Explore the concept of dynamic graphs and their applications in real-time systems.
22. Learn about graph algorithms for solving optimization problems and decision-making processes.
23. Gain proficiency in analyzing and interpreting graph data for actionable insights.
24. Understand the concept of graph databases and their advantages over traditional relational databases.
25. Explore the use of graphs in modeling complex systems and networks.
26. Learn about graph algorithms for solving combinatorial problems and optimization tasks.
27. Gain insights into the applications of graphs in bioinformatics, cheminformatics, and computational biology.
28. Understand the concept of graph algorithms for solving routing and transportation problems.
29. Explore the use of graphs in modeling social networks, communication networks, and information networks.
30. Learn about graph algorithms for solving scheduling and resource allocation problems.
31. Gain proficiency in implementing graph algorithms using programming languages such as Python, Java, or C++.
32. Understand the concept of graph algorithms for solving clustering and community detection problems.
33. Explore the use of graphs in modeling financial networks, supply chains, and logistics systems.
34. Learn about graph algorithms for solving recommendation and personalization problems.
35. Gain insights into the applications of graphs in natural language processing, computer vision, and robotics.
36. Understand the concept of graph algorithms for solving network flow and connectivity problems.
37. Explore the use of graphs in modeling biological networks, ecological systems, and environmental processes.
38. Learn about graph algorithms for solving optimization problems in energy systems and smart grids.
39. Gain proficiency in analyzing and visualizing graph data using libraries such as NetworkX, Graph-tool, or igraph.
40. Understand the concept of graph algorithms for solving problems in distributed systems and parallel computing.
41. Explore the use of graphs in modeling transportation networks, logistics systems, and urban planning.
42. Learn about graph algorithms for solving problems in wireless networks, sensor networks, and IoT systems.
43. Gain insights into the applications of graphs in cybersecurity, fraud detection, and anomaly detection.
44. Understand the concept of graph algorithms for solving problems in recommendation systems and collaborative filtering.
45. Explore the use of graphs in modeling knowledge graphs, semantic networks, and ontologies.
46. Learn about graph algorithms for solving problems in social network analysis, influence maximization, and information diffusion.
47. Gain proficiency in implementing graph algorithms using parallel and distributed computing frameworks such as Apache Spark or Hadoop.
48. Understand the concept of graph algorithms for solving problems in computer graphics, image processing, and computer vision.
49. Explore the use of graphs in modeling transportation systems, traffic flow, and route optimization.
50. Learn about graph algorithms for solving problems in bioinformatics, genomics, and proteomics.
51. Gain insights into the applications of graphs in recommendation systems, personalization, and user behavior analysis.
52. Understand the concept of graph algorithms for solving problems in network security, intrusion detection, and vulnerability analysis.
53. Explore the use of graphs in modeling financial networks, risk analysis, and portfolio optimization.
54. Learn about graph algorithms for solving problems in supply chain management, logistics optimization, and inventory management.
55. Gain proficiency in analyzing and interpreting graph data for decision-making and strategic planning.
56. Understand the concept of graph algorithms for solving problems in transportation planning, traffic management, and route optimization.
57. Explore the use of graphs in modeling social networks, online communities, and user interactions.
58. Learn about graph algorithms for solving problems in recommendation systems, collaborative filtering, and content personalization.
59. Gain insights into the applications of graphs in natural language processing, text mining, and information retrieval.
60. Understand the concept of graph algorithms for solving problems in computer vision, image segmentation, and object recognition.
61. Explore the use of graphs in modeling biological networks, protein-protein interactions, and metabolic pathways.
62. Learn about graph algorithms for solving problems in network flow, connectivity, and optimization.
63. Gain proficiency in implementing graph algorithms using programming languages such as Python, Java, or C++.
64. Understand the concept of graph algorithms for solving problems in distributed systems, parallel computing, and cloud computing.
65. Explore the use of graphs in modeling transportation networks, logistics systems, and supply chain management.
66. Learn about graph algorithms for solving problems in wireless networks, sensor networks, and IoT systems.
67. Gain insights into the applications of graphs in cybersecurity, fraud detection, and anomaly detection.
68. Understand the concept of graph algorithms for solving problems in recommendation systems, collaborative filtering, and content personalization.
69. Explore the use of graphs in modeling knowledge graphs, semantic networks, and ontologies.
70. Learn about graph algorithms for solving problems in social network analysis, influence maximization, and information diffusion.
"""
#understand and define the AgentState structure
#create simple node functions to process and update state
#Setup basic langgraph structure
#Compile and invoke a LangGraph graph
#Understand how data flows through a single node in LangGraph

from typing import Dict, TypedDict
from langgraph.graph import StateGraph #framework that helps you design and manage the flow of task in application using a graph

# We now create an AgentState - shared data structure that keeps track of information as your application runs. This is a TypedDict that defines the structure of the state.

class AgentState(TypedDict):
    message: str

def greeting_node (state: AgentState) -> AgentState:
    """A simple node that adds a greeting message to state."""
    state["message"] = "Hello," + state["message"] + ", welcome to LangGraph!"
    return state
    
graph = StateGraph(AgentState)

graph.add_node ("greeting_node", greeting_node)

graph.set_entry_point ("greeting_node")
graph.set_finish_point ("greeting_node")

app = graph.compile()


        







