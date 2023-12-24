let url = './json/datos.json'

/* nota : hacer un fetch por página */

fetch(url) // index
    .then(response => response.json())
    .then(data => {  

        separador = " | "

        let titulo = document.getElementById("title").textContent
        titulo += separador + data.datos.nombre
        document.getElementById("title").textContent = titulo;

        let profesion = document.getElementById("profesion").textContent;
        profesion = data.informacion.profesion;
        document.getElementById("profesion").textContent = profesion;
        
        let sobremi = document.getElementById("sobre").textContent;
        sobre = data.informacion.sobre;
        document.getElementById("sobre").textContent = sobre;

        let biografia = document.getElementById("biografia").textContent;
        biografia = data.informacion.biografia;
        document.getElementById("biografia").textContent = biografia;
    }

    

    )

    fetch(url) // biography
    .then(response => response.json())
    .then(data => {  

        separador = " | "

        let titulo = document.getElementById("title").textContent
        titulo += separador + data.datos.nombre
        document.getElementById("title").textContent = titulo;

        let sobremi = document.getElementById("sobre").textContent;
        sobre = data.informacion.sobre;
        document.getElementById("sobre").textContent = sobre;

        let biografia = document.getElementById("biografia").textContent;
        biografia = data.informacion.biografia;
        document.getElementById("biografia").textContent = biografia;
    }

    

    )