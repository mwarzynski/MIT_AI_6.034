from production import AND, OR, NOT, PASS, FAIL, IF, THEN, \
     match, populate, simplify, variables
from zookeeper import ZOOKEEPER_RULES

# This function, which you need to write, takes in a hypothesis
# that can be determined using a set of rules, and outputs a goal
# tree of which statements it would need to test to prove that
# hypothesis. Refer to the problem set (section 2) for more
# detailed specifications and examples.

# Note that this function is supposed to be a general
# backchainer.  You should not hard-code anything that is
# specific to a particular rule set.  The backchainer will be
# tested on things other than ZOOKEEPER_RULES.

# Matching consequent:
#     - insert variable in antecedent
#     - it's a new hypothesis
#
# Get rules by hypothesis.
#     - if no statements, it's a leaf
#     - if there are statements:
#         do OR on the statements
#
# AND or OR:
#     - check leaves of AND-OR tree
#     - recursively backward chain on them
#
# # Useful functions/methods provided by MIT:
#
# match(leaf_a, leaf_b) : {None, {bindings}}, where bindings are values for x, y, etc.
# match("(?x) is a (?y)", "John is a student") => { x: "John", y: "student" }
#
# populate(exp, bindings)
# populate("(?x) is a (?y)", { x: "John", y: "student" }) => "John is a student"
#
# rule.antecedent(): returns the IF part of a rule
# rule.consequent(): returns the THEN part of a rule

def backchain_to_goal_tree(rules, hypothesis):
    if not rules:
        return hypothesis

    tree = OR(hypothesis)

    for rule in rules:
        for consequent in rule.consequent():
            matches = match(consequent, hypothesis)
            if matches == None:
                continue

            variables = {}
            for name, value in matches.items():
                variables[name] = value

            antecedents = rule.antecedent()

            # If antecedents is a string, behave as it is a list with single item - unify antecedents handling
            if isinstance(antecedents, str):
                antecedents = [antecedents]

            # Determine type of antecedents
            if isinstance(rule.antecedent(), AND):
                statements = AND()
            else:
                statements = OR()

            # For each antecedent generate new possible subtree
            for antecedent in antecedents:
                new_hypothesis = populate(antecedent, variables)
                subtree = backchain_to_goal_tree(rules, new_hypothesis)
                statements.append(subtree)

            tree.append(simplify(statements))

    return simplify(tree)

# Here's an example of running the backward chainer - uncomment
# it to see it work:
# print(backchain_to_goal_tree(ZOOKEEPER_RULES, 'opus is a penguin'))
