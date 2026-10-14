print("Welcome To the unit converter ")
length_ranking = ["i","f","m","km","mi"]
length_symbol = ["in","ft","m","km","mi"]
unit_list_l = [12,3.281,1000,1.609344]

weight_ranking = ["g","o","p","k"]
weight_symbol = ["g","oz","lb","kg"]
unit_list_w = [28.3495,16,2.20462]

while True :
    conversion_from = 0
    conversion_to = 0
    try:
        what = int(input("Please enter a 1 for length conversion or 2 for weight conversion  or '3' to quit : "))
    except:
        print("Please enter a valid input")
        continue
    if what == 1 :
        try:
            length = float(input("Please enter the magnitude of the value : "))
        except:
            print("the value you have entered is invalid!!")
            continue
        converted_length = length
        convert_from_l = input("Please enter the unit of the magnitude you just entered ('f' for feet , 'i' for inches , 'm' for meters , 'km' for kilometers , 'mi' for miles ) : ")
        convert_to_l = input("Please enter the unit to convert into ('f' for feet , 'i' for inches , 'm' for meters , 'km' for kilometers , 'mi' for miles ) : ")
        if (convert_from_l.lower()  in length_ranking ) and (convert_to_l.lower() in length_ranking ):
            for value,len_cons in enumerate(length_ranking) :
                if convert_from_l.lower() == len_cons :
                    conversion_from = value
                if convert_to_l.lower() == len_cons:
                    conversion_to = value
            tem_conversion = conversion_from
            if conversion_to == conversion_from:
                print("not possible rewrite!!")
                continue
            elif conversion_to > conversion_from :
                for conversion in range(len(length_ranking)) :
                    converted_length = converted_length/unit_list_l[tem_conversion]
                    tem_conversion = tem_conversion + 1
                    if tem_conversion == conversion_to :
                        break
            elif conversion_from > conversion_to :
                for conversion in range(len(length_ranking)):
                    tem_conversion = tem_conversion -1
                    converted_length = converted_length * unit_list_l[tem_conversion]
                    if tem_conversion == conversion_to:
                        break

            else :
                print("explain me how!!")
                continue
            print(f"you conveted {length} {length_symbol[conversion_from]} to {converted_length} {length_symbol[conversion_to]}")
        else :
            print("please enter a valid unit")
            continue
    elif what == 2 :
        conversion_from = 0
        conversion_to = 0
        try :
            weight = float(input("Please enter the magnitude of the value : "))
        except:
            print("Please enter a valid input!!")
            continue
        converted_weight = weight
        convert_from_w = input("Please enter the unit you want to convert from by ('g' for gram , 'o' for ounce , 'p' for pound and 'k' for kg) :  ")
        convert_to_w = input("Please enter the unit you want to convert into by ('g' for gram , 'o' for ounce , 'p' for pound and 'k' for kg) :  ")
        if ( convert_from_w.lower() in weight_ranking) and (convert_to_w.lower() in weight_ranking):
            for value,weg_cons in enumerate(weight_ranking):
                if convert_from_w.lower() == weg_cons :
                    conversion_from = value
                if convert_to_w.lower() == weg_cons :
                    conversion_to = value
            tem_conversion = conversion_from
            if conversion_from == conversion_to :
                print("You can't convert a same value to itself !!")
                continue
            elif conversion_to > conversion_from :
                for conversion in range (len(weight_ranking)):
                    converted_weight = converted_weight/unit_list_w[tem_conversion]
                    tem_conversion = tem_conversion +1
                    if tem_conversion == conversion_to :
                        break
            elif conversion_from > conversion_to:
                for conversion in range (len(weight_ranking)):
                    tem_conversion = tem_conversion -1
                    converted_weight = converted_weight* unit_list_w[tem_conversion]
                    if tem_conversion == conversion_to :
                        break
            else :
                print("explain me how!!")
                continue
        else :
            print("please enter a valid unit")
            continue
        print(f"you conveted {weight} {weight_symbol[conversion_from]} to {converted_weight} {weight_symbol[conversion_to]}")
    elif what == 3:
        break
    else:
        print("Please enter a valid input !!")
        continue
    quit = input("please enter q to quit : ")
    if quit.lower() == "q" :
        break
