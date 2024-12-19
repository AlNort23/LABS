from mindmap_leaf import MindMapLeaf
from mindmap_composite import MindMapComposite


def main():
    print("mindmap")

    root = MindMapComposite("Python at CR", "circle")

    skills = MindMapComposite("Skills Gained", "plain")
    skills.add(MindMapLeaf("Problem-solving abilities", "plain"))
    skills.add(MindMapLeaf("Logical thinking", "plain"))
    skills.add(MindMapLeaf("Writing clean, readable code", "plain"))
    root.add(skills)

    careers = MindMapComposite("Career Paths", "plain")
    careers.add(MindMapLeaf("Local tech companies", "plain"))
    careers.add(MindMapLeaf("Remote work opportunities", "plain"))
    careers.add(MindMapLeaf("Starting own tech business", "plain"))
    root.add(careers)

    concepts = MindMapComposite("Concepts Covered", "plain")
    concepts.add(MindMapLeaf("Variables, Expressions and Statements", "plain"))
    concepts.add(MindMapLeaf("Functions", "plain"))
    concepts.add(MindMapLeaf("Interface Design", "plain"))
    concepts.add(MindMapLeaf("Conditionals and Recursion", "plain"))
    concepts.add(MindMapLeaf("Iteration", "plain"))
    concepts.add(MindMapLeaf("Strings, Lists, Dictionaries", "plain"))
    concepts.add(MindMapLeaf("Tuples", "plain"))
    root.add(concepts)

    print("  root((Python at CR))")
    # Start children at indent level 4 (2 more than root)
    for child in root.children:
        child.display(4)


if __name__ == "__main__":
    main()