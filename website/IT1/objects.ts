interface Person {
    name: string,
    adresse: string,
    hobbyer: string[]
}

function createPerson(name?: string | null, adresse?: string | null, hobbyer?: string[] | null): Person {
    let person: Person = {name: "Empty", adresse: "Empty", hobbyer: ["None"]};
    if (name) person.name = name;
    if (adresse) person.adresse = adresse;
    if (hobbyer) person.hobbyer = hobbyer;

    return person;
}

let person: Person = createPerson(null,undefined,["Sykling", "Lesing"]);

for (let i in person) {
    console.log(person[i]);
}