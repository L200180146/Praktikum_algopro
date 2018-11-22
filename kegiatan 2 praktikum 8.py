def konversiSuhu(C = "none", F = "none"):
    "mengkonversikan suhu dari Celcius ke Fahrenheit dan sebaliknya"
    suhu = 0
    if (C == "none") and (F == "none"):
        print ("Suhu 0 Celcius setara dengan 32 Fahrenheit")
    elif (C == "none") and (F == "none"):
        suhu = (F - 32) * 5/9
        print "Suhu", F, "Fahrenheit setara dengan", int(suhu), "Celcius"
    elif (C != "none") and (F == "none"):
        suhu = (C * 9/5) + 32
        print "Suhu", C, "Celcius setara dengan", int(suhu), "Fahrenheit"
