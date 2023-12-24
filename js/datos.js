let url = './json/datos.json'
fetch(url)
    .then(response => response.json())
    .then(data => {  

        let titulo = document.getElementById("title").textContent
        titulo += " | " + data.nombre

        console.log(titulo)
        document.getElementById("title").textContent = titulo;
    }
    );