from graphviz import Digraph


def mockGUI():
    dot = Digraph(comment='The Round Table')

    dot.node('A', 'King Arthur')
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')

    dot.edges(['AB', 'AL'])
    dot.render('test-output/round-table.gv', view=True)
