import networkx as nx
import matplotlib.pyplot as plt

my_list = [['Hadiach', 'Zinkiv', 45],['Zinkiv', 'Hadiach', 45], ['Hadiach', 'Lebedyn', 60], ['Lebedyn', 'Hadiach', 60],
           ['Hadiach','Myrhorod', 61], ['Myrhorod', 'Hadiach', 61], ['Hadiach', 'Zavodske', 67], ['Zavodske', 'Hadiach', 67],
           ['Hadiach', 'Romny', 71], ['Hadiach', 'Lokhvytsia', 81], ['Lokvytsia', 'Hadiach', 81], ['Hadiach', 'Vorozhba', 94],
           ['Hadiach', 'Bilopillia',94],['Kharkiv','Derhachi',23], ['Derhachi', 'Liubotyn', 26], ['Derhachi', 'Pivdenne', 26],
           ['Kharkiv', 'Bilopillia', 229],['Derhachi', 'Hadiach',194], ['Liubotyn', 'Hadiach', 175],
           ['Liubotyn', 'Lokhvytsia', 320], ['Bilopillia', 'Lokhvytsia', 133]]

g = nx.Graph()
for i in my_list :
    g.add_edge(i[0], i[1], weight=i[2])

pos = nx.spiral_layout(g)
nx.draw_networkx(g,pos)
plt.title("Мій граф ")
plt.show()


