import random as rd
import tabulate as tb
from collections import Counter



desserts={}
drinks={}
mains={}

def secondMenu(att,hc,number):
    choice=0
    pref=input("Enter preferences file name: ")
    while(choice != 6):
        print("Choose the reasoning task to perform:")
        print("1. Encoding")
        print("2. Feasibility Checking")
        print("3. Show the Table")
        print("4. Exemplification")
        print("5. Omni-optimization")
        print("6. Back to previous menu")
        choice=int(input())
        print("Your choice " + str(choice))

        if(choice==1):
            for h in range( len(read_and_encode(att))):
                print(read_and_encode(att)[h]) 
        elif(choice==2):
            print("There are "+ str(len(feasible(att,hc))) +" feasible objects")
            feasible
        elif(choice==3):
            if(number==1):
                drawTable(pref,att,hc)
            elif(number==2):
                drawTable2(pref,att,hc)
        elif(choice==4):
                if(number==1):
                    exemplification(pref,att,hc)
                elif(number==2):
                    exemplification2(pref,att,hc)
        elif(choice==5):
                if(number==1):
                    optimal(pref,att,hc)
                if(number==2):
                    optimal2(pref,att,hc)
        elif(choice==6):
            mainMenu()

def mainMenu():
    choice=0
    print("Welcome to PrefAgent!")
    att_fn=input("Enter Attributes File Name: ")
    hc_fn=input("Enter hard constraint File Name: ")
    while(choice != 3):
        print("Choose the preference logic to use:")
        print("1. Penalty Logic")
        print("2. Qualitative Choice Logic")
        print("3. Exit")
        print("")
        choice=(input())
        print("your choice: "+ str(choice))
        if(choice=="1"):
            print("You picked Penalty Logic")
            secondMenu(att_fn,hc_fn,1)
            break
        elif(choice=="2"):
            print("You picked Qualitative Choice Logic")
            secondMenu(att_fn,hc_fn,2)
            break
        elif(choice=="3"):
            break
        else:
            print ("Incorrect option")
            print("Choose the preference logic to use:")
            print("1. Penalty Logic")
            print("2. Qualitative Choice Logic")
            print("3. Exit")
            print("")
            choice=(input())
            print("your choice: "+ str(choice))




def read_and_encode(file_path):
    # Read the file and process each line
    with open(file_path, 'r') as file:
        lines = file.readlines()
        attributes = [line.strip().split(': ')[1].split(', ') for line in lines]

        desserts = {attributes[0][0]: 1, attributes[0][1]: 0}
        drinks = {attributes[1][0]: 1, attributes[1][1]: 0}
        mains = {attributes[2][0]: 1, attributes[2][1]: 0}
        

        '''dessert = {'cake': 1, 'ice-cream': 0}
            drink = {'wine': 1, 'beer': 0}
            main = {'fish': 1, 'beef': 0}'''

        objectsRev=[]
        objects=[]
        for i, (dessert, dessert_value) in enumerate(desserts.items()):
            for j, (drink, drink_value) in enumerate(drinks.items()):
                for k, (main, main_value) in enumerate(mains.items()):
                    binary_encoding = [dessert_value, drink_value, main_value]
                    string=(f"o{abs((i*4 + j*2 + k)-7)} - {dessert}, {drink}, {main} <{','.join(map(str, binary_encoding))}>")
                    objectsRev.append(string)

        
        for k in range(len(objectsRev)-1, -1, -1):
            objects.append(objectsRev[k])

    return objects


def feasible(attri,constraint):
    conditions=[]
    elements=[]
    with open(constraint,'r') as constraint:
        for line in constraint:
            words = line.strip().split()
            con_arr=[]
            el_arr=[]
            for word in words:
                # Check if the word is uppercase
                if word.isupper():
                    con_arr.append(word)
                # Check if the word is lowercase
                elif word.islower():
                    el_arr.append(word)
            conditions.append(con_arr)
            elements.append(el_arr)
    
    filtered_objects = []
    objetos=read_and_encode(attri)

    for obj, (cond_op, cond_val) in zip(objetos, zip(conditions, elements)):
        condition_met = True
        
        for operator, value in zip(cond_op, cond_val):
            if operator == 'NOT':
                if value in obj:
                    condition_met = False
                    break
            elif operator == 'OR':
                if value not in obj:
                    condition_met = False
                    break
        
        if condition_met:
            filtered_objects.append(obj)

    # Print the filtered objects
    
    return filtered_objects





