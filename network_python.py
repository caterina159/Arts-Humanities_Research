import csv
import pandas as pd
import networkx as nx
import argparse



with open(r"C:\Users\keric\Downloads\quakers_nodelist.csv", "r") as nodecsv: # Open the file
    nodereader = csv.reader(nodecsv) # Read the csv
    # Retrieve the data (using Python list comprhension and list slicing to remove the header row)

    nodes = [n for n in nodereader][1:]
    #print(nodes)
node_names = [n[0] for n in nodes] # Get a list of only the node names
#print(node_names) 
#transform nodes into a pandas dataframe
pd_nodes = pd.DataFrame(nodes)
#print(pd_nodes)
#add names to the columns
pd_nodes.columns =["Name", "Historical Significance", "Gender", "Birth date", "Death date", "ID"]
#print(pd_nodes)

with open(r"C:\Users\keric\Downloads\quakers_edgelist.csv", "r") as edgecsv: # Open the file
    edgereader = csv.reader(edgecsv) # Read the csv
    edges = [tuple(e) for e in edgereader][1:] # Retrieve the data
    #print(edges)
#transform edges into a pandas dataframe
pd_edges = pd.DataFrame(edges)
#print(pd_edges)
#add names to the columns
pd_edges.columns =["Source", "Target"]
#print(pd_edges)    

#create graph from dataframe
graph = nx.from_pandas_edgelist(pd_edges, source="Source", target="Target")
#print(graph)
#nx.draw_spring(graph, with_labels=True, node_size=20, font_size=2)
#plt.show()
# Iterate over df rows and set the target nodes' and node-attributes for each row:
for index, row in pd_nodes.iterrows():
    graph.nodes[row[0]]["attr_dict"] = row.iloc[1:].to_dict() 

#use argparse for command line argument
parser = argparse.ArgumentParser()
parser.add_argument("--birth_year", type=str)
#add another argument death_year 
#parser.add_argument("--death_year", type=str)
#add another argument significance
#parser.add_argument("--significance", type=str)
#add another argument gender
parser.add_argument("--gender", type=str)
args = parser.parse_args()
#print(args.birth_year, "birth year")
#the argument is birth_year
#print(args.death_year, "death year")
#the argument is death_year
#print(args.significance, "significance")
#the argument is significance
#print(args.gender, "gender")
#the argument is gender
#for n in graph.nodes(): # Loop through every node, in our data "n" will be the name of the person
  #if args.birth_year == graph.nodes[n]["attr_dict"]["Birth date"] and args.death_year == graph.nodes[n]["attr_dict"]["Death date"] and args.significance == graph.nodes[n]["attr_dict"]["Historical Significance"] and args.gender == graph.nodes[n]["attr_dict"]["Gender"]:
    #print(n, graph.nodes[n]["attr_dict"]["Birth date"]) # Access every node by its name, and then by the attribute "birth_year" 
    #print(n, graph.nodes[n]["attr_dict"]["Death date"]) # Access every node by its name, and then by the attribute "death_year" 
    #print(n, graph.nodes[n]["attr_dict"]["Historical Significance"]) # Access every node by its name, and then by the attribute "significance" 
    #print(n, graph.nodes[n]["attr_dict"]["Gender"]) # Access every node by its name, and then by the attribute "gender" 
for n in graph.nodes():
    if args.gender == graph.nodes[n]["attr_dict"]["Gender"] == "male" and args.birth_year == graph.nodes[n]["attr_dict"]["Birth date"] >= "1610" and args.birth_year == graph.nodes[n]["attr_dict"]["Birth date"] <= "1700":
        print(n, graph.nodes[n]["attr_dict"]["Gender"])
        print(n, graph.nodes[n]["attr_dict"]["Birth date"])

#print(graph.nodes())

#print(pd_nodes)




    
