PrefAgent
PrefAgent is a command-line tool that allows you to work with preference relations and make decisions based on them.

Overview
PrefAgent has the following features:

Preferences encoding: Encodes a set of preferences defined in a text file into a binary format.
Feasibility checking: Checks if a given object (defined by a set of attribute values) satisfies a set of hard constraints.
Table drawing: Draws a table showing the total penalty or quality level for each object based on the given preferences.
Exemplification: Provides an example of two objects that are comparable according to the given preferences.
Optimization: Returns the optimal objects based on the given preferences.
Getting Started
To use PrefAgent, you need to have a Python environment installed. You can then download the code and run the mainMenu() function.

You will be asked to input the file names of the attributes and hard constraints, as well as choose the preference logic to use (Penalty Logic or Qualitative Choice Logic).

Penalty Logic

The Penalty Logic assigns a penalty to each object based on the number of preferences it violates. The lower the penalty, the more preferred the object.

Qualitative Choice Logic

The Qualitative Choice Logic assigns a quality level to each object based on the preferences it satisfies. The higher the quality level, the more preferred the object.

Functions
read_and_encode(file_path)

Reads the attributes and their values from a text file and encodes them into a binary format.

feasible(attri, constraint)

Checks if a given object satisfies a set of hard constraints.

drawTable(preferences, objects, hard_constraint)

Draws a table showing the total penalty for each object based on the given preferences.

drawTable2(preferences, objects, hard_constraints)

Draws a table showing the quality level for each object based on the given preferences.

exemplification(preferences, objects, hard_constraints)

Provides an example of two objects that are comparable according to the given preferences.

exemplification2(preferences, objects, hard_constraints)

Provides an example of two objects that are comparable according to the given preferences, using the Qualitative Choice Logic.

optimal(preferences, objects, hard_constraints)

Returns the optimal objects based on the given preferences, using the Penalty Logic.

optimal2(preferences, objects, hard_constraints)

Returns the optimal objects based on the given preferences, using the Qualitative Choice Logic.
