def naformatuj_text(zak):
    return f"Student {zak["jmeno"]} {zak["prijmeni"]} vek: {zak["vek"]} obor: {zak["obor"]} prumer: {sum(zak["znamky"])/len(zak["znamky"]):.2f}"
    



if __name__ == "__main__":
    student = {
        "jmeno": "Jan", 
        "prijmeni": "Novak", 
        "vek": 22, 
        "znamky": [1,2,3,1,2,1]
    }
    student["vek"] += 1
    student["obor"] = "AEFP"
    print(naformatuj_text(student))
    
   


    





