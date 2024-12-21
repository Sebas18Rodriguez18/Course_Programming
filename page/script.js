document.getElementById('jsButton').addEventListener('click', function() {
    displayInfo('JavaScript', 'JavaScript es un lenguaje de programación de alto nivel que se utiliza para crear sitios web interactivos.');
});

document.getElementById('pythonButton').addEventListener('click', function() {
    displayInfo('Python', 'Python es un lenguaje de programación interpretado que se utiliza para crear aplicaciones web y móviles.');
});

document.getElementById('javaButton').addEventListener('click', function() {
    displayInfo('Java', 'Java es un lenguaje de programación de propósito general que se utiliza para crear aplicaciones empresariales.');
});

document.
getElementById('phpButton').addEventListener('click', function() {
    displayInfo('PHP', 'PHP es un lenguaje de programación de servidor que se utiliza para crear aplicaciones web dinámicas.');
});


function displayInfo(title, description) {
    const infoDiv = document.getElementById('info');
    infoDiv.innerHTML = `<h3>${title}</h3><p>${description}</p>`;
    infoDiv.style.display = 'block';
    setTimeout(() => {
        infoDiv.style.opacity = '1';
    }, 10);
}