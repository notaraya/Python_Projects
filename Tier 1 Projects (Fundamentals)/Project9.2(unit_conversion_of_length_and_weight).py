print("Welcome to unit converter ")
length_factors = {"in":0.0254,"ft":0.3048,"m":1.0,"km":1000.0,"mi":1609.344}
weight_factors = {"g":0.001,"oz":0.0283495,"lb":0.453592,"kg":1.0}

while True:
    result = 0
    try:
        what = int(input("Please enter 1 for conversion of length , 2 for weight , 3 to quit : "))
    except:
        print("Please enter a valid input!!")
        continue
    if what == 1 :
        try:
            length = float(input("Please enter the magnitude of value : "))
        except:
            print("Please enter a valid input!!")
            continue
        from_unit = input("Please enter the unit of the value you want to convert from ('in' for inches, 'ft' for feet, 'm' for meter, 'km' for kilometer & 'mi' for miles ) : ")
        if from_unit.lower() not in length_factors :
            print("Please enter a valid input!!")
            continue
        to_unit = input("Please enter the unit of the value you want to convert to ('in' for inches, 'ft' for feet, 'm' for meter, 'km' for kilometer & 'mi' for mile ) : ")
        if to_unit.lower() not in length_factors :
            print("Please enter a valid input!!")
            continue
        result = length * (length_factors[from_unit]/length_factors[to_unit])
        print(f"-> {length} {from_unit} = {result} {to_unit}")
    elif what == 2 :
        try :
            weight = float(input("Please enter the magnitude of the value to want to convert : "))
        except:
            print("Please enter a valid input!!")
            continue
        from_unit = input("Please enter the unit of the value you want to convert from ('g' for gram, 'oz' for ounce, 'lb' for pounds & 'kg' for kilograms) : ")
        if from_unit.lower() not in weight_factors :
            print("Please enter a valid input!!")
            continue
        to_unit = input("Please enter the unit of the value you want to convert to ('g' for gram, 'oz' for ounce, 'lb' for pounds & 'kg' for kilograms) : ")
        if to_unit.lower() not in weight_factors :
            print("Please enter a valid input!!")
            continue
        result = weight * (weight_factors[from_unit]/weight_factors[to_unit])
        print(f"-> {weight} {from_unit} = {result} {to_unit}")
    elif what == 3 :
        break
    else:
        print("Please enter a valid input!!")
        continue