def drawTable(preferences, objects, hard_constraint):
    penal={}
    fif={}
    header=["encoding"]
    
    with open(preferences, 'r') as file:
        for line in file:
            # Split the line into expression and value
            expression, value = line.strip().split(', ')
            # Add the expression and value to the dictionary
            penal[expression] = int(value)
            header.append(expression) 
        header.append("total penalty")   
    feasibleObjects=feasible(objects,hard_constraint)
    max_arr=[]
    print(penal)
    for ob in feasibleObjects:
        ob_array=[ob.split()[0]]
        for p in penal:
            pSplit=p.split()
            if(pSplit[1]=="AND"):           
                if(p.split()[0] in ob and p.split()[2] in ob):
                    penalty1=0
                    ob_array.append(penalty1)
                else:
                    penalty1=penal[p]
                    ob_array.append(penalty1)
            elif(pSplit[1]=="OR"):
                if(p.split()[0] in ob or p.split()[2] in ob):
                    penalty2=0
                    ob_array.append(penalty2)
                else:
                    penalty2=penal[p]
                    ob_array.append(penalty2)
                ob_array.append(penalty1+penalty2)
                fif[ob.split()[0]]=(penalty1+penalty2)
        max_arr.append(ob_array)
    print(max_arr)
    print(tb.tabulate(max_arr, headers=header))
    return fif 

def drawTable2(preferences,objects,hard_constraints):
    quali_d=[]
    quali=[]
    with open(preferences, 'r') as file:
        for line in file:
            # Split the line into expression and value
            expression_d= line.strip().split()
            # Add the expression and value to the dictionary
            quali_d.append(expression_d) 
            quali.append(line)
    headers=['encoding']
    max_arr=[]
    f_objects=feasible(objects,hard_constraints)
    for g in f_objects:
        ob_arr=[g.split()[0]]
        for q in quali:
            headers.append(q)
            if(q.split()[-2]=="IF"):
                if(q.split()[-1] in g):
                    if (q.split()[0] in g ):
                        val=1
                        ob_arr.append(val)
                    else:
                        low=[]
                        for word in q.split():
                            if word.islower():
                                low.append(word)
                        val=len(low)-1
                        ob_arr.append(val)
                else:
                    val="inf"
                    ob_arr.append(val)
            elif(q.split()[0] in g):
                val=1
                ob_arr.append(val)
            
            elif(q.split()[-2] in g):
                val=2
                ob_arr.append(val)
    
        max_arr.append(ob_arr)
    print(tb.tabulate(max_arr, headers=headers))
    return max_arr

def exemplification(preferences, objects, hardContraints):
    ob=feasible(objects,hardContraints)
    object1=rd.choice(ob)
    object2=rd.choice(ob)
    p={}
    
    total_objects=drawTable(preferences, objects, hardContraints)
    for o in total_objects:
        if object1.split()[0]==o:
            p[o]=total_objects[o]
        if object2.split()[0]==o:
            p[o]=total_objects[o]

    min_key = min(p, key=p.get)
    max_key = max(p, key=p.get)



    print("Two randomly selected feasible objects are "+ object1.split()[0]+" and "+ object2.split()[0] +" and "+ min_key+" is strictly preferred over "+ max_key) 
   
def exemplification2(preferences, objects, hardContraints):
    ex_arr=drawTable2(preferences, objects, hardContraints)
    ob1=rd.choice(ex_arr)
    ob2=rd.choice(ex_arr)
    
    for i in range(len(ob1)):
        if ob1[i] == ob2[i] == 'inf':
            sum1=sum(x for x in ob1 if isinstance(x, int))
            sum2=sum(x for x in ob2 if isinstance(x, int))
            if sum1 > sum2:
                print(ob2[0]+" is strictly preferred over "+ ob1[0])
            elif sum2 > sum1:
                print(ob1[0]+" is strictly preferred over "+ ob2[0])
            else:
                print("same")
        if ob1[i] == 'inf' and ob2[i] != 'inf':
            print(ob1[0]+" and "+ob2[0]+" are incomparable")
            break
        elif ob1[i] != 'inf' and ob2[i] == 'inf':
            print(ob1[0]+" and "+ob2[0]+" are incomparable")
            break


def optimal(preferences, objects, hardContraints):
    f=drawTable(preferences, objects, hardContraints)
    min_value = min(f.values())

    # Get the keys associated with the minimum value
    min_keys = [key for key, value in f.items() if value == min_value]

    print("All optimal objects are: ", min_keys)

def optimal2(preferences, objects, hardContraints):
    exarr=drawTable2(preferences, objects, hardContraints)
    most_arr=[]

    for i in range(len(exarr)):
        for j in range(i + 1, len(exarr)):
            sum1=sum(x for x in exarr[i] if isinstance(x, int))
            sum2=sum(x for x in exarr[j] if isinstance(x, int))
            if sum1 > sum2:
                most_arr.append(exarr[j])   
            elif sum2 > sum1:
                most_arr.append(exarr[i])  


    array_tuples = [tuple(lst) for lst in most_arr]

    # Count the occurrences of each element using Counter
    element_counts = Counter(array_tuples)

    # Find the element that appears the most times
    most_common_element, max_occurrences = element_counts.most_common(1)[0]

    print("All optimal objects are: "+ str((most_common_element)[0]))


mainMenu()

