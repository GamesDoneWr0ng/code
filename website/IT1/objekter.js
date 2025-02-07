// Oppgave 1
let informasjonsteknologi1 = {
    språk: ["HTML", "CSS", "Javascript"],
    likerFaget: true,
    timetall: 5,
    klasserom: "C14",
    antallElever: 15
};

delete informasjonsteknologi1.timetall;

informasjonsteknologi1.språk.forEach((språk) => {
    console.log(språk);
});
// HTML
// CSS
// Javascript

for (let key in informasjonsteknologi1) {
    console.log(key, informasjonsteknologi1[key]);
}
// språk [ 'HTML', 'CSS', 'Javascript' ]
// likerFaget true
// klasserom C14
// antallElever 15

// Oppgave 2
const filmer = [
    { tittel: "Inception", regissør: "Christopher Nolan", sett: true },
    { tittel: "The Godfather", regissør: "Francis Ford Coppola", sett: false },
    { tittel: "Pulp Fiction", regissør: "Quentin Tarantino", sett: false },
    { tittel: "The Dark Knight", regissør: "Christopher Nolan", sett: false },
    { tittel: "Fight Club", regissør: "David Fincher", sett: false }
];

filmer.sort((a,b) => a.tittel>b.tittel?1:-1);

filmer.forEach((i) => {
    console.log(`Jeg har${i.sett?"":" ikke"} sett ${i.tittel} av ${i.regissør}`);
});
// Jeg har ikke sett Fight Club av David Fincher
// Jeg har sett Inception av Christopher Nolan
// Jeg har ikke sett Pulp Fiction av Quentin Tarantino
// Jeg har ikke sett The Dark Knight av Christopher Nolan
// Jeg har ikke sett The Godfather av Francis Ford Coppola

// Oppgave 3
let figurer = [{
    form: "rektangel",
    lengde: 4,
    bredde: 6,
    areal: 24,
    omkrets: 20
}, {
    form: "rektangel",
    lengde: 4,
    bredde: 6,
    areal: 24,
    omkrets: 20
}, {
    form: "rektangel",
    lengde: 9,
    bredde: 1,
    omkrets: 20
}, {
    form: "kvadrat",
    lengde: 4,
    bredde: 4,
    areal: 16
}, {
    from: "kvadrat",
    lengde: 6,
    bredde: 6,
}
];

function info(figur) {
    for (let key in figur) {
        console.log(key, figur[key]);
    }
}

function antallMetoder(figur) {
    return Object.keys(figur).length;
}

function sammenlign(a, b) {
    if (antallMetoder(a) !== antallMetoder(b)) {
        return false;
    }
    for (let key in a) {
        if (a[key] !== b[key]) {
            return false;
        }
    }
    return true;
}

function likheter(a, b) {
    let ny = {};
    for (let key in a) {
        if (a[key] === b[key]) {
            ny[key] = a[key];
        }
    }
    return ny;
}

for (let i = 0; i < figurer.length; i++) {
    for (let j = 0; j < figurer.length; j++) {
        //console.log(i, j, sammenlign(figurer[i], figurer[j]));
        console.log(i, j, likheter(figurer[i],figurer[j]))
    }
}
