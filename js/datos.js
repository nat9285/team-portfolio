let url = './json/datos.json'
fetch(url)
    .then(response => response.json())
    .then(data => {  

        separador = " | "

        let titulo = document.getElementById("title").textContent
        titulo += separador + data.datos.nombre
        document.getElementById("title").textContent = titulo;

        let profesion = document.getElementById("profesion").textContent;
        profesion = data.informacion.profesion;
        document.getElementById("profesion").textContent = profesion;

        
        let sobremi = document.getElementById("sobremi").textContent;
        sobremi = data.informacion.sobremi;
        document.getElementById("sobremi").textContent = sobremi;

        let biografia = document.getElementById("biografia").textContent;
        biografia = data.informacion.biografia;
        document.getElementById("biografia").textContent = sobremi;
    }

    )