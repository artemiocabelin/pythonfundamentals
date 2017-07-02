my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_in_tup_out(dict_in):
    tup_out = []
    for key in dict_in:
        tup_pair = (key,dict_in[key])
        tup_out.append(tup_pair)
    print tup_out

dict_in_tup_out(my_dict)







# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]